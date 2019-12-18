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

    def test_put_bool_ln_assign(self):
        input = """
            void main () {
				int a;
				a = 1;
				a = a + 1;
				boolean check;
				check = false;
                putBoolLn(check);
            }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))	

    def test_simple_multiply_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(2*3);
                putFloatLn(2.5*1.2);
                putFloatLn(1.5* 10);
                }"""
        expect = """6
3.0
15.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))



    # Test simple expression not include assign
    def test_simple_add_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1+2);
                putFloatLn(1.5+2.5);
                putFloatLn(1+2.5);
                }"""
        expect = """3
4.0
3.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_simple_minus_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1-2);
                putFloatLn(2.5-1.2);
                putFloatLn(10.5-5);
                }"""
        expect = """-1
1.3
5.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))


    def test_simple_and_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true && false);
                putBoolLn(false && true && true);
                putBoolLn(false && (false && true));
                }"""
        expect = """false
false
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))




    def test_simple_or_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true || false);
                putBoolLn(false || true || true);
                putBoolLn(false || (false || true));
                }"""
        expect = """true
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_print_simple_negative_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(-1);
                putFloatLn(-1.5);
                putFloatLn(-(10+2.5));
                }"""
        expect = """-1
-1.5
-12.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))



    def test_simplecomplex_divide_expression(self):
        """Simple program: int main() {} """
        input = """
            int a;
            float b,c;
            void main() {
                a = 1;
                b= c = 1.5;
                putIntLn(100 / (10 / (1 +3)));
                putFloatLn((b* 1.5) / (20*40));
                putFloatLn((a / 2.5) /((c / 2.1) / b));
                }"""
        expect = """50
0.0028125
0.84000003
"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))



    def test_simpleassign_local_variable_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() {
                    int a;
                    a = 0;
                    putIntLn(a);
                    a =2;
                    putIntLn(a);
                    }"""
        expect = """0
2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_simplemultiple_local_variables_assign_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() {
                    int a,b,c;
                    a = b = c = 0;
                    a = a = a+1;
                    putIntLn(a);
                    putIntLn(b);
                    putIntLn(c);
                    }"""
        expect = """1
0
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    
	#Int
    def test_simpleput_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_simpleput_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_simpleput_int_ln(self):
        input = """void main() {putIntLn(99);}"""
        expect = "99\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))
	#Float
    def test_simpleput_float(self):
        """Simple program: int main() {} """
        input = """void main() {putFloat(100.001);}"""
        expect = "100.001"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_simplefloat_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloat"),[FloatLiteral(5.1)])]))])
    	expect = "5.1"
    	self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_simplefloat_ln_ast_more(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloatLn"),[FloatLiteral(5.1)])]))])
    	expect = "5.1\n"
    	self.assertTrue(TestCodeGen.test(input,expect,525))
    #String
    def test_simplestring_ast_more(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putString"),[StringLiteral('PPL')])]))])
    	expect = "PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_simplestring_ln_more(self):
        input = """
            void main () {
                putStringLn("ppl");
            }"""
        expect = "ppl\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))	
	#Bool
    def test_simpleput_bool_more(self):
        input = """
            void main () {
                putBool(false);
            }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,528))	
    def test_simpleput_bool_ln_more(self):
        input = """
            void main () {
                putBoolLn(true);
            }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))	

    def test_simpleput_bool_ln_assign_more(self):
        input = """
            void main () {
				int a;
				a = 1;
				a = a + 1;
				boolean check;
				check = false;
                putBoolLn(check);
            }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))	

    def test_simplesimple_multiply_expression_more(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(2*3);
                putFloatLn(2.5*1.2);
                putFloatLn(1.5* 10);
                }"""
        expect = """6
3.0
15.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_simplesimple_divide_expression_more(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(3/2);
                putFloatLn(3.6/1.2);
                putFloatLn(6.4/4);
                }"""
        expect = """1
2.9999998
1.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_simpleprint_float_more(self):
        """Simple program: int main() {} """
        input = """void main() {
                        putFloat(7.7);
                    }"""
        expect = "7.7"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_simplemultiple_local_variables_assign_statement_different_type(self):
        """Simple program: int main() {} """
        input = """
                    void main() {
                        int a;
                        float b;
                        string c;
                        boolean d;
                        a =10;
                        b =6.9;
                        c = "Hello world";
                        d = true;
                        putIntLn(a);
                        putFloatLn(b);
                        putStringLn(c);
                        putBoolLn(d);
                        }"""
        expect = """10
6.9
Hello world
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    # statement
    def test_simplesimple_block_statement(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    a = 10;
                    putIntLn(a);
                }
                putIntLn(a);
                }"""
        expect = """10
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_simpleinitial_variable_inside_block(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    int a;
                    a = 2;
                    putIntLn(a);
                }
                putIntLn(a);
            }"""
        expect = """2
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_simple_divide_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(3/2);
                putFloatLn(3.6/1.2);
                putFloatLn(6.4/4);
                }"""
        expect = """1
2.9999998
1.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_simple_assign_global_variable(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a =1;
                putInt(a);
                }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_simple_assign_local__variable(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                int a;
                a = 1;
                putInt(a);
                }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_simple_assign_multiple_variables(self):
        """Simple program: int main() {} """
        input = """
            int a;
            boolean b;
            string c;
            float d;
            void main() {
                a =1;
                b = true;
                c = "Hello world";
                d = 1.2;
                putIntLn(a);
                putBoolLn(b);
                putStringLn(c);
                putFloatLn(d);
                }"""
        expect = """1
true
Hello world
1.2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_simple_assign_multiple_variables_in_1_line(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 1;
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
                }"""
        expect = """1
1
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))



        

    def test_complex_add_expression(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 1;
                putIntLn(a +10 +(b + 20));
                putIntLn(b + (a +(a - b)));
                putIntLn((c+ (a + b)) + c);
                }"""
        expect = """32
2
4
"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_complex_minus_expression(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 69;
                putIntLn(a - b - (c-10));
                putFloatLn(b - (a -( c- a - 100.1)));
                putFloatLn((a - 2.5)- (c - 212.1) - b);
                }"""
        expect = """-59
-100.100006
140.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_complex_multiple_expression(self):
        """Simple program: int main() {} """
        input = """
            int a;
            float b,c;
            void main() {
                a = 1;
                b= c = 1.5;
                putIntLn(a* (10 * (1 +3)));
                putFloatLn((b* 1.5) * (20*40));
                putFloatLn((a * 2.5) * (c - 2.1) * b);
                }"""
        expect = """40
1800.0
-2.2499995
"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_complex_divide_expression(self):
        """Simple program: int main() {} """
        input = """
            int a;
            float b,c;
            void main() {
                a = 1;
                b= c = 1.5;
                putIntLn(100 / (10 / (1 +3)));
                putFloatLn((b* 1.5) / (20*40));
                putFloatLn((a / 2.5) /((c / 2.1) / b));
                }"""
        expect = """50
0.0028125
0.84000003
"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))



    def test_assign_local_variable_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() {
                    int a;
                    a = 0;
                    putIntLn(a);
                    a =2;
                    putIntLn(a);
                    }"""
        expect = """0
2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_multiple_local_variables_assign_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() {
                    int a,b,c;
                    a = b = c = 0;
                    a = a = a+1;
                    putIntLn(a);
                    putIntLn(b);
                    putIntLn(c);
                    }"""
        expect = """1
0
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_multiple_local_variables_assign_statement_different_type(self):
        """Simple program: int main() {} """
        input = """
                    void main() {
                        int a;
                        float b;
                        string c;
                        boolean d;
                        a =10;
                        b =6.9;
                        c = "Hello world";
                        d = true;
                        putIntLn(a);
                        putFloatLn(b);
                        putStringLn(c);
                        putBoolLn(d);
                        }"""
        expect = """10
6.9
Hello world
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    # statement
    def test_simple_block_statement(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    a = 10;
                    putIntLn(a);
                }
                putIntLn(a);
                }"""
        expect = """10
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_initial_variable_inside_block(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    int a;
                    a = 2;
                    putIntLn(a);
                }
                putIntLn(a);
            }"""
        expect = """2
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_initial_variable_in_2_blocks(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
               a = 0;
               {
                    int a;
                    a = 6;
                    putIntLn(a);
                }
                {
                    float a;
                    a = 1;
                    putFloatLn(a);
                }
            }"""
        expect = """6
1.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))


    def test_block_statement_inside_block_statement_with_global_variable(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    a = 2;
                    putIntLn(a);
                    {
                        a =3;
                        putIntLn(a);
                    }
                }
                putIntLn(a);
            }"""
        expect = """2
3
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_block_statement_inside_block_statement_with_local_variable(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                int a;
                a = 0;
                {
                    a = 2;
                    putIntLn(a);
                    {
                        a =3;
                        putIntLn(a);
                    }
                }
                putIntLn(a);
            }"""
        expect = """2
3
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_complex_block_statement(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                int a;
                  a = 0;
                  {
                      a = 2;
                      putIntLn(a);
                      {
                          a =3;
                          {
                           a =4;
                          }
                          putIntLn(a);
                      }

                      {
                        a =1;
                      }
                  }
                  putIntLn(a);
            }"""
        expect = """2
4
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))



	#Int
    def test_simple_put_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_simple_put_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_simple_put_int_ln(self):
        input = """void main() {putIntLn(99);}"""
        expect = "99\n"
        self.assertTrue(TestCodeGen.test(input,expect,557))
	#Float
    def test_simple_put_float(self):
        """Simple program: int main() {} """
        input = """void main() {putFloat(100.001);}"""
        expect = "100.001"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_simple_float_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloat"),[FloatLiteral(5.1)])]))])
    	expect = "5.1"
    	self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_simplefloat_ln_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putFloatLn"),[FloatLiteral(5.1)])]))])
    	expect = "5.1\n"
    	self.assertTrue(TestCodeGen.test(input,expect,560))
    #String
    def test_simplestring_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putString"),[StringLiteral('PPL')])]))])
    	expect = "PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_simplestring_ln(self):
        input = """
            void main () {
                putStringLn("ppl");
            }"""
        expect = "ppl\n"
        self.assertTrue(TestCodeGen.test(input,expect,562))	
	#Bool
    def test_simpleput_bool(self):
        input = """
            void main () {
                putBool(false);
            }"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,563))	
    def test_simpleput_bool_ln(self):
        input = """
            void main () {
                putBoolLn(true);
            }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,564))	

    def test_simpleput_bool_ln_assign(self):
        input = """
            void main () {
				int a;
				a = 1;
				a = a + 1;
				boolean check;
				check = false;
                putBoolLn(check);
            }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,565))	

    def test_simplesimple_multiply_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(2*3);
                putFloatLn(2.5*1.2);
                putFloatLn(1.5* 10);
                }"""
        expect = """6
3.0
15.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_simplesimple_divide_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(3/2);
                putFloatLn(3.6/1.2);
                putFloatLn(6.4/4);
                }"""
        expect = """1
2.9999998
1.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_simpleprint_float(self):
        """Simple program: int main() {} """
        input = """void main() {
                        putFloat(7.7);
                    }"""
        expect = "7.7"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_simpleprint_string(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putString("Hello world");
                }"""
        expect = "Hello world"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_simpleprint_boolean(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBool(true);
                }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_simpleputIntLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1);
                }"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_simpleputFloatLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putFloatLn(10.0);
                }"""
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_simpleputBoolLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true);
                }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_simpleputStringLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putStringLn("Hello world!");
                }"""
        expect = "Hello world!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_simpleputLn(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBool(true);
                putLn();
                putInt(1);
                }"""
        expect = "true\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    # Test simple expression not include assign
    def test_simplesimple_add_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1+2);
                putFloatLn(1.5+2.5);
                putFloatLn(1+2.5);
                }"""
        expect = """3
4.0
3.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_simplesimple_minus_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1-2);
                putFloatLn(2.5-1.2);
                putFloatLn(10.5-5);
                }"""
        expect = """-1
1.3
5.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))


    def test_simplesimple_and_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true && false);
                putBoolLn(false && true && true);
                putBoolLn(false && (false && true));
                }"""
        expect = """false
false
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))




    def test_simplesimple_or_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true || false);
                putBoolLn(false || true || true);
                putBoolLn(false || (false || true));
                }"""
        expect = """true
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_simpleprint_simple_negative_expression(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(-1);
                putFloatLn(-1.5);
                putFloatLn(-(10+2.5));
                }"""
        expect = """-1
-1.5
-12.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 580))



    def test_simplesimple_assign_global_variable(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a =1;
                putInt(a);
                }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_simplesimple_assign_local__variable(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                int a;
                a = 1;
                putInt(a);
                }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_simplesimple_assign_multiple_variables(self):
        """Simple program: int main() {} """
        input = """
            int a;
            boolean b;
            string c;
            float d;
            void main() {
                a =1;
                b = true;
                c = "Hello world";
                d = 1.2;
                putIntLn(a);
                putBoolLn(b);
                putStringLn(c);
                putFloatLn(d);
                }"""
        expect = """1
true
Hello world
1.2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_simplesimple_assign_multiple_variables_in_1_line(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 1;
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
                }"""
        expect = """1
1
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 584))



        

    def test_simplecomplex_add_expression(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 1;
                putIntLn(a +10 +(b + 20));
                putIntLn(b + (a +(a - b)));
                putIntLn((c+ (a + b)) + c);
                }"""
        expect = """32
2
4
"""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_simplecomplex_minus_expression(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                a = b= c = 69;
                putIntLn(a - b - (c-10));
                putFloatLn(b - (a -( c- a - 100.1)));
                putFloatLn((a - 2.5)- (c - 212.1) - b);
                }"""
        expect = """-59
-100.100006
140.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_simplecomplex_multiple_expression(self):
        """Simple program: int main() {} """
        input = """
            int a;
            float b,c;
            void main() {
                a = 1;
                b= c = 1.5;
                putIntLn(a* (10 * (1 +3)));
                putFloatLn((b* 1.5) * (20*40));
                putFloatLn((a * 2.5) * (c - 2.1) * b);
                }"""
        expect = """40
1800.0
-2.2499995
"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))



    def test_print_float(self):
        """Simple program: int main() {} """
        input = """void main() {
                        putFloat(7.7);
                    }"""
        expect = "7.7"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_print_string(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putString("Hello world");
                }"""
        expect = "Hello world"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_print_boolean(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBool(true);
                }"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_putIntLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putIntLn(1);
                }"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_putFloatLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putFloatLn(10.0);
                }"""
        expect = "10.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_putBoolLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBoolLn(true);
                }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_putStringLn_function(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putStringLn("Hello world!");
                }"""
        expect = "Hello world!\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_putLn(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                putBool(true);
                putLn();
                putInt(1);
                }"""
        expect = "true\n1"
        self.assertTrue(TestCodeGen.test(input, expect, 595))


    def test_simpleinitial_variable_in_2_blocks(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
               a = 0;
               {
                    int a;
                    a = 6;
                    putIntLn(a);
                }
                {
                    float a;
                    a = 1;
                    putFloatLn(a);
                }
            }"""
        expect = """6
1.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))


    def test_simpleblock_statement_inside_block_statement_with_global_variable(self):
        """Simple program: int main() {} """
        input = """
            int a;
            void main() {
                a = 0;
                {
                    a = 2;
                    putIntLn(a);
                    {
                        a =3;
                        putIntLn(a);
                    }
                }
                putIntLn(a);
            }"""
        expect = """2
3
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_simpleblock_statement_inside_block_statement_with_local_variable(self):
        """Simple program: int main() {} """
        input = """
            void main() {
                int a;
                a = 0;
                {
                    a = 2;
                    putIntLn(a);
                    {
                        a =3;
                        putIntLn(a);
                    }
                }
                putIntLn(a);
            }"""
        expect = """2
3
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_simplecomplex_block_statement(self):
        """Simple program: int main() {} """
        input = """
            int a,b,c;
            void main() {
                int a;
                  a = 0;
                  {
                      a = 2;
                      putIntLn(a);
                      {
                          a =3;
                          {
                           a =4;
                          }
                          putIntLn(a);
                      }

                      {
                        a =1;
                      }
                  }
                  putIntLn(a);
            }"""
        expect = """2
4
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))
