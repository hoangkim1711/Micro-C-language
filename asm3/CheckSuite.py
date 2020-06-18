#
#   @author nhphung
#

import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

#2.1 Redeclared Variable/Function/Parameter:_______________________________
###########################################################################
###########################################################################
###########################################################################

    #Redeclared Variable

    def test_redeclare_variable_global(self):
        input = """
            int a;
            float a;
            void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclare_variable_para(self):
        input = """
            void func(){ return ;}
            void main(int a, float b){
                string b;
            }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclare_variable_block(self):
        input = """
            void func(int numint, float numfloat){
                int c;
                float c; 
            }
            void main(){
                func(1, 2.1);
            }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclare_variable_block_and_para(self):
        input = """
        int func(int d){
            int d;
            d = 2;
            return d*d;
        }
        void main(){
            func(1);
        }
        """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    #Redeclared Function

    def test_redeclare_function(self):
        input = """
            void func() {}

            void main(){
                func();
            }

            void func(){}
        """
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclare_arr_function(self):
        input = """int[] func(){}
        int[] func(){}
        """
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclare_function_and_variable(self):
        input = """
        int var;
        void func(){}
        void var(){}
        void main(){}
        """
        expect = "Redeclared Function: var"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclare_array_function(self):
        input = """float[] func(){}
        string[] func(){}
        """
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_redeclare_func_and_var(self):
        input = """
        int a;
        void a(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 476))

    #Redeclared Parameter

    def test_redeclare_parameter_basic(self):
        input = """
            void main(){a(1,2);}
            int a(int a, float a){}
            """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclare_parameter(self):
        input = """
            int a;
            int func(float b, string b){
                return a;
            }
            void main(){
                func(a,"Hello");
            }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_redeclare_parameter_simple(self):
        input = """
        int func(int c, int c){
            return 1;
        }
        void main(){
        }
        """
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclare_parameter_in_function(self):
        input = """
            int func(float b, string b){
                return 1;
            }
            void main(){
                func(1.1,"Hi");
            }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 477))


#2.2 Undeclared Identifier/Function:_______________________________________
###########################################################################
###########################################################################
###########################################################################

    #Undeclared Identifier

    def test_undeclared_indentifier_in_function(self):
        input = """
        void func(int a){
            int b;
            a;
            c;
        }
        void main() {
               func(1);
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_undeclared_indentifier_simple(self):
        input = """
        int a[10],c;
        int func(int size, int arr[]){
            int number;
            b;
        }
        void main(){
            int a[1];
            func(10,a);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undeclared_indentifier_assign(self):
        input = """
        int a[10],c;
        int func(int size, int arr[]){
            int iNum;
            a[1]=number;
        }
        void main(){
            int a[1];
            func(10,a);   
        }
        """

        expect = "Undeclared Identifier: number"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared_indentifier_in_if_state(self):
        input = """
        int a[10],c;
        int func(int size, int arr[]){
            int iNum;
            if(true){
                h = 1;
            }
        }
        void main(){
            int a[1];
            func(10,a);
        }
        """
        expect = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_undeclared_indentifier_in_for_state(self):
        input = """
        int func(){
            for(i; i < 10; i = i + 1){ }
            return 1;
        }
        void main(){
            func();
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_undeclared_indentifier_in_func(self):
        input = """
        void func(){
            int b;
            b = c;
        }
        void main() {
               func();
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_undeclared_indentifier_in_if(self):
        input = """
        int a[10],c;
        int func(int size, int arr[]){
            if(true){
                h = 1;
            }
        }
        void main(){
            int a[1];
            func(10,a);
        }
        """
        expect = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_undeclared_indentifier_in_for(self):
        input = """
        int func(){
            for(k; k < 10; k = k + 2){ }
            return 1;
        }
        void main(){
            func();
        }
        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 480))

    #Undeclared Function

    def test_undeclared_function(self):
        input = """
        int main() {
            func();
        }
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_function_simple(self):
        input = """
        void main () {
            writeInt(3);      
        }    
        """
        expect = "Undeclared Function: writeInt"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_function_basic(self):
        input = """
        int a[10],c;
        int m(int size, int arr[]){
            func();
        }
        void main(){
            int a[1];
            m(10,a);
        }
        """
        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,417))


    def test_undeclared_function_in_if_state(self):
        input = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if(true){
                size = i;
            }
            else{
                func(10);
            }
        }
        """

        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_function_in_do_while(self):
        input = """
        int a[10],c;
        void main(){
            int size;
            int i;
            do{
                func();
            }
            while(true);
        }
        """

        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,419))

#2.3 Type Mismatch In Statement:___________________________________________
###########################################################################
###########################################################################
###########################################################################

    #if

    def test_type_mismatch_in_if_state(self):
        input = """
            void main(){
                int a;
                float b;
                if(a == 0){
                    b = b + 1;
                }
                if(b) break;
            }
        """
        expect = "Type Mismatch In Statement: If(Id(b),Break())"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_type_mismatch_in_if_else_state(self):
        input = """
            void main(){
                int a;
                float b;
                boolean c;
                if(c)
                    b + 1;
                else
                    a + 2;
                if(b)
                    b + 3;
                else
                    b + 4;
            }
        """
        expect = "Type Mismatch In Statement: If(Id(b),BinaryOp(+,Id(b),IntLiteral(3)),BinaryOp(+,Id(b),IntLiteral(4)))"
        self.assertTrue(TestChecker.test(input, expect, 421))       
    
    #for

    def test_mismatch_in_for_state(self):
        input = """
            int a;
            float b;
            void main(){
                int c;
                for(a; c = a; c = c + 1){ 
                    b = b + 1;
               }
            }
        """
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(=,Id(c),Id(a));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_type_mismatch_in_for_state_level_2(self):
        input = """int main() {
            int a,b,c,e;
            e = 9;
            for(a=1;a<=5;a=a+1)
             {
                for(b=0; b ;b= b+1)
                {
                    putIntLn(b);
                }
                putIntLn(a);
                e=e-2;
             }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(b),IntLiteral(0));Id(b);BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([CallExpr(Id(putIntLn),[Id(b)])]))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    #do while

    def test_mismatch_type_in_do_while_state(self):
        input = """
            void main(){
                int a;
                float b;
                do
                    b+1;
                while(a);
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(+,Id(b),IntLiteral(1))],Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_type_mismatch_in_do_while_simple(self):
        input = """
            int main() {
                int i;
                int n;
                do{
                    n = n - 1;
                    i = i+1;
                    if( i ==n )
                        return i;
                    else
                        break;
                }
                while(i + n); 
                }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(n),BinaryOp(-,Id(n),IntLiteral(1))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(==,Id(i),Id(n)),Return(Id(i)),Break())])],BinaryOp(+,Id(i),Id(n)))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_type_mismatch_in_do_while_in_for_in_if(self):
        input = """
            void main(){
                if(true){
                    int i;
                    for(i = 0; i < 10; i = i +1){
                        do{
                            int e;
                            i + 2;
                        } while(i);
                    }
                }
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(e,IntType),BinaryOp(+,Id(i),IntLiteral(2))])],Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 426))

    #return

    def test_return_state_wrong_type(self):
        input = """
            int func(int a, float b){
                return b;
            }
            void main(){}
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_return_state_wrong_arr_type(self):
        input = """
            int[] func(){
                float b[5];
                return b;
            }
            void main(){
                func();
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 428))
  
    def test_return_state_wrong_type_in_if(self):
        input = """
            int func(){
                boolean a;
                if(a){
                    return 1;
                }
                else{
                    float c;
                    c = 2.1;
                    return c;
                }
            }
            void main(){
                func();
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 429))

#2.4 Type Mismatch In Expression:__________________________________________
###########################################################################
###########################################################################
###########################################################################

    def test_diff_numofparam_expr(self):
        input = """int main () {
            putIntLn(getInt(4.1));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[FloatLiteral(4.1)])"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_in_expression_arrcell(self):
        input = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[fNum];
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("fNum")))
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_type_mismatch_in_expression_array(self):
        input = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[isTrue];
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("isTrue")))
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_mismatch_in_expression_4(self):
        input = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr["isTrue"];
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),StringLiteral("isTrue")))
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_mismatch_in_expression_5(self):
        input =  """
        int a[10],b,arr;
        void main(){
            int iNum;
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = isTrue;
        }
        """
        expect = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("fNum"),Id("isTrue")))
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_mismatch_in_expression_6(self):
        input = """
        int a[10],c;
        int[] func(){
            int a[10];
            return a;
        }
        void main(){
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[func()];
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),CallExpr(Id("func"),[])))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_mismatch_in_expression_7(self):
        input = """
        int a[10];
        void main(){
            int a;
            a[10];
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_mismatch_in_expression_8(self):
        input = """
        int a[10],c;
        int[] func(){
            int a[10];
            return a;
        }
        void main(){
            string a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            func();
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_mismatch_in_expression_9(self):
        input = """
        int a[10],c;
        int[] func(){
            int a[10];
            return a;
        }
        void main(){
            float a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            a[10];
            func();
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_mismatch_in_expression_arr_2(self):
        input = """
        int a[10],c;
        int[] func(){
            int a[10];
            return a;
        }
        void main(){
            boolean a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            func();
        }
        """
        expect = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(input,expect,439))

#2.5 Function not return:______________________________________________440_
###########################################################################
###########################################################################
###########################################################################

    def test_function_not_return_1(self):
        input = """
        void main(){ func(1,1); }
        int func(int a,float b){
            if(true){ } 
            else {
                return 2;
            } 
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_function_not_return_2(self):
        input = """
        void main(){ func(); }
        int func(){
            int x;
            do
                x=0;
            while(true);
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_function_not_return_3(self):
        input = """
        void main(){ func(); }
        int func(){
            if(true) return 1;
        }"""
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_function_not_return_4(self):
        input =  """
        void main(){ func(2); }
        int func(int a){
            a = 1;
        }
        """  
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_function_not_return_5(self):
        input = """
        string getString(){return "Abc";}
        void func(){ }
        void main(){
            func();
            getString();
            haha();
        }
        boolean haha(){ }
        """
        expect = "Function haha Not Return "
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_function_not_return_6(self):
        input = """
        void main(){ func(); }
        int func(){
            int x;
            x = x * x;
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,481))

#2.6 Break/Continue not in loop:_______________________________________445_
###########################################################################
###########################################################################
###########################################################################

    #break

    def test_break_not_in_loop_1(self):
        input = """
        void main(){
            func();
        }
        void func(){
            do{
                2;
            } while (true);
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_break_not_in_loop_2(self):
        input = """
        void main(){
            for(1;true;1) 1;
            break;
            return;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_break_not_in_loop_3(self):
        input = """
            void main(){
                break;   
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_break_not_in_loop_4(self):
        input = """
            void main(){
                int a;
                for( a = 0 ; a < 10; a = a+1){
                    if(a == 5){
                        break;
                    }
                }
                if(a == 5){
                        break;
                }
                return;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_break_not_in_loop_5(self):
        input = """
             void main(){
                {
                    {
                        break;
                    }
                }
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 449))

    #continue

    def test_continue_not_in_loop_1(self):
        input = """
        void main(){
            for(1;true;1){if(true) continue;}
            if(true) { 
                for(1;true;1){ 
                    if(true) break; 
                } 
                continue;
            } 
            else { }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_continue_not_in_loop_2(self):
        input = """
        void main() {
            int i;
            for (i; i < 5; i = i + 2) {
              i = i + 1;
            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_continue_not_in_loop_3(self):
        input = """
        void main(){
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_continue_not_in_loop_4(self):
        input = """
        void main(){
            if(true) { 
                for(1;true;1) { continue; } 
                if(false) { continue;} 
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_continue_not_in_loop_5(self):
        input = """
        void main(){
            for(1;true;1) { 
                if(true) continue; 
            }
            do 
                if(true) continue; 
                else { continue;} 
            while(true);
            if(false) {} 
            else continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,454))


#2.7 No Entry Point:___________________________________________________455_
###########################################################################
###########################################################################
###########################################################################

    def test_no_entry_point_1(self):
        input = """
            void func() {}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_no_entry_point_2(self):
        input = """int main;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_no_entry_point_3(self):
        input = """
        int mn(){
            int i; 
            if(i==5) return 1; 
            else return 1; 
            i=1+i;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_no_entry_point_4(self):
        input = "float min(int a){ }"
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_no_entry_point_5(self):
        input = "boolean man(int a, int b){ int c; man();}"
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,459))

#2.8 Unreachable function:_____________________________________________460_
###########################################################################
###########################################################################
###########################################################################

    def test_unreachable_function_1(self):
        input = """
            void func(int a, float b){
            }
            void main(){
            }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_unreachable_function_more(self):
        input = """
            void func22(){}
            void func(){
                func22();
            }
            void goo(int a, float b){
                func();
            }
            void main(){
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_unreachable_function_139(self):
        input = """
        void func(){ }
        void main(){ }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_unreachable_function_140(self):
        input = """
        void func(){
            func();
        }
        void main(){ }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_unreachable_function_1141(self):
        input = """
        void func(){
            func();
        }
        void func1(){
            func();
        }
        void main(){ }
        """
        expect = "Unreachable Function: func1"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_unreachable_function_141(self):
        input = """
        void func(){
            func1();
        }
        void func1(){
            func();
        }
        void func2(){
            func();
            func1();
        }
        void main(){ }
        """
        expect = "Unreachable Function: func2"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_unreachable_function_234124(self):
        input = """
            void func(int a, float b){ 
            }
            void main(){
            }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_unreachable_function_q123(self):
        input = """
            void func22(){}
            void func(){
                func22();
            }
            void goo(int a, float b){ 
                func();
            }
            void main(){
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_unreachable_function_rec(self):
        input = """
               void func(int a, float b){ 
                   func(a,b);
               }
               void main(){
               }
           """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_unreachable_function_12442(self):
        input = """
            void func1(){}
            void func22(){}
            void func(){
                {
                    func1();
                }
            }
            void goo(int a, float b){
                func22();
                {
                        func();
                }
            }
            void main(){
                func1();
                if(true){
                    func();
                }
                else
                    func22();
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 469))


#2.9 Not Left Value:___________________________________________________470_
###########################################################################
###########################################################################
###########################################################################

    def test_not_left_value_1(self):
        """
        void main(){
            1 + 2 = 3;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),Return()]))]))
        expect = "Not Left Value: BinaryOp(+,IntLiteral(1),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_not_left_value_2(self):
        input = """
            void main(){
                float ace;
                ace = -1.5234;
                -ace = 1.5234;
            }
        """
        expect = "Not Left Value: UnaryOp(-,Id(ace))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_not_left_value_3(self):
        input = """
            int func(int a){
                return a*a;
            }
            void main(){
                int c, d[5];
                c = func(10);
                d[4] = func(5);
                func(8) = c; 
            }
        """
        expect = "Not Left Value: CallExpr(Id(func),[IntLiteral(8)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_not_left_value_4(self):
        input = """
            int[] func(){
                int a[5];
                return a;
            }
            void main(){
                int a;
                a = 1+ 2 * 4 / 3 % 5;
                (a) = 3;
                func()[4] = 2;
                (func()[4] -a) = 1; 
            }
        """
        expect = "Not Left Value: BinaryOp(-,ArrayCell(CallExpr(Id(func),[]),IntLiteral(4)),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_not_left_value_5(self):
        """
        void main(){
            int a;
            a + 1 = a;
            return;
        }
        """
        input = (Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),Id("a")),Return()]))]))
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,474))

#2.10 Unreachable statement:___________________________________________4_
###########################################################################
###########################################################################
###########################################################################


#2.11 Index expect of range:___________________________________________475_
###########################################################################
###########################################################################
###########################################################################

#2.12 Uninitialized Variable:__________________________________________4_
###########################################################################
###########################################################################
###########################################################################

    def test_total_program_1(self):
        input = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            func(1,2,"hihi");
        }
        int func(int a, int b, string str){
            int ar, br;
        }
        float numberOne;
        void func(int a, int c){
        }"""
        expect = "Redeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_total_program_2(self):
        input = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            func(1,2,"a");
        }
        int func(int a, int b, string str){
            int ar, br;
            {
                int a;
                {
                    int abc;
                    int abc;
                }
            }
        }
        float numberOne;"""
        expect = "Redeclared Variable: abc"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_total_program_3(self):
        input = """
        int a[10],c;
        int func(int size, int arr[]){
            int number;
            b;
        }
        void main(){
            int a[1];
            func(10,a);
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_total_program_4(self):
        input = """
        void main(){
            for(1;true;1) { 
                do if(true) break; else {continue;} while(true); if(true) continue; }
                do if(true) continue; else {continue;} while(true);
                if(false) { } 
                else { { 
                    { 
                        { 
                            { int a; continue; } 
                        } 
                    } 
                } 
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_total_program_5(self):
        input = """
         void main(){
          do if(true) break; else {continue;} while(true);
          for(1;true;1) { if(true) continue; }
          do if(false) break; else {} while(true);
          continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_total_program_6(self):
        input = """
        void main(){ func(1); }
        int func(int a){ }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_total_program_7(self):
        input = """
        void main(){ func(1,1); }
        int func(int a,float b){
            if(true){ } 
            else {
                return 2;
            } 
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,488))


    def test_total_program_8(self):
        input = """
        void main(){ func(); }
        int func(){
            if(true) 1; 
            else 1;
        }"""
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_total_program_9(self):
        input = """
            void func(){ return ;}
            void main(int a, float b){
                string b;
            }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_total_program_10(self):
        input = """
            void func(int numint, float numfloat){
                int c;
                float c; 
            }
            void main(){
                func(1, 2.1);
            }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_total_program_11(self):
        input = """
        int func(int d){
            int d;
            d = 2;
            return d*d;
        }
        void main(){
            func(1);
        }
        """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_total_program_12(self):
        input = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if(true){
                size = i;
            }
            else{
                func(10);
            }
        }
        """

        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_total_program_13(self):
        input = """
        int a[10],c;
        void main(){
            int size;
            int i;
            do{
                func();
            }
            while(true);
        }
        """

        expect = "Undeclared Function: func"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_total_program_14(self):
        input = """
            void func(int a, float b){
            }
            void main(){
            }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_total_program_15(self):
        input = """
            void func22(){}
            void func(){
                func22();
            }
            void goo(int a, float b){
                func();
            }
            void main(){
            }
        """
        expect = "Unreachable Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_total_program_16(self):
        input = """
        void func(){ }
        void main(){ }
        """
        expect = "Unreachable Function: func"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_total_program_17(self):
        input = """
        void main(){
            for(1;true;1){if(true) continue;}
            if(true) { 
                for(1;true;1){ 
                    if(true) break; 
                } 
                continue;
            } 
            else { }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_total_program_18(self):
        input = """
        void main() {
            int i;
            for (i; i < 5; i = i + 2) {
              i = i + 1;
            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,499))