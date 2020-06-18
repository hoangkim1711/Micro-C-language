#
# ID: 1711872
# Name: Dinh Hoang Kim
# Assignment 02 - Micro C Language
#
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MCVisitor):
    
    #Program -------------------------------------------------
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    def visitDecls(self,ctx:MCParser.DeclsContext):
#        if ctx.decls():
#            return self.visit(ctx.one_decl()) + self.visit(ctx.decls()) 
#        else:
#            return self.visit(ctx.one_decl())
        if ctx.decls():
            if isinstance(self.visit(ctx.one_decl()), list):
                return self.visit(ctx.one_decl()) + self.visit(ctx.decls())
            else:
                return [self.visit(ctx.one_decl())] + self.visit(ctx.decls())
        else:
            if isinstance(self.visit(ctx.one_decl()), list):
                return self.visit(ctx.one_decl())
            else:
                return self.visit(ctx.one_decl())    

    def visitOne_decl(self,ctx:MCParser.One_declContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())  
        else:
            return self.visit(ctx.func_decl())

    #Variable decl -------------------------------------------
    def visitVar_decl(self,ctx:MCParser.Var_declContext):
        #return VarDecl([self.visit(ctx.id_list())], self.visit(ctx.prim_type()))
        return [VarDecl(str(x[0]), self.visit(ctx.prim_type())) if x[1] == -1 else VarDecl(str(x[0]), ArrayType(int(x[1]),self.visit(ctx.prim_type()))) for x in self.visit(ctx.id_list())]

    def visitPrim_type(self,ctx:MCParser.Prim_typeContext):
        if ctx.INT_TYPE():
            return IntType()
        elif ctx.FLOAT_TYPE():
            return FloatType()
        elif ctx.BOOLEAN_TYPE():
            return BoolType()
        else:
            return StringType()

    def visitId_list(self,ctx:MCParser.Id_listContext):
        if ctx.id_list():
            if ctx.getChildCount()==3:
                return [[ctx.ID().getText(),-1]] + self.visit(ctx.id_list())  
            else:
                return [[ctx.ID().getText(),ctx.INTLIT().getText()]] + self.visit(ctx.id_list())
        else:
            if ctx.getChildCount()==1:
                return [[ctx.ID().getText(),-1]]  
            else:
                return [[ctx.ID().getText(),ctx.INTLIT().getText()]]

#    def visitId_list(self, ctx:MCParser.Id_listContext):
#        return [self.visit(x) for x in ctx.id_var()]

#    def visitId_var(self,ctx:MCParser.Id_varContext):
#        if ctx.INTLIT():
#            return ArrayCell(Id(ctx.ID().getText()), IntLiteral(int(ctx.INTLIT().getText())))
#        else:
#            return Id(ctx.ID().getText())

    #Function Decl -------------------------------------------
    def visitFunc_decl(self,ctx:MCParser.Func_declContext):
        if ctx.LSB():
            return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_list()),ArrayPointerType(self.visit(ctx.prim_type())),self.visit(ctx.block_state()))]
        else:
            if ctx.prim_type():
                return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_list()),self.visit(ctx.prim_type()),self.visit(ctx.block_state()))]
            else:
                return [FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_list()),VoidType(),self.visit(ctx.block_state()))]
    
    #def visitFunc_type(self, ctx:MCParser.Func_typeContext):
    #    if ctx.output_para():
    #        return self.visit(ctx.output_para())
    #    elif ctx.VOID_TYPE():
    #        return VoidType()
    #    else:
    #        return self.visit(ctx.prim_type())
    
    def visitPara_list(self,ctx:MCParser.Para_listContext):
        if ctx.para_decl():
            return [self.visit(ctx.para_decl())] + self.visit(ctx.re_para())  
        else:
            return []

    def visitRe_para(self,ctx:MCParser.Re_paraContext):
        if ctx.para_decl():
            return [self.visit(ctx.para_decl())] + self.visit(ctx.re_para())  
        else:
            return []

    def visitPara_decl(self,ctx:MCParser.Para_declContext):
        if ctx.LSB():
            return  VarDecl(ctx.ID().getText(), ArrayPointerType(self.visit(ctx.prim_type())))  
        else:
            return VarDecl(ctx.ID().getText(),self.visit(ctx.prim_type()))

    #Block statement -------------------------------------------
    def visitBlock_state(self,ctx:MCParser.Block_stateContext):
        list_state = []
        for x in ctx.statement():
            if isinstance(self.visit(x),list):
                list_state = list_state+self.visit(x)
            else:
                list_state.append(self.visit(x))
        return Block(list_state)

    def visitStatement(self,ctx:MCParser.StatementContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        if ctx.do_while_state():
            return self.visit(ctx.do_while_state())
        elif ctx.if_state():
            return self.visit(ctx.if_state())
        elif ctx.for_state():
            return self.visit(ctx.for_state())
        elif ctx.break_state():
            return self.visit(ctx.break_state())
        elif ctx.continue_state():
            return self.visit(ctx.continue_state())
        elif ctx.return_state():
            return self.visit(ctx.return_state())
        elif ctx.exp():
            return self.visit(ctx.exp())
        else:
            return self.visit(ctx.block_state())
            
    # Statements and Control Flow ------------------------------------
    def visitDo_while_state(self,ctx:MCParser.Do_while_stateContext):
        return Dowhile([self.visit(x) for x in ctx.statement()], self.visit(ctx.exp()))

    def visitIf_state(self,ctx:MCParser.If_stateContext):
        if (ctx.ELSE()):
            if (isinstance(self.visit(ctx.statement(0)), list) and isinstance(self.visit(ctx.statement(1)),list)):
                return If(self.visit(ctx.exp()), Block(self.visit(ctx.statement(0))), Block(self.visit(ctx.statement(1))))
            if (isinstance(self.visit(ctx.statement(0)), list)):
                return If(self.visit(ctx.exp()), Block(self.visit(ctx.statement(0))), self.visit(ctx.statement(1)))
            if (isinstance(self.visit(ctx.statement(1)), list)):
                return If(self.visit(ctx.exp()), self.visit(ctx.statement(0)), Block(self.visit(ctx.statement(1))))
            return If(self.visit(ctx.exp()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        else:
            if (isinstance(self.visit(ctx.statement(0)), list)):
                return If(self.visit(ctx.exp()), Block(self.visit(ctx.statement(0))))
            else:
                return If(self.visit(ctx.exp()), self.visit(ctx.statement(0)))

    def visitFor_state(self,ctx:MCParser.For_stateContext):
        if (isinstance(self.visit(ctx.statement()), list)):
            return For(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), Block(self.visit(ctx.statement())))
        else:
            return For(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), self.visit(ctx.statement()))

    def visitBreak_state(self,ctx:MCParser.Break_stateContext):
        return Break()

    def visitContinue_state(self,ctx:MCParser.Continue_stateContext):
        return Continue() 

    def visitReturn_state(self,ctx:MCParser.Return_stateContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

    # Expressions -----------------------------------------------
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.exp():
            return BinaryOp(ctx.ASSIGN().getText(),self.visit(ctx.exp_1()), self.visit(ctx.exp()))  
        else:
            return self.visit(ctx.exp_1())

    def visitExp_1(self,ctx:MCParser.Exp_1Context):
        if ctx.exp_1():
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp_1()), self.visit(ctx.exp_2()))  
        else:
            return self.visit(ctx.exp_2())

    def visitExp_2(self,ctx:MCParser.Exp_2Context):
        if ctx.exp_2():
            return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp_2()), self.visit(ctx.exp_3()))  
        else:
            return self.visit(ctx.exp_3())

    def visitExp_3(self,ctx:MCParser.Exp_3Context):
        if ctx.exp_3():
            if ctx.EQUAL():
                return BinaryOp(ctx.EQUAL().getText(),self.visit(ctx.exp_3(0)), self.visit(ctx.exp_3(1)))  
            else:
                return BinaryOp(ctx.NOT_EQUAL().getText(),self.visit(ctx.exp_3(0)), self.visit(ctx.exp_3(1)))
        else:
            return self.visit(ctx.exp_4())

    def visitExp_4(self,ctx:MCParser.Exp_4Context):
        if ctx.exp_4():
            if ctx.LESS_THAN():
                return BinaryOp(ctx.LESS_THAN().getText(),self.visit(ctx.exp_4(0)), self.visit(ctx.exp_4(1)))
            elif ctx.LESS_EQ():
                return BinaryOp(ctx.LESS_EQ().getText(),self.visit(ctx.exp_4(0)), self.visit(ctx.exp_4(1)))
            elif ctx.GREAT_THAN():
                return BinaryOp(ctx.GREAT_THAN().getText(),self.visit(ctx.exp_4(0)), self.visit(ctx.exp_4(1)))
            else:
                return BinaryOp(ctx.GREAT_EQ().getText(),self.visit(ctx.exp_4(0)), self.visit(ctx.exp_4(1)))               
        else:
            return self.visit(ctx.exp_5())

    def visitExp_5(self,ctx:MCParser.Exp_5Context):
        if ctx.exp_5():
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp_5()), self.visit(ctx.exp_6()))  
            else:
                return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp_5()), self.visit(ctx.exp_6()))
        else:
            return self.visit(ctx.exp_6())

    def visitExp_6(self,ctx:MCParser.Exp_6Context):
        if ctx.exp_6():
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp_6()), self.visit(ctx.exp_7()))
            elif ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp_6()), self.visit(ctx.exp_7()))
            else:
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp_6()), self.visit(ctx.exp_7()))
        else:
            return self.visit(ctx.exp_7())

    def visitExp_7(self,ctx:MCParser.Exp_7Context):
        if ctx.exp_7():
            if ctx.NOT():
                return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp_7()))  
            else:
                return UnaryOp(ctx.SUB().getText(),self.visit(ctx.exp_7()))
        else:
            return self.visit(ctx.exp_8())

    def visitExp_8(self,ctx:MCParser.Exp_8Context):
        if ctx.exp_5():
            return ArrayCell(self.visit(ctx.exp_9()),self.visit(ctx.exp_5()))  
        else:
            return self.visit(ctx.exp_9())

    def visitExp_9(self,ctx:MCParser.Exp_9Context):
        if ctx.LB():
            return self.visit(ctx.exp_1())  
        else:
            return self.visit(ctx.exp_0())
            
    def visitExp_0(self,ctx:MCParser.Exp_0Context):
        if ctx.primid_lit():
            return self.visit(ctx.primid_lit())  
        else:
            if ctx.exp():
                return CallExpr(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.exp()])  
            else:
                return CallExpr(Id(ctx.ID().getText()),[])
    
    def visitPrimid_lit(self,ctx:MCParser.Primid_litContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.FLOATLIT():
            return FloatLiteral(ctx.FLOATLIT().getText())
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText())
        else:
            return Id(str(ctx.ID()))