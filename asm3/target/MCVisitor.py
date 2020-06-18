# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decls.
    def visitDecls(self, ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#one_decl.
    def visitOne_decl(self, ctx:MCParser.One_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_decl.
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#prim_type.
    def visitPrim_type(self, ctx:MCParser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#id_list.
    def visitId_list(self, ctx:MCParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_list.
    def visitPara_list(self, ctx:MCParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#re_para.
    def visitRe_para(self, ctx:MCParser.Re_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_decl.
    def visitPara_decl(self, ctx:MCParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_state.
    def visitBlock_state(self, ctx:MCParser.Block_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_state.
    def visitDo_while_state(self, ctx:MCParser.Do_while_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_state.
    def visitIf_state(self, ctx:MCParser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_state.
    def visitFor_state(self, ctx:MCParser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_state.
    def visitBreak_state(self, ctx:MCParser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_state.
    def visitContinue_state(self, ctx:MCParser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_state.
    def visitReturn_state(self, ctx:MCParser.Return_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp.
    def visitExp(self, ctx:MCParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_1.
    def visitExp_1(self, ctx:MCParser.Exp_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_2.
    def visitExp_2(self, ctx:MCParser.Exp_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_3.
    def visitExp_3(self, ctx:MCParser.Exp_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_4.
    def visitExp_4(self, ctx:MCParser.Exp_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_5.
    def visitExp_5(self, ctx:MCParser.Exp_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_6.
    def visitExp_6(self, ctx:MCParser.Exp_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_7.
    def visitExp_7(self, ctx:MCParser.Exp_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_8.
    def visitExp_8(self, ctx:MCParser.Exp_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_9.
    def visitExp_9(self, ctx:MCParser.Exp_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp_0.
    def visitExp_0(self, ctx:MCParser.Exp_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primid_lit.
    def visitPrimid_lit(self, ctx:MCParser.Primid_litContext):
        return self.visitChildren(ctx)



del MCParser