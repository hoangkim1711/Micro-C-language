import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
	#Int
    def test_put_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_put_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_put_int_ln(self):
        input = """void main() {putIntLn(99);}"""
        expect = "99\n"
        self.assertTrue(TestCodeGen.test(input,expect,502))
	#Float
    def test_put_float(self):
        """Simple program: int main() {} """
        input = """void main() {putFloat(100.001);}"""
        expect = "100.001"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_float_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloat"),[FloatLiteral(5.1)])]))])
    	expect = "5.1"
    	self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_float_ln_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloatLn"),[FloatLiteral(5.1)])]))])
    	expect = "5.1\n"
    	self.assertTrue(TestCodeGen.test(input,expect,505))
    #String
    def test_string_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putString"),[StringLiteral('PPL')])]))])
    	expect = "PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_string_ln(self):
        input = """
            void main () {
                putStringLn("ppl");
            }"""
        expect = "ppl\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))	
	#Bool
    def test_put_bool(self):
        input = """
            void main () {
                putBool(false);
            }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,508))	
    def test_put_bool_ln(self):
        input = """
            void main () {
                putBoolLn(true);
            }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))	

    # def test_put_bool_ln_assign(self):
    #     input = """
    #         void main () {
	# 			int a;
	# 			a = 1;
	# 			a = a + 1;
	# 			boolean check;
	# 			check = false;
    #             putBoolLn(check);
    #         }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))	

