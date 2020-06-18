"""
 *  @author nhphung

    ID:   1711872
    Name: Dinh Hoang Kim
    Assignment 03 - Micro C Language - StaticCheck.py
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *
import functools

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def getSymbolName(self):
        return self.name

    def getFromDecl(decl):
        if type(decl) is FuncDecl:
            return Symbol(decl.name.name, MType([i.varType for i in decl.param], decl.returnType))
        else:
            return Symbol(decl.variable, decl.varType)

class raiseError:
    utils = Utils()

    def raiseRedeclared(lst, lstSymbol):
        temp = lst.copy()
        for i in lstSymbol:
            check = raiseError.utils.lookup(i.name, temp, Symbol.getSymbolName)
            if check is not None:
                if type(i.mtype) is MType:
                    raise Redeclared(Function(), i.name) 
                else:
                    raise Redeclared(Variable(), i.name)
            temp.append(i)
        return temp

    def checkMatchingPara(pattern, currentPara):
        if len(currentPara) == len(pattern):
            return functools.reduce(lambda y, x: y and raiseError.checkMatchingType(x[0], x[1]),zip(pattern, currentPara), True)
        else:
            return False

    def checkMatchingType(patternType, paraType):
        if type(patternType) is ArrayPointerType:
            if type(paraType) in [ArrayType, ArrayPointerType] and type(patternType.eleType) is type(paraType.eleType):
                return True
        elif type(patternType) is FloatType:
            if type(paraType) in [IntType, FloatType]: 
                return True
        elif type(patternType) is type(paraType):
            return True
        else:
            return False

    def checkReturnStatement(stateList):
        for i in filter(lambda x: isinstance(x, list), stateList):
            if i[0] is not None:
                return i[0]
        return None


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast    

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):

        declList = raiseError.raiseRedeclared(StaticChecker.global_envi, [Symbol.getFromDecl(i) for i in ast.decl])

        funcList = [i.name.name for i in filter(lambda x: type(x) is FuncDecl, ast.decl)] + [i.name for i in c]

        funcCall = [i.name for i in c]

        res = self.lookup('main', declList, lambda x: x.name)

        if res is None or type(res.mtype) is not MType:
            raise NoEntryPoint()

        visit = [self.visit(decl, [declList, funcCall]) for decl in ast.decl]

        funcList.remove('main')
        checkReachable = list(set(funcList) - set(funcCall))

        if len(checkReachable) == 0:
            return visit
        else:
            raise UnreachableFunction(checkReachable[0])

    def visitFuncDecl(self, ast, c):
        try:
            para = raiseError.raiseRedeclared([], [Symbol.getFromDecl(i) for i in ast.param])
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)

        env = [para] + [[Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType))] + c[0]]
        bodyState = []

        for decl in ast.body.member:
            if type(decl) is VarDecl:
                env = [raiseError.raiseRedeclared(env[0], self.visit(decl, env)), env[1]]
            else:
                bodyState.append(self.visit(decl, (env, ast.returnType, False, ast.name.name, c[1])))

        stateType = raiseError.checkReturnStatement(bodyState)

        if type(ast.returnType) is not VoidType and type(stateType) is not Return:
            raise FunctionNotReturn(ast.name.name)

        return [Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType))]

    def visitVarDecl(self, ast, c):
        return [Symbol(ast.variable, ast.varType)]

    def visitBlock(self, ast, c):

        refEnv, funcType, inLoop, funcName, funcCall = c

        env = [[]] + refEnv

        stateList = []

        for decl in ast.member:
            if type(decl) is VarDecl:
                env = [raiseError.raiseRedeclared(env[0], self.visit(decl, env))] + env[1:]
            else:
                stateList += [self.visit(decl, (env, funcType, inLoop, funcName, funcCall))]

        return [raiseError.checkReturnStatement(stateList)]

    def visitIf(self,ast,c):
        retThen = False
        retElse = False

        if not type(self.visit(ast.expr,c)) is BoolType:
            raise TypeMismatchInStatement(ast)

        retThen = self.visit(ast.thenStmt,c)

        if not ast.elseStmt is None:
            retElse = self.visit(ast.elseStmt,c)

        if not isinstance(retElse,bool):
            retElse = False

        if not isinstance(retThen,bool):
            retThen = False

        return retThen and retElse

    def visitFor(self, ast, c):
        refEnv, funcType, inLoop, funcName, funcCall = c

        check1 = self.visit(ast.expr1, c)
        check2 = self.visit(ast.expr2, c)
        check3 = self.visit(ast.expr3, c)

        if type(check1) is not IntType or type(check3) is not IntType or type(check2) is not BoolType:
            raise TypeMismatchInStatement(ast)
        loopStmts = [self.visit(ast.loop, (refEnv, funcType, True, funcName, funcCall))]
        return [None]

    def visitDowhile(self, ast, c):
        refEnv, funcType, inLoop, funcName, funcCall = c

        check = self.visit(ast.exp, c)
        if type(check) is not BoolType:
            raise TypeMismatchInStatement(ast)

        stateList = functools.reduce(lambda y, x: y + [self.visit(x, (refEnv, funcType, True, funcName, funcCall))], ast.sl, [])
        stateType = raiseError.checkReturnStatement(stateList)

        if type(stateType) is Return:
            return [stateType]
        else: 
            return [None]

    def visitBreak(self, ast, c):
        if not c[2]:
            raise BreakNotInLoop()
        return "break"

    def visitContinue(self, ast, c):
        if not c[2]:
            raise ContinueNotInLoop()
        return None

    def visitReturn(self, ast, c):
        refEnv, returnType, inLoop, funcName, funcCall = c

        if ast.expr and type(returnType) is VoidType:
            raise TypeMismatchInStatement(ast)

        exprType = self.visit(ast.expr, c) if ast.expr else VoidType()

        if not raiseError.checkMatchingType(returnType, exprType):
            raise TypeMismatchInStatement(ast)
        return [Return()]
 
    #####################################################################################
    def visitBinaryOp(self, ast, c):
        op = ast.op
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)

        if op=="=":
            if not type(ast.left) is Id and not type(ast.left) is ArrayCell:
                raise NotLeftValue(ast.left)
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is FloatType and type(right) is FloatType:
                return FloatType()
            elif type(left) is FloatType and type(right) is IntType:
                return FloatType()
            elif type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            elif type(left) is StringType and type(right) is StringType:
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op=="&&" or op=="||":
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op=="+" or op=="-" or op=="*" or op=="/":
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            elif type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op==">" or op=="<" or op==">=" or op=="<=":
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
            elif type(left) is FloatType or type(right) is FloatType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op=="==" or op=="!=":
            if type(left) is IntType and type(right) is IntType:
                return BoolType()
            elif type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op=="%":
            if type(left) is IntType and type(right) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)

        else:
            raise TypeMismatchInExpression(ast)
    
    ########################################################################
    def visitUnaryOp(self, ast, c):
        unOp=ast.op
        expr=self.visit(ast.body,c)
        if unOp == '!':
            if isinstance(expr,BoolType):
                return BoolType()
            else: 
                raise TypeMismatchInExpression(ast)
        if unOp == '-':
            if isinstance(expr,(IntType,FloatType)):
                return expr
            else:
                raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        refEnv, returnType, inLoop, funcName, funcCall = c

        env = [i for j in refEnv for i in j]
        at = [self.visit(i, c) for i in ast.param]
        res = self.lookup(ast.method.name, env, lambda x: x.name)
        
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(), ast.method.name)
        elif not raiseError.checkMatchingPara(res.mtype.partype, at):
            raise TypeMismatchInExpression(ast)
        else:
            if ast.method.name != funcName and ast.method.name != 'main':
                funcCall.append(ast.method.name)
            return res.mtype.rettype

    ##################################################################################
    def visitArrayCell(self, ast, c):
        res = None
        if type(ast.arr) is Id:
            res = self.visit(ast.arr,c)
            if not type(res) is ArrayType and not type(res) is ArrayPointerType:
                raise TypeMismatchInExpression(ast)
        else:
            res = self.visit(ast.arr,c)
            if not type(res) is ArrayPointerType:
                raise TypeMismatchInExpression(ast)
        
        if not isinstance(self.visit(ast.idx,c),IntType):
            raise TypeMismatchInExpression(ast)
        else:
            return res.eleType

    def visitId(self, ast, c):
        list = [i for j in c[0] for i in j]
        res = self.lookup(ast.name, list, lambda x: x.name)

        if res is None or type(res.mtype) is MType:
            raise Undeclared(Identifier(), ast.name)
        else:
            return res.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()
        
    def visitIntType(self, ast, c):
        return IntType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitBooleanType(self, ast, c):
        return BoolType()

    def visitStringType(self, ast, c):
        return StringType()