import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_func_decl_1(self):
        input = """
        
            void main () {
				boolean check;
				check = false;
                putBoolLn(check);
            }

            
        """
        expect = str(Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(check,BoolType),BinaryOp(=,Id(check),BooleanLiteral(false)),CallExpr(Id(putBoolLn),[Id(check)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))


#     def test_func_decl_1(self):
#         input = """int mc_function() {}"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,300))

#     def test_func_decl_2(self):
#         input = """int mc_function() {
#             a = 1 + 1;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(1)))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,301))

#     def test_func_decl_3(self):
#         input = """int main(string str) {}"""
#         expect = str(Program([FuncDecl(Id("main"),[VarDecl("str",StringType())],IntType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,302))

#     def test_func_decl_4(self):
#         input = """int main() {
#             a = a + 1;
#             print("Hello word!");
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),CallExpr(Id("print"),[StringLiteral("Hello word!")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,303))

#     def test_func_decl_5(self):
#         input = """int main(int a, float b, string c[]) {}"""
#         expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(StringType()))],IntType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,304))

#     def test_func_decl_6(self):
#         input = """int mc_function() {}
#         void func() {}"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([])),FuncDecl(Id("func"),[],VoidType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,305))

#     def test_func_decl_7(self):
#         input = """int mc_function(float x) {}
#         string[] foofunc(int y[]) {}"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[VarDecl("x",FloatType())],IntType(),Block([])),FuncDecl(Id("foofunc"),[VarDecl("y",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,306))

#     def test_func_decl_8(self):
#         input = """int main() {
#             foofunc();
#         }
#         void foofunc() {
#             print("Hello Word !!");
#             a = a + 1;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("foofunc"),[])])),FuncDecl(Id("foofunc"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("Hello Word !!")]),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,307))

    
#     def test_func_decl_9(self):
#         input = """string[] foofunc(boolean check) {}"""
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("check",BoolType())],ArrayPointerType(StringType()),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,308))

#     def test_func_decl_10(self):
#         input = """int mc_function(float b, boolean c[]) {}
#         string[] foofunc(int a[]) {
#             print("Hello Word !!");
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[VarDecl("b",FloatType()),VarDecl("c",ArrayPointerType(BoolType()))],IntType(),Block([])),FuncDecl(Id("foofunc"),[VarDecl("a",ArrayPointerType(IntType()))],ArrayPointerType(StringType()),Block([CallExpr(Id("print"),[StringLiteral("Hello Word !!")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,309))
   
#     def test_full1(self):
#         input = """
#         void mc_function()
#         {
#             float pi,t,n,eps,dau;
#             clrscr();
#             printf("Nhap sai so eps=");scanf("%f",eps);
#             pi=0;t=4;n=dau=1;
#             do
#             {
#                 pi=dau*t; n=n+2;
#                 dau=-dau; t=4/n;
#             }while (t>=eps);
#             printf("So PI tinh duoc voi sai so %12.10f, PI=%12.10f",eps,pi);
#             printf("So PI cua Turbo C++, PI=%12.10f",M_PI);
#             getch();
#         }

#         """
#         expect = str(Program([FuncDecl(Id("mc_function"),[],VoidType(),Block([VarDecl("pi",FloatType()),VarDecl("t",FloatType()),VarDecl("n",FloatType()),VarDecl("eps",FloatType()),VarDecl("dau",FloatType()),CallExpr(Id("clrscr"),[]),CallExpr(Id("printf"),[StringLiteral("Nhap sai so eps=")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("eps")]),BinaryOp("=",Id("pi"),IntLiteral(0)),BinaryOp("=",Id("t"),IntLiteral(4)),BinaryOp("=",Id("n"),BinaryOp("=",Id("dau"),IntLiteral(1))),Dowhile([Block([BinaryOp("=",Id("pi"),BinaryOp("*",Id("dau"),Id("t"))),BinaryOp("=",Id("n"),BinaryOp("+",Id("n"),IntLiteral(2))),BinaryOp("=",Id("dau"),UnaryOp("-",Id("dau"))),BinaryOp("=",Id("t"),BinaryOp("/",IntLiteral(4),Id("n")))])],BinaryOp(">=",Id("t"),Id("eps"))),CallExpr(Id("printf"),[StringLiteral("So PI tinh duoc voi sai so %12.10f, PI=%12.10f"),Id("eps"),Id("pi")]),CallExpr(Id("printf"),[StringLiteral("So PI cua Turbo C++, PI=%12.10f"),Id("M_PI")]),CallExpr(Id("getch"),[])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,310))
#     def test_full2(self):
#         input = """
#         void LietKeDongChuaGiaTriChan(int a[], int dong, int cot)
#         {
#             int flag;
#             for(i = 0; i < dong; i)
#             {
#                 flag = 0;
#                 for(j = 0; j < cot; j)
#                 {
#                     if(a[i] % 2 == 0)
#                     {
#                         flag = 1;
#                         break;
#                     }
#                 }
#                 if(flag == 1)
#                 {
#                     printf("Dong a[%d] co chua so chan ", i); 
#                 }	
#             }
#         }

#         """
#         expect = str(Program([FuncDecl(Id("LietKeDongChuaGiaTriChan"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("dong",IntType()),VarDecl("cot",IntType())],VoidType(),Block([VarDecl("flag",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("dong")),Id("i"),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("cot")),Id("j"),Block([If(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),Id("i")),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("flag"),IntLiteral(1)),Block([CallExpr(Id("printf"),[StringLiteral("Dong a[%d] co chua so chan "),Id("i")])]))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,311))

#     def test_full3(self):
#         input = """
#         void myfunction(){
#             do {} while (!true);
#         }
        
#         int mc_function() {
#             myfunction();
#             getch();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("myfunction"),[],VoidType(),Block([Dowhile([Block([])],UnaryOp("!",BooleanLiteral("true")))])),FuncDecl(Id("mc_function"),[],IntType(),Block([CallExpr(Id("myfunction"),[]),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,312))

#     def test_full4(self):
#         input = """
#         int main(){
#             !2;
#             getch();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",IntLiteral(2)),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,313))


#     def test_full5(self):
#         input = """
#         int main()
#         {
#             float themang, n;
#             int sochuso;

#             do
#             {
#             printf("Nhap n: ");
#             scanf("%ld",n);
#             }while(n < 0 && printf("Loi: n >= 0 !"));
#             sochuso = 0;
#             themang = n;

#             if(n == 0)
#                     sochuso = 1;
            
#             printf("So chu so cua %ld la %d", n, sochuso);

#             getch();
#             return 0;
#         }

#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("themang",FloatType()),VarDecl("n",FloatType()),VarDecl("sochuso",IntType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap n: ")]),CallExpr(Id("scanf"),[StringLiteral("%ld"),Id("n")])])],BinaryOp("&&",BinaryOp("<",Id("n"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Loi: n >= 0 !")]))),BinaryOp("=",Id("sochuso"),IntLiteral(0)),BinaryOp("=",Id("themang"),Id("n")),If(BinaryOp("==",Id("n"),IntLiteral(0)),BinaryOp("=",Id("sochuso"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("So chu so cua %ld la %d"),Id("n"),Id("sochuso")]),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,314))



#     def test_full6(self):
#         input = """void foofunco(boolean x, int y[], float z[]) {}
#         int main(){
#             return x+" "+ "a";
#         }
#         """
#         expect = str(Program([
#             FuncDecl(Id("foofunco"),[VarDecl("x",BoolType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",ArrayPointerType(FloatType()))],VoidType(),Block([]))
#             ,FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp('+',BinaryOp('+',Id('x'),StringLiteral(' ')),StringLiteral('a')))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,315))

#     def test_full8(self):
#         input = """void foofunco(boolean x, int y[], float z[]) {}
#         int mc_function(){
#             continue;
#             return -(x+5/2 -5.2 >= 1.2);
#         }
#         """
#         expect = str(Program([
#             FuncDecl(Id("foofunco"),[VarDecl("x",BoolType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",ArrayPointerType(FloatType()))],VoidType(),Block([]))
#             ,FuncDecl(Id("mc_function"),[],IntType(),Block([Continue(),Return(UnaryOp('-',BinaryOp('>=',BinaryOp('-',BinaryOp('+',Id('x'),BinaryOp('/',IntLiteral(5),IntLiteral(2))),FloatLiteral(5.2)),FloatLiteral(1.2))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,316))

#     def test_full_9(self):
#         input = """int mc_function() {
#             int x;
#             float y;
#             printf("Input total distance in km: ");
#             scanf("%d",x);
#             printf("Input total fuel spent in liters: ");
#             scanf("%f", y);
#             printf("Average consumption (km/lt) %.3f ",x/y);
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",FloatType()),CallExpr(Id("printf"),[StringLiteral("Input total distance in km: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("x")]),CallExpr(Id("printf"),[StringLiteral("Input total fuel spent in liters: ")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("y")]),CallExpr(Id("printf"),[StringLiteral("Average consumption (km/lt) %.3f "),BinaryOp("/",Id("x"),Id("y"))]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,317))

#     def test_full_10(self):
#         input = """int main() {
#             int x, y;
#             printf("Input the first number: "); 
#             scanf("%d", x);
#             printf("Input the second number: ");
#             scanf("%d", y);
#             if(x > y) {
#                 int temp;
#                 temp = x;
#                 x = y;
#                 y = temp;
#             }
#             if((y % x)== 0) printf("Multiplied!");
#             else printf("Not Multiplied!");
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),CallExpr(Id("printf"),[StringLiteral("Input the first number: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("x")]),CallExpr(Id("printf"),[StringLiteral("Input the second number: ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("y")]),If(BinaryOp(">",Id("x"),Id("y")),Block([VarDecl("temp",IntType()),BinaryOp("=",Id("temp"),Id("x")),BinaryOp("=",Id("x"),Id("y")),BinaryOp("=",Id("y"),Id("temp"))])),If(BinaryOp("==",BinaryOp("%",Id("y"),Id("x")),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Multiplied!")]),CallExpr(Id("printf"),[StringLiteral("Not Multiplied!")])),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,318))

#     def test_full_11(self):
#         input = """int main() {
#             float N[10];
#             int i;
#             printf("Input the 5 members of the array:");
#             for(i = 0; i < AL; i=i+1) {
#                 scanf("%f", N[0]);
#             }
#             for(i = 0; i < AL; i=i+1) {
#                 if(N[0] < MAX) printf("A[%d] = %.1f", i, N[0]);
#             }
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("N",ArrayType(10,FloatType())),VarDecl("i",IntType()),CallExpr(Id("printf"),[StringLiteral("Input the 5 members of the array:")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("AL")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("scanf"),[StringLiteral("%f"),ArrayCell(Id("N"),IntLiteral(0))])])),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("AL")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([If(BinaryOp("<",ArrayCell(Id("N"),IntLiteral(0)),Id("MAX")),CallExpr(Id("printf"),[StringLiteral("A[%d] = %.1f"),Id("i"),ArrayCell(Id("N"),IntLiteral(0))]))])),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,319))

#     def test_full_12(self):
#         input = """int mc_function (){
#             int x;

#             printf ("Is command processor available?");
#             if (system(NULL)) printf ("Command processor available!");
#             else {
#                 printf ("Command processor not available!");
#                 exit (1);
#             }
#             printf ("Executing command DIR");
#             x=system ("dir");
#             printf ("Returned value is: %d.",x);
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("x",IntType()),CallExpr(Id("printf"),[StringLiteral("Is command processor available?")]),If(CallExpr(Id("system"),[Id("NULL")]),CallExpr(Id("printf"),[StringLiteral("Command processor available!")]),Block([CallExpr(Id("printf"),[StringLiteral("Command processor not available!")]),CallExpr(Id("exit"),[IntLiteral(1)])])),CallExpr(Id("printf"),[StringLiteral("Executing command DIR")]),BinaryOp("=",Id("x"),CallExpr(Id("system"),[StringLiteral("dir")])),CallExpr(Id("printf"),[StringLiteral("Returned value is: %d."),Id("x")]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,320))

#     def test_full_13(self):
#         input = """int mc_function () {
#             int number, input;
#             /* initialize random seed: */
#             srand (time(NULL));
#             /* Generate a random number: */
#             number = rand() % 10 + 1;
#             do {
#                     printf ("Guess the number (1 to 10): ");
#                     scanf ("%d",input);
#                     if (number > input) printf ("The number is higher");
#                 } while (number!=input);
#             printf ("That is correct!");
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("number",IntType()),VarDecl("input",IntType()),CallExpr(Id("srand"),[CallExpr(Id("time"),[Id("NULL")])]),BinaryOp("=",Id("number"),BinaryOp("+",BinaryOp("%",CallExpr(Id("rand"),[]),IntLiteral(10)),IntLiteral(1))),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Guess the number (1 to 10): ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("input")]),If(BinaryOp(">",Id("number"),Id("input")),CallExpr(Id("printf"),[StringLiteral("The number is higher")]))])],BinaryOp("!=",Id("number"),Id("input"))),CallExpr(Id("printf"),[StringLiteral("That is correct!")]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,321))

#     def test_if_state_1(self):
#         input = """int mc_function() {
#             if (1) {}
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([If(IntLiteral(1),Block([]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,322))

#     def test_if_state_2(self):
#         input = """int mc_func() {
#             if (1) {
#                 print("Hello Word !!");
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([If(IntLiteral(1),Block([CallExpr(Id("print"),[StringLiteral("Hello Word !!")])]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,323))

#     def test_if_state_3(self):
#         input = """int mc_func() {
#             if (true) {
#                 {}
#                 int a;
#                 float b[10];
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([If(BooleanLiteral(True),Block([Block([]),VarDecl("a",IntType()),VarDecl("b",ArrayType(10,FloatType()))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,324))

#     def test_if_state_4(self):
#         input = """int mc_func() {
#             if (1) {}
#         }
#         void foofunc(int a) {
#             if (a) {
#                 a = a + 1;
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([If(IntLiteral(1),Block([]))])),FuncDecl(Id("foofunc"),[VarDecl("a",IntType())],VoidType(),Block([If(Id("a"),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,325))

#     def test_if_state_5(self):
#         input = """int mc_func() {
#             if (1) {} {}
#             if (1+1) {
#                 do print("Hello Word !!"); while (true);
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([If(IntLiteral(1),Block([])),Block([]),If(BinaryOp("+",IntLiteral(1),IntLiteral(1)),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Word !!")])],BooleanLiteral(True))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,326))

#     def test_if_state_6(self):
#         input = """int main() {
#             if (1) {} else {}
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]),Block([]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,327))

#     def test_if_state_7(self):
#         input = """int main() {
#             if (1) {} else print("Hello Word !!");
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(IntLiteral(1),Block([]),CallExpr(Id("print"),[StringLiteral("Hello Word !!")]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,328))

#     def test_if_state_8(self):
#         input = """int main() {
#             if (true) {
#                 if (a==2) a = a + 1;
#                 else a = a - 1;
#             }
#             else {}
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BooleanLiteral(True),Block([If(BinaryOp("==",Id("a"),IntLiteral(2)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),BinaryOp('-',Id("a"),IntLiteral(1))))]),Block([]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,329))

#     def test_if_state_9(self):
#         input = """int mc_func() {
#             int a;
#             do {
#                 if (true) print(a);
#                 else print(a+1);
#             } while(flase);
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([VarDecl("a",IntType()),Dowhile([Block([If(BooleanLiteral(True),CallExpr(Id("print"),[Id("a")]),CallExpr(Id("print"),[BinaryOp("+",Id("a"),IntLiteral(1))]))])],Id("flase"))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,330))

#     def test_if_state_10(self):
#         input = """int mc_func() {
#             if (a && false) {
#                 if (true) int a;
#             }
#             else {
#                 if (false) int b;
#                 else int c;
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],IntType(),Block([If(BinaryOp("&&",Id("a"),BooleanLiteral(False)),Block([If(BooleanLiteral(True),Block([VarDecl("a",IntType())]))]),Block([If(BooleanLiteral(False),Block([VarDecl("b",IntType())]),Block([VarDecl("c",IntType())]))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,331))

#     def test_simple_program_001(self):
#         input = """
#             int x;
#         """
#         expect = str(Program([VarDecl("x",IntType())]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,332))
    
#     def test_function_2(self):
#         input = """float mc_func() {}"""
#         expect = str(Program([FuncDecl(Id("mc_func"),[],FloatType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,333))

#     def test_function_13(self):
#         input = """
#         int foofunc(int a) {
#             int b;
#             b = a;
#             print("ID = ",a);
#             return b;
#         }
#         int ham() {
#             int arr[1];
#             arr[1] = foofunc(arr[0]);
#             }
#         """
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),Id("a")),CallExpr(Id("print"),[StringLiteral("ID = "),Id("a")]),Return(Id("b"))])),FuncDecl(Id("ham"),[],IntType(),Block([VarDecl("arr",ArrayType(1,IntType())),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(1)),CallExpr(Id("foofunc"),[ArrayCell(Id("arr"),IntLiteral(0))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,334))

    
#     def test_program_1(self):
#         input="""
#         float main(){
#             for (x=2;x<5;x=x+2){
#                 if (x%2==0) {
#                     print("x la so chan");
#                     return x;
#                 }
#                 else {
#                     for (j=0; j<10;j=j+2){
#                         if(j<=x){
#                             print("j la so nho hon x");
#                         }
#                     }
#                 }
#             }
#             print("Hello my func");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             FloatType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('x la so chan')]),
#             Return(Id('x'))
#             ]),
#             Block([
#             For(BinaryOp('=',Id('j'),IntLiteral(0)),
#             BinaryOp('<',Id('j'),IntLiteral(10)),
#             BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('<=',Id('j'),Id('x')),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('j la so nho hon x')])
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('Hello my func')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 335))

#     def test_program_2(self):
#         input="""
#         void main(){
#             for (x=2;x<5;x=x+2){
#                 if (x%2==0) {
#                     print("x la so chan");
#                     return x;
#                 }
#             }
#             print("Hello! This is main");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('x la so chan')]),
#             Return(Id('x'))
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('Hello! This is main')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    

#     def test_program_29(self):
#         input = """
#         int[] foofunc(float a[]){
#             return 2;
#         }
#         int ham(float a[]){
#             getArray();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([Return(IntLiteral(2))])),FuncDecl(Id("ham"),[VarDecl("a",ArrayPointerType(FloatType()))],IntType(),Block([CallExpr(Id("getArray"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,337))

#     def test_program_3(self):
#         input = """
#         void ham( int n)
#         {
#             for(i = 0; i < n - 1; i)
#             {
#                 if(a[i] % 2 != 0)
#                 {
#                     for(j = i + 1; j < n; j)
#                     {
#                         if(a[j] % 2 != 0 && a[i] > a[j])
#                         {
#                             foofunc(a[i], a[j]);
#                         }
#                     }

#                 }
#             }
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('ham'),
#             [VarDecl('n',IntType())],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('i'),IntLiteral(0)),
#             BinaryOp('<',Id('i'),BinaryOp('-',Id('n'),IntLiteral(1))),
#             Id('i'),
#             Block([
#             If(BinaryOp('!=',BinaryOp('%',ArrayCell(Id('a'),Id('i')),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             For(BinaryOp('=',Id('j'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             BinaryOp('<',Id('j'),Id('n')),
#             Id('j'),
#             Block([
#             If(BinaryOp('&&',BinaryOp('!=',BinaryOp('%',ArrayCell(Id('a'),Id('j')),IntLiteral(2)),IntLiteral(0)),BinaryOp('>',ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j')))),
#             Block([
#             CallExpr(Id('foofunc'),[ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j'))])
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,338))

#     def test_program_4(self):
#         input="""
#         float main(){
#             return x + 1;
#             for ( i=1;i<5;i=i+1){
#                 if ( i==2) break;
#                 else {
#                     print(i);
#                     foofunc(i);
#                 }
#                 return foofunc(x);
#             }
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             FloatType(),
#             Block([
#             Return(BinaryOp('+',Id('x'),IntLiteral(1))),
#             For(BinaryOp('=',Id('i'),IntLiteral(1)),
#             BinaryOp('<',Id('i'),IntLiteral(5)),
#             BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('==',Id('i'),IntLiteral(2)),
#             Break(),
#             Block([
#             CallExpr(Id('print'),[Id('i')]),
#             CallExpr(Id('foofunc'),[Id('i')])
#             ])
#             ),
#             Return(CallExpr(Id('foofunc'),[Id('x')]))
#             ])
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 339))


#     def test_program_5(self):
#         input="""
#         void main(){
#             for (x=2;x<5;x=x+1){
#                 if (x%2==0) {
#                     print(x);
#                     return x;
#                 }
#             }
#             print("foofunc");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[Id('x')]),
#             Return(Id('x'))
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('foofunc')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 340))
    
#     def test_program_6(self):
#         input = """
#         void ham() {
#             int x; x = 0;
#             int i,j;
#             do{
#                 x= x+1;
#                 for(i = 1*x; i <= 100*x; i= i + 1){
#                     if(i%2==0 && i %3==0)
#                         print(i);
#                 }
#             }{}
#             while(x<10);
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('ham'),
#             [],
#             VoidType(),
#             Block([
#             VarDecl('x',IntType()),
#             BinaryOp('=',Id('x'),IntLiteral(0)),
#             VarDecl('i',IntType()),
#             VarDecl('j',IntType()),
#             Dowhile([Block([
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),
#             For(BinaryOp('=',Id('i'),BinaryOp('*',IntLiteral(1),Id('x'))),
#             BinaryOp('<=',Id('i'),BinaryOp('*',IntLiteral(100),Id('x'))),
#             BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('&&',BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(3)),IntLiteral(0))),
#             CallExpr(Id('print'),[Id('i')])
#             )
#             ])
#             )
#             ]),
#             Block([

#             ])],
#             BinaryOp('<',Id('x'),IntLiteral(10))
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,341))

#     def test_program_microC_23(self):
#         input = """
#         int ham()
#         {
#             int n1,f;
#             printf(" Recursion : Find the Factorial of a number :");
#             printf("-------------------------------------------------");	  
#             printf(" Input  a number : ");
#             scanf("%d",n1);
#             f = findFactorial(n1); //call the function findFactorial for factorial
#             printf(" The Factorial of %d is : %d",n1,f);
#             return 0;
#         }

#         int findFactorial(int n) {
#             if(n==1) return 1;
#             else return(n*findFactorial(n-1));// calling the function findFactorial to itself recursively
#         }
#         """
#         expect = str(Program([FuncDecl(Id("ham"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("f",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Find the Factorial of a number :")]),CallExpr(Id("printf"),[StringLiteral("-------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input  a number : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("f"),CallExpr(Id("findFactorial"),[Id("n1")])),CallExpr(Id("printf"),[StringLiteral(" The Factorial of %d is : %d"),Id("n1"),Id("f")]),Return(IntLiteral(0))])),FuncDecl(Id("findFactorial"),[VarDecl("n",IntType())],IntType(),Block([If(BinaryOp("==",Id("n"),IntLiteral(1)),Return(IntLiteral(1)),Return(BinaryOp("*",Id("n"),CallExpr(Id("findFactorial"),[BinaryOp("-",Id("n"),IntLiteral(1))]))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,342))

#     def test_program_microC_24(self):
#         input = """
#         int i;
#         int mainfunc() {
#             int n1,primeNo;
#             printf(" Recursion : Check a number is prime number or not :");
#             printf("--------------------------------------------------------");
#             printf(" Input any positive number : ");
#             scanf("%d",n1);
#             i = n1/2;
#             primeNo = checkForPrime(n1); //call the function checkForPrime
#             if(primeNo==1) printf(" The number %d is a prime number. ",n1);
#             else printf(" The number %d is not a prime number.",n1);
#             return 0;
#         }

#         int checkForPrime(int n1) {
#             if(i==1) return 1;
#             if(n1 %i==0) return 0;
#             else {
#                 i = i -1; 
#                 checkForPrime(n1); //calling the function checkForPrime itself recursively
#             }
#         }
#         """
#         expect = str(Program([VarDecl("i",IntType()),FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("primeNo",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Check a number is prime number or not :")]),CallExpr(Id("printf"),[StringLiteral("--------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input any positive number : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),BinaryOp("=",Id("i"),BinaryOp("/",Id("n1"),IntLiteral(2))),BinaryOp("=",Id("primeNo"),CallExpr(Id("checkForPrime"),[Id("n1")])),If(BinaryOp("==",Id("primeNo"),IntLiteral(1)),CallExpr(Id("printf"),[StringLiteral(" The number %d is a prime number. "),Id("n1")]),CallExpr(Id("printf"),[StringLiteral(" The number %d is not a prime number."),Id("n1")])),Return(IntLiteral(0))])),FuncDecl(Id("checkForPrime"),[VarDecl("n1",IntType())],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Return(IntLiteral(1))),If(BinaryOp("==",BinaryOp("%",Id("n1"),Id("i")),IntLiteral(0)),Return(IntLiteral(0)),Block([BinaryOp("=",Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),CallExpr(Id("checkForPrime"),[Id("n1")])]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,343))

#     def test_program_microC_25(self):
#         input = """
#         int mainfunc() {
#             int n1, n2, lcmOf;
#             printf(" Recursion : Find the LCM of two numbers :");
#             printf("----------------------------------------------");
#             printf(" Input 1st number for LCM : ");
#             scanf("%d", n1);
#             printf(" Input 2nd number for LCM : ");
#             scanf("%d", n2);
#             // Ensures that first parameter of lcm must be smaller than 2nd
#             if(n1 >  n2) lcmOf = lcmCalculate(n2, n1); //call the function lcmCalculate for lcm calculation
#             else lcmOf = lcmCalculate(n1, n2);//call the function lcmCalculate for lcm calculation
#             printf(" The LCM of %d and %d :  %d", n1, n2, lcmOf);
#             return 0;
#         }
#         int lcmCalculate(int a, int b) //the value of n1 and n2 is passing through a and b
#         {
#             int m;
#             //Increments m by adding max value to it
#             m = m+b;
#             // If found a common multiple then return the m.
#             if((m % a == 0) && (m % b == 0)) return m;
#             else lcmCalculate(a, b); //calling the function lcmCalculate itself
#         }
#         """
#         expect = str(Program([FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("n1",IntType()),VarDecl("n2",IntType()),VarDecl("lcmOf",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Find the LCM of two numbers :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input 1st number for LCM : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n1")]),CallExpr(Id("printf"),[StringLiteral(" Input 2nd number for LCM : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n2")]),If(BinaryOp(">",Id("n1"),Id("n2")),BinaryOp("=",Id("lcmOf"),CallExpr(Id("lcmCalculate"),[Id("n2"),Id("n1")])),BinaryOp("=",Id("lcmOf"),CallExpr(Id("lcmCalculate"),[Id("n1"),Id("n2")]))),CallExpr(Id("printf"),[StringLiteral(" The LCM of %d and %d :  %d"),Id("n1"),Id("n2"),Id("lcmOf")]),Return(IntLiteral(0))])),FuncDecl(Id("lcmCalculate"),[VarDecl("a",IntType()),VarDecl("b",IntType())],IntType(),Block([VarDecl("m",IntType()),BinaryOp("=",Id("m"),BinaryOp("+",Id("m"),Id("b"))),If(BinaryOp("&&",BinaryOp("==",BinaryOp("%",Id("m"),Id("a")),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("m"),Id("b")),IntLiteral(0))),Return(Id("m")),CallExpr(Id("lcmCalculate"),[Id("a"),Id("b")]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,344))

#     def test_program_microC_26(self):
#         input = """
#         int main() {
#             int n;
#             printf(" Recursion : Print even or odd numbers in a given range :");
#             printf("-------------------------------------------------------------");
#             printf(" Input the range to print starting from 1 : ");
#             scanf("%d", n);
#             printf(" All even numbers from 1 to %d are : ", n);
#             EvenAndOdd(2, n); //call the function EvenAndOdd for even numbers 
#             printf(" All odd numbers from 1 to %d are : ", n);
#             EvenAndOdd(1, n); // call the function EvenAndOdd for odd numbers
#             printf("");
#             return 0;
#         }
#         void EvenAndOdd(int stVal, int n) {
#             if(stVal > n) return;
#             printf("%d  ", stVal);
#             EvenAndOdd(stVal+2, n); //calling the function EvenAndOdd itself recursively
#         }
#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("n",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Print even or odd numbers in a given range :")]),CallExpr(Id("printf"),[StringLiteral("-------------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input the range to print starting from 1 : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" All even numbers from 1 to %d are : "),Id("n")]),CallExpr(Id("EvenAndOdd"),[IntLiteral(2),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" All odd numbers from 1 to %d are : "),Id("n")]),CallExpr(Id("EvenAndOdd"),[IntLiteral(1),Id("n")]),CallExpr(Id("printf"),[StringLiteral("")]),Return(IntLiteral(0))])),FuncDecl(Id("EvenAndOdd"),[VarDecl("stVal",IntType()),VarDecl("n",IntType())],VoidType(),Block([If(BinaryOp(">",Id("stVal"),Id("n")),Return()),CallExpr(Id("printf"),[StringLiteral("%d  "),Id("stVal")]),CallExpr(Id("EvenAndOdd"),[BinaryOp("+",Id("stVal"),IntLiteral(2)),Id("n")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,345))

#     def test_program_microC_27(self):
#         input = """
#         int main() {
#             string wordPal[25];
#             printf(" Recursion : Check a given string is Palindrome or not :");
#             printf("----------------------------------------------------------");	
#             printf(" Input  a word to check for palindrome : ");
#             scanf("%s", wordPal);
#             checkPalindrome(wordPal, 0);//call the function for checking Palindore
#             return 0;
#         }
        
#         void checkPalindrome(string wordPal[], int index) {
#             int len;
#             len = strlen(wordPal) - (index + 1);
#             if (wordPal[index] == wordPal[len]) {
#                 if (index + 1 == len || index == len) {
#                     printf(" The entered word is a palindrome.");
#                     return;
#                 }
#                 checkPalindrome(wordPal, index + 1);//calling the function itself recursively
#             }
#             else {
#                 printf(" The entered word is not a palindrome.");
#             }
#         }
#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("wordPal",ArrayType(25,StringType())),CallExpr(Id("printf"),[StringLiteral(" Recursion : Check a given string is Palindrome or not :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input  a word to check for palindrome : ")]),CallExpr(Id("scanf"),[StringLiteral("%s"),Id("wordPal")]),CallExpr(Id("checkPalindrome"),[Id("wordPal"),IntLiteral(0)]),Return(IntLiteral(0))])),FuncDecl(Id("checkPalindrome"),[VarDecl("wordPal",ArrayPointerType(StringType())),VarDecl("index",IntType())],VoidType(),Block([VarDecl("len",IntType()),BinaryOp("=",Id("len"),BinaryOp("-",CallExpr(Id("strlen"),[Id("wordPal")]),BinaryOp("+",Id("index"),IntLiteral(1)))),If(BinaryOp("==",ArrayCell(Id("wordPal"),Id("index")),ArrayCell(Id("wordPal"),Id("len"))),Block([If(BinaryOp("||",BinaryOp("==",BinaryOp("+",Id("index"),IntLiteral(1)),Id("len")),BinaryOp("==",Id("index"),Id("len"))),Block([CallExpr(Id("printf"),[StringLiteral(" The entered word is a palindrome.")]),Return()])),CallExpr(Id("checkPalindrome"),[Id("wordPal"),BinaryOp("+",Id("index"),IntLiteral(1))])]),Block([CallExpr(Id("printf"),[StringLiteral(" The entered word is not a palindrome.")])]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,346))

#     def test_program_microC_28(self):
#         input = """
#         int mainfunc() {
#             int arr1[10], i, n, md, c, low, hg;
#             printf(" Recursion : Binary searching :");
#             printf("-----------------------------------");
#             printf(" Input the number of elements to store in the array :");
#             scanf("%d", n);
#             printf(" Input %d numbers of elements in the array in ascending order :", n);
#             for (i = 0; i < n; i=i+1) {
#                 printf(" element - %d : ", i);
#                 scanf("%d", arr1[1]);
#             }
#             printf(" Input the number to search : ");
#             scanf("%d", md);
#             low = 0;
#             hg = n - 1;
#             c = binarySearch(arr1, n, md, low, hg);
#             if (c == 0) printf(" The search number not exists in the array.");
#             else printf(" The search number found in the array.");
#             return 0;
#         }

#         int binarySearch(int arr1[], int n, int md, int low, int hg) {
#             int mid, c;
#             if (low <= hg) {
#                 mid = (low + hg) / 2;
#                 if (md == arr1[1]) c = 1;
#                 if (md < arr1[1]) return binarySearch(arr1, n, md, low, mid - 1);
#                 else  return binarySearch(arr1, n, md, mid + 1, hg);
#             }
#             else return c;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("arr1",ArrayType(10,IntType())),VarDecl("i",IntType()),VarDecl("n",IntType()),VarDecl("md",IntType()),VarDecl("c",IntType()),VarDecl("low",IntType()),VarDecl("hg",IntType()),CallExpr(Id("printf"),[StringLiteral(" Recursion : Binary searching :")]),CallExpr(Id("printf"),[StringLiteral("-----------------------------------")]),CallExpr(Id("printf"),[StringLiteral(" Input the number of elements to store in the array :")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("n")]),CallExpr(Id("printf"),[StringLiteral(" Input %d numbers of elements in the array in ascending order :"),Id("n")]),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("n")),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([CallExpr(Id("printf"),[StringLiteral(" element - %d : "),Id("i")]),CallExpr(Id("scanf"),[StringLiteral("%d"),ArrayCell(Id("arr1"),IntLiteral(1))])])),CallExpr(Id("printf"),[StringLiteral(" Input the number to search : ")]),CallExpr(Id("scanf"),[StringLiteral("%d"),Id("md")]),BinaryOp("=",Id("low"),IntLiteral(0)),BinaryOp("=",Id("hg"),BinaryOp("-",Id("n"),IntLiteral(1))),BinaryOp("=",Id("c"),CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),Id("low"),Id("hg")])),If(BinaryOp("==",Id("c"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral(" The search number not exists in the array.")]),CallExpr(Id("printf"),[StringLiteral(" The search number found in the array.")])),Return(IntLiteral(0))])),FuncDecl(Id("binarySearch"),[VarDecl("arr1",ArrayPointerType(IntType())),VarDecl("n",IntType()),VarDecl("md",IntType()),VarDecl("low",IntType()),VarDecl("hg",IntType())],IntType(),Block([VarDecl("mid",IntType()),VarDecl("c",IntType()),If(BinaryOp("<=",Id("low"),Id("hg")),Block([BinaryOp("=",Id("mid"),BinaryOp("/",BinaryOp("+",Id("low"),Id("hg")),IntLiteral(2))),If(BinaryOp("==",Id("md"),ArrayCell(Id("arr1"),IntLiteral(1))),BinaryOp("=",Id("c"),IntLiteral(1))),If(BinaryOp("<",Id("md"),ArrayCell(Id("arr1"),IntLiteral(1))),Return(CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),Id("low"),BinaryOp("-",Id("mid"),IntLiteral(1))])),Return(CallExpr(Id("binarySearch"),[Id("arr1"),Id("n"),Id("md"),BinaryOp("+",Id("mid"),IntLiteral(1)),Id("hg")])))]),Return(Id("c")))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,347))

#     def test_program_microC_29(self):
#         input = """
#         int mainfunc() {
#             string str[1000];
#             string fname[20];
#             fname = "test.txt";
#             printf(" Create a file (test.txt) and input text :");
#             printf("----------------------------------------------"); 
#             fptr = fopen(fname,"w");	
#             if(fptr==NULL) {
#                 printf(" Error in opening file!");
#                 exit(1);
#             }
#             printf(" Input a sentence for the file : ");
#             fgets(str, sizeof(str), stdin);
#             fprintf(fptr,"%s",str);
#             fclose(fptr);
#             printf(" The file %s created successfully...!!",fname);
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("str",ArrayType(1000,StringType())),VarDecl("fname",ArrayType(20,StringType())),BinaryOp("=",Id("fname"),StringLiteral("test.txt")),CallExpr(Id("printf"),[StringLiteral(" Create a file (test.txt) and input text :")]),CallExpr(Id("printf"),[StringLiteral("----------------------------------------------")]),BinaryOp("=",Id("fptr"),CallExpr(Id("fopen"),[Id("fname"),StringLiteral("w")])),If(BinaryOp("==",Id("fptr"),Id("NULL")),Block([CallExpr(Id("printf"),[StringLiteral(" Error in opening file!")]),CallExpr(Id("exit"),[IntLiteral(1)])])),CallExpr(Id("printf"),[StringLiteral(" Input a sentence for the file : ")]),CallExpr(Id("fgets"),[Id("str"),CallExpr(Id("sizeof"),[Id("str")]),Id("stdin")]),CallExpr(Id("fprintf"),[Id("fptr"),StringLiteral("%s"),Id("str")]),CallExpr(Id("fclose"),[Id("fptr")]),CallExpr(Id("printf"),[StringLiteral(" The file %s created successfully...!!"),Id("fname")]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,348))

#     def test_program_microC_30(self):
#         input = """
#         int main() {
#             float s, j, d, i;
#             for(i=1; i<=7; i=i+2){
#                 d = (i/j);
#                 s = s+ 1.72E-1;
#                 j = j*2;
#             }
#             printf("Value of series: %.2lf", s);
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("s",FloatType()),VarDecl("j",FloatType()),VarDecl("d",FloatType()),VarDecl("i",FloatType()),For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(7)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(2))),Block([BinaryOp("=",Id("d"),BinaryOp("/",Id("i"),Id("j"))),BinaryOp("=",Id("s"),BinaryOp("+",Id("s"),FloatLiteral("1.72E-1"))),BinaryOp("=",Id("j"),BinaryOp("*",Id("j"),IntLiteral(2)))])),CallExpr(Id("printf"),[StringLiteral("Value of series: %.2lf"),Id("s")]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,349))


#     def test_var_decl_2(self):
#         input = """int main() {
#             float a;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType())]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,350))

#     def test_var_decl_3(self):
#         input = """int main() {}
#         boolean a,b,c[10];"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",ArrayType(10,BoolType()))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,351))

#     def test_var_decl_4(self):
#         input = """int main() {
#             string a,b[100];
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",StringType()),VarDecl("b",ArrayType(100,StringType()))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,352))

#     def test_var_decl_5(self):
#         input = """int main() {
#             float b;
#             string c[5];
#         }
#         int a[5];"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("b",FloatType()),VarDecl("c",ArrayType(5,StringType()))])),VarDecl("a",ArrayType(5,IntType()))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,353))

#     def test_var_decl_6(self):
#         input = """int main(int a[]) {
#             string c;
#         }
#         void foo(int a) {
#             boolean b[10];
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType()))],IntType(),Block([VarDecl("c",StringType())])),FuncDecl(Id("foo"),[VarDecl("a",IntType())],VoidType(),Block([VarDecl("b",ArrayType(10,BoolType()))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,354))

#     def test_var_decl_7(self):
#         input = """int main() {
#             int a;
#             float b[5];
#             print(a);
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,FloatType())),CallExpr(Id("print"),[Id("a")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,355))

#     def test_var_decl_8(self):
#         input = """int main() {}
#         void foo() {
#             float a[10], b[10], d;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("foo"),[],VoidType(),Block([VarDecl("a",ArrayType(10,FloatType())),VarDecl("b",ArrayType(10,FloatType())),VarDecl("d",FloatType())]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,356))

#     def test_var_decl_9(self):
#         input = """int[] main() {
#             string b[0];
#         }
#         int a[10];"""
#         expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("b",ArrayType(0,StringType()))])),VarDecl("a",ArrayType(10,IntType()))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,357))

#     def test_var_decl_10(self):
#         input = """int main() {}
#         int a;
#         float b[10];
#         string c;
#         boolean d, e[5], f;"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),VarDecl("a",IntType()),VarDecl("b",ArrayType(10,FloatType())),VarDecl("c",StringType()),VarDecl("d",BoolType()),VarDecl("e",ArrayType(5,BoolType())),VarDecl("f",BoolType())]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,358))

#     def test_do_while_state_1(self):
#         input = """int[] main() {
#             int a;
#             do print("Hello Python3"); while (true);
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],ArrayPointerType(IntType()),Block([VarDecl("a",IntType()),Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Python3")])],BooleanLiteral(True))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,359))



#     def test_1(self):
#         input = """
#         void main()
#         {
#             float pi,t,n,eps,dau;
#             clrscr();
#             printf("Nhap sai so eps=");scanf("%f",eps);
#             pi=0;t=4;n=dau=1;
#             do
#             {
#                 pi=dau*t; n=n+2;
#                 dau=-dau; t=4/n;
#             }while (t>=eps);
#             printf("So PI tinh duoc voi sai so %12.10f, PI=%12.10f",eps,pi);
#             printf("So PI cua Turbo C++, PI=%12.10f",M_PI);
#             getch();
#         }

#         """
#         expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([VarDecl("pi",FloatType()),VarDecl("t",FloatType()),VarDecl("n",FloatType()),VarDecl("eps",FloatType()),VarDecl("dau",FloatType()),CallExpr(Id("clrscr"),[]),CallExpr(Id("printf"),[StringLiteral("Nhap sai so eps=")]),CallExpr(Id("scanf"),[StringLiteral("%f"),Id("eps")]),BinaryOp("=",Id("pi"),IntLiteral(0)),BinaryOp("=",Id("t"),IntLiteral(4)),BinaryOp("=",Id("n"),BinaryOp("=",Id("dau"),IntLiteral(1))),Dowhile([Block([BinaryOp("=",Id("pi"),BinaryOp("*",Id("dau"),Id("t"))),BinaryOp("=",Id("n"),BinaryOp("+",Id("n"),IntLiteral(2))),BinaryOp("=",Id("dau"),UnaryOp("-",Id("dau"))),BinaryOp("=",Id("t"),BinaryOp("/",IntLiteral(4),Id("n")))])],BinaryOp(">=",Id("t"),Id("eps"))),CallExpr(Id("printf"),[StringLiteral("So PI tinh duoc voi sai so %12.10f, PI=%12.10f"),Id("eps"),Id("pi")]),CallExpr(Id("printf"),[StringLiteral("So PI cua Turbo C++, PI=%12.10f"),Id("M_PI")]),CallExpr(Id("getch"),[])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,360))
#     def test_full_mc_2(self):
#         input = """
#         void LietKe(int a[], int dong, int cot)
#         {
#             int flag;
#             for(i = 0; i < dong; i)
#             {
#                 flag = 0;
#                 for(j = 0; j < cot; j)
#                 {
#                     if(a[i] % 2 == 0)
#                     {
#                         flag = 1;
#                         break;
#                     }
#                 }
#                 if(flag == 1)
#                 {
#                     printf("Dong a[%d] co chua so chan ", i); 
#                 }	
#             }
#         }

#         """
#         expect = str(Program([FuncDecl(Id("LietKe"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("dong",IntType()),VarDecl("cot",IntType())],VoidType(),Block([VarDecl("flag",IntType()),For(BinaryOp("=",Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),Id("dong")),Id("i"),Block([BinaryOp("=",Id("flag"),IntLiteral(0)),For(BinaryOp("=",Id("j"),IntLiteral(0)),BinaryOp("<",Id("j"),Id("cot")),Id("j"),Block([If(BinaryOp("==",BinaryOp("%",ArrayCell(Id("a"),Id("i")),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp("=",Id("flag"),IntLiteral(1)),Break()]))])),If(BinaryOp("==",Id("flag"),IntLiteral(1)),Block([CallExpr(Id("printf"),[StringLiteral("Dong a[%d] co chua so chan "),Id("i")])]))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,361))


#     def test_full_mc_3(self):
#         input = """
#         void myfunction(){
#             do {} while (!true);
#         }
        
#         int main() {
#             myfunction();
#             getch();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("myfunction"),[],VoidType(),Block([Dowhile([Block([])],UnaryOp("!",BooleanLiteral("true")))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("myfunction"),[]),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,362))

#     def test_full_mc_4(self):
#         input = """
#         int main(){
#             !2;
#             getch();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([UnaryOp("!",IntLiteral(2)),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,363))


#     def test_full_mc_5(self):
#         input = """
#         int main()
#         {
#             float themang, n;
#             int sochuso;

#             do
#             {
#             printf("Nhap n: ");
#             scanf("%ld",n);
#             }while(n < 0 && printf("Loi: n >= 0 !"));
#             sochuso = 0;
#             themang = n;

#             if(n == 0)
#                     sochuso = 1;
            
#             printf("So chu so cua %ld la %d", n, sochuso);

#             getch();
#             return 0;
#         }

#         """
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("themang",FloatType()),VarDecl("n",FloatType()),VarDecl("sochuso",IntType()),Dowhile([Block([CallExpr(Id("printf"),[StringLiteral("Nhap n: ")]),CallExpr(Id("scanf"),[StringLiteral("%ld"),Id("n")])])],BinaryOp("&&",BinaryOp("<",Id("n"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Loi: n >= 0 !")]))),BinaryOp("=",Id("sochuso"),IntLiteral(0)),BinaryOp("=",Id("themang"),Id("n")),If(BinaryOp("==",Id("n"),IntLiteral(0)),BinaryOp("=",Id("sochuso"),IntLiteral(1))),CallExpr(Id("printf"),[StringLiteral("So chu so cua %ld la %d"),Id("n"),Id("sochuso")]),CallExpr(Id("getch"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,364))



#     def test_full_mc_6(self):
#         input = """void fooo(boolean x, int y[], float z[]) {}
#         int main(){
#             return x+" "+ "a";
#         }
#         """
#         expect = str(Program([
#             FuncDecl(Id("fooo"),[VarDecl("x",BoolType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",ArrayPointerType(FloatType()))],VoidType(),Block([]))
#             ,FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp('+',BinaryOp('+',Id('x'),StringLiteral(' ')),StringLiteral('a')))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,365))

#     def test_full_mc_7(self):
#         input = """void main() {
#             do{
#                 x= x+1;
                
#                 }{}
#             while(x<=100);
#             return ;
#         }"""
#         expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),Block([])],BinaryOp('<=',Id('x'),IntLiteral(100))),Return()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,366))


#     def test_full_7(self):
#         input = """void mc_function() {
#             do{
#                 x= x+1;
                
#                 }{}
#             while(x<=100);
#             return ;
#         }"""
#         expect = str(Program([FuncDecl(Id('mc_function'),[],VoidType(),Block([Dowhile([Block([BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))]),Block([])],BinaryOp('<=',Id('x'),IntLiteral(100))),Return()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,367))

#     def test_full_mc_8(self):
#         input = """void fooo(boolean x, int y[], float z[]) {}
#         int main(){
#             continue;
#             return -(x+5/2 -5.2 >= 1.2);
#         }
#         """
#         expect = str(Program([
#             FuncDecl(Id("fooo"),[VarDecl("x",BoolType()),VarDecl("y",ArrayPointerType(IntType())),VarDecl("z",ArrayPointerType(FloatType()))],VoidType(),Block([]))
#             ,FuncDecl(Id("main"),[],IntType(),Block([Continue(),Return(UnaryOp('-',BinaryOp('>=',BinaryOp('-',BinaryOp('+',Id('x'),BinaryOp('/',IntLiteral(5),IntLiteral(2))),FloatLiteral(5.2)),FloatLiteral(1.2))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,368))


#     def test_break_state_1(self):
#         input = """int main() {
#             break;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Break()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,369))

#     def test_break_state_2(self):
#         input = """int main() {
#             continue;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,370))

#     def test_break_state_3(self):
#         input = """int main() {
#             return;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,371))

#     def test_break_state_4(self):
#         input = """int main() {
#             return 2;
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(IntLiteral(2))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,372))

#     def test_break_state_5(self):
#         input = """int main() {
#             return (a+b)>(c+d);
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(BinaryOp(">",BinaryOp("+",Id("a"),Id("b")),BinaryOp("+",Id("c"),Id("d"))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,373))

#     def test_break_state_6(self):
#         input = """int main() {
#             return CallExpr("parameter");
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Return(CallExpr(Id("CallExpr"),[StringLiteral("parameter")]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,374))

#     def test_exp_state_1(self):
#         input = """int mc_function() {
#             a = a + b * c;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c"))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,375))

#     def test_exp_state_2(self):
#         input = """int mc_function() {
#             int a[10];
#             a[1] = a[0] + b * c;
#             print(a[2]);
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("a",ArrayType(10,IntType())),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(1)),BinaryOp("+",ArrayCell(Id("a"),IntLiteral(0)),BinaryOp("*",Id("b"),Id("c")))),CallExpr(Id("print"),[ArrayCell(Id("a"),IntLiteral(2))])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,376))

#     def test_exp_state_3(self):
#         input = """void foofunc(string a) {
#             print(a);
#         }
#         int mainfunc() {
#             if (!a == !b) return foofunc("Hello Python3");
#         }"""
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("a",StringType())],VoidType(),Block([CallExpr(Id("print"),[Id("a")])])),FuncDecl(Id("mainfunc"),[],IntType(),Block([If(BinaryOp("==",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),Return(CallExpr(Id("foofunc"),[StringLiteral("Hello Python3")])))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,377))

#     def test_exp_state_4(self):
#         input = """int mainfunc() {
#             boolean bool_1, bool_2;
#             bool_1 = (!bool_2 || (bool_2 && true));
#             print(bool_1);
#         }"""
#         expect = str(Program([FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("bool_1",BoolType()),VarDecl("bool_2",BoolType()),BinaryOp("=",Id("bool_1"),BinaryOp("||",UnaryOp("!",Id("bool_2")),BinaryOp("&&",Id("bool_2"),BooleanLiteral(True)))),CallExpr(Id("print"),[Id("bool_1")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,378))

#     def test_exp_state_5(self):
#         input = """int count(string arr[]){
#             return len(arr);
#         }
#         int mc_function() {
#             if (!a && !b) print(count(arr));
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("count"),[VarDecl("arr",ArrayPointerType(StringType()))],IntType(),Block([Return(CallExpr(Id("len"),[Id("arr")]))])),FuncDecl(Id("mc_function"),[],IntType(),Block([If(BinaryOp("&&",UnaryOp("!",Id("a")),UnaryOp("!",Id("b"))),CallExpr(Id("print"),[CallExpr(Id("count"),[Id("arr")])])),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,379))

#     def test_exp_state_6(self):
#         input = """int main() {
#             a = a + b * c;
#             do {} while (a);
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c")))),Dowhile([Block([])],Id("a"))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,380))

#     def test_exp_state_7(self):
#         input = """void mc_function() {
#             int a;
#             a =  CallExpr(a[b[2]]);
#             print(a);
#             return;
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],VoidType(),Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),CallExpr(Id("CallExpr"),[ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2)))])),CallExpr(Id("print"),[Id("a")]),Return()]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,381))

#     def test_exp_state_8(self):
#         input = """int[] mainfunc() {
#             string str;
#             if (str!=isempty(null)) {
#                 int a;
#                 for (a;a<10;a=a+1) print(str[a]);
#             }
#             else{
#                 break;
#             }
#         }"""
#         expect = str(Program([FuncDecl(Id("mainfunc"),[],ArrayPointerType(IntType()),Block([VarDecl("str",StringType()),If(BinaryOp("!=",Id("str"),CallExpr(Id("isempty"),[Id("null")])),Block([VarDecl("a",IntType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),CallExpr(Id("print"),[ArrayCell(Id("str"),Id("a"))]))]),Block([Break()]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,382))

#     def test_exp_state_9(self):
#         input = """int mc_function() {
#             string a,b,c;
#             a = a + b * c = foofunc(2) +b = arr[a[10]];
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType()),BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),Id("c"))),BinaryOp("=",BinaryOp("+",CallExpr(Id("foofunc"),[IntLiteral(2)]),Id("b")),ArrayCell(Id("arr"),ArrayCell(Id("a"),IntLiteral(10))))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,383))

#     def test_exp_state_10(self):
#         input = """boolean check(string a) {
#             if(!isempty(a)) return true;
#             else return false;
#         }
#         int mainfunc() {
#             int a;
#             string arr;
#             for (a;a<10;a=a+1) {
#                 do print("Hello Python3"); while (arr[a]);
#                 if(!arr[a]) break;
#             }
#             return 0;
#         }"""
#         expect = str(Program([FuncDecl(Id("check"),[VarDecl("a",StringType())],BoolType(),Block([If(UnaryOp("!",CallExpr(Id("isempty"),[Id("a")])),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),FuncDecl(Id("mainfunc"),[],IntType(),Block([VarDecl("a",IntType()),VarDecl("arr",StringType()),For(Id("a"),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([Dowhile([CallExpr(Id("print"),[StringLiteral("Hello Python3")])],ArrayCell(Id("arr"),Id("a"))),If(UnaryOp("!",ArrayCell(Id("arr"),Id("a"))),Break())])),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,384))

#     def test_exp_state_11(self):
#         input = """int mc_function () {
#             boolean a, b;
#             b = true;
#             a = !(!(!b));
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),BinaryOp("=",Id("b"),BooleanLiteral(True)),BinaryOp("=",Id("a"),UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("b")))))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,385))

#     def test_exp_state_12(self):
#         input = """boolean mc_function (boolean a){
#             if (a) return true;
#             else return false;
#         }
#         int main () {
#             print(foofunc(!foofunc(true)));
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[VarDecl("a",BoolType())],BoolType(),Block([If(Id("a"),Return(BooleanLiteral(True)),Return(BooleanLiteral(False)))])),FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("print"),[CallExpr(Id("foofunc"),[UnaryOp("!",CallExpr(Id("foofunc"),[BooleanLiteral(True)]))])])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,386))

#     def test_exp_state_13(self):
#         input = """int mc_function () {
#             return (foofunc(!(a==2)==true));
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([Return(CallExpr(Id("foofunc"),[BinaryOp("==",UnaryOp("!",BinaryOp("==",Id("a"),IntLiteral(2))),BooleanLiteral(True))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,387))

#     def test_exp_state_14(self):
#         input = """int main () {
#             float a, b, c[10];
#             a = ((b * c[0] + (b - c[1]) / c[2]) == 3);
#             print(a);
#         }"""
#         expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",ArrayType(10,FloatType())),BinaryOp("=",Id("a"),BinaryOp("==",BinaryOp("+",BinaryOp("*",Id("b"),ArrayCell(Id("c"),IntLiteral(0))),BinaryOp("/",BinaryOp("-",Id("b"),ArrayCell(Id("c"),IntLiteral(1))),ArrayCell(Id("c"),IntLiteral(2)))),IntLiteral(3))),CallExpr(Id("print"),[Id("a")])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,388))

#     def test_exp_state_15(self):
#         input = """int mc_function () {
#             boolean a, b;
#             a = -10;
#             b = -(-20);
#             print(a+b);
#         }"""
#         expect = str(Program([FuncDecl(Id("mc_function"),[],IntType(),Block([VarDecl("a",BoolType()),VarDecl("b",BoolType()),BinaryOp("=",Id("a"),UnaryOp("-",IntLiteral(10))),BinaryOp("=",Id("b"),UnaryOp("-",UnaryOp("-",IntLiteral(20)))),CallExpr(Id("print"),[BinaryOp("+",Id("a"),Id("b"))])]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,389))

#     def test_simple_program_1213(self):
#         input = """
#         int[] foofunc(float a[]){
#             return 2;
#         }
#         int main(float a[]){
#             getArray();
#             return 0;
#         }
#         """
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("a",ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([Return(IntLiteral(2))])),FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(FloatType()))],IntType(),Block([CallExpr(Id("getArray"),[]),Return(IntLiteral(0))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,390))

#     def test_simple_program_9991(self):
#         input = """
#         void main( int n)
#         {
#             for(i = 0; i < n - 1; i)
#             {
#                 if(a[i] % 2 != 0)
#                 {
#                     for(j = i + 1; j < n; j)
#                     {
#                         if(a[j] % 2 != 0 && a[i] > a[j])
#                         {
#                             foofunc(a[i], a[j]);
#                         }
#                     }

#                 }
#             }
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [VarDecl('n',IntType())],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('i'),IntLiteral(0)),
#             BinaryOp('<',Id('i'),BinaryOp('-',Id('n'),IntLiteral(1))),
#             Id('i'),
#             Block([
#             If(BinaryOp('!=',BinaryOp('%',ArrayCell(Id('a'),Id('i')),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             For(BinaryOp('=',Id('j'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             BinaryOp('<',Id('j'),Id('n')),
#             Id('j'),
#             Block([
#             If(BinaryOp('&&',BinaryOp('!=',BinaryOp('%',ArrayCell(Id('a'),Id('j')),IntLiteral(2)),IntLiteral(0)),BinaryOp('>',ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j')))),
#             Block([
#             CallExpr(Id('foofunc'),[ArrayCell(Id('a'),Id('i')),ArrayCell(Id('a'),Id('j'))])
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,391))

#     def test_simple_program_9992(self):
#         input="""
#         float main(){
#             return x + 1;
#             for ( i=1;i<5;i=i+1){
#                 if ( i==2) break;
#                 else {
#                     print(i);
#                     foofunc(i);
#                 }
#                 return foofunc(x);
#             }
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             FloatType(),
#             Block([
#             Return(BinaryOp('+',Id('x'),IntLiteral(1))),
#             For(BinaryOp('=',Id('i'),IntLiteral(1)),
#             BinaryOp('<',Id('i'),IntLiteral(5)),
#             BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('==',Id('i'),IntLiteral(2)),
#             Break(),
#             Block([
#             CallExpr(Id('print'),[Id('i')]),
#             CallExpr(Id('foofunc'),[Id('i')])
#             ])
#             ),
#             Return(CallExpr(Id('foofunc'),[Id('x')]))
#             ])
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 392))


#     def test_simple_program_993(self):
#         input="""
#         void main(){
#             for (x=2;x<5;x=x+1){
#                 if (x%2==0) {
#                     print(x);
#                     return x;
#                 }
#             }
#             print("foofunc");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[Id('x')]),
#             Return(Id('x'))
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('foofunc')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    
#     def test_simple_program_3394(self):
#         input = """
#         void main() {
#             int x; x = 0;
#             int i,j;
#             do{
#                 x= x+1;
#                 for(i = 1*x; i <= 100*x; i= i + 1){
#                     if(i%2==0 && i %3==0)
#                         print(i);
#                 }
#             }{}
#             while(x<10);
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             VoidType(),
#             Block([
#             VarDecl('x',IntType()),
#             BinaryOp('=',Id('x'),IntLiteral(0)),
#             VarDecl('i',IntType()),
#             VarDecl('j',IntType()),
#             Dowhile([Block([
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),
#             For(BinaryOp('=',Id('i'),BinaryOp('*',IntLiteral(1),Id('x'))),
#             BinaryOp('<=',Id('i'),BinaryOp('*',IntLiteral(100),Id('x'))),
#             BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),
#             Block([
#             If(BinaryOp('&&',BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(2)),IntLiteral(0)),BinaryOp('==',BinaryOp('%',Id('i'),IntLiteral(3)),IntLiteral(0))),
#             CallExpr(Id('print'),[Id('i')])
#             )
#             ])
#             )
#             ]),
#             Block([

#             ])],
#             BinaryOp('<',Id('x'),IntLiteral(10))
#             )
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input,expect,394))




#     def test_simple_program_003(self):
#         input = """
#             int x;
#         """
#         expect = str(Program([VarDecl("x",IntType())]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,395))
    
#     def test_simple_program_0009(self):
#         input = """float main() {}"""
#         expect = str(Program([FuncDecl(Id("main"),[],FloatType(),Block([]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,396))

#     def test_simple_program_0011(self):
#         input = """
#         int foofunc(int a) {
#             int b;
#             b = a;
#             print("ID = ",a);
#             return b;
#         }
#         int main() {
#             int arr[1];
#             arr[1] = foofunc(arr[0]);
#             }
#         """
#         expect = str(Program([FuncDecl(Id("foofunc"),[VarDecl("a",IntType())],IntType(),Block([VarDecl("b",IntType()),BinaryOp("=",Id("b"),Id("a")),CallExpr(Id("print"),[StringLiteral("ID = "),Id("a")]),Return(Id("b"))])),FuncDecl(Id("main"),[],IntType(),Block([VarDecl("arr",ArrayType(1,IntType())),BinaryOp("=",ArrayCell(Id("arr"),IntLiteral(1)),CallExpr(Id("foofunc"),[ArrayCell(Id("arr"),IntLiteral(0))]))]))]))
#         self.assertTrue(TestAST.checkASTGen(input,expect,397))

    
#     def test_simple_program_00112(self):
#         input="""
#         float main(){
#             for (x=2;x<5;x=x+2){
#                 if (x%2==0) {
#                     print("x la so chan");
#                     return x;
#                 }
#                 else {
#                     for (j=0; j<10;j=j+2){
#                         if(j<=x){
#                             print("j la so nho hon x");
#                         }
#                     }
#                 }
#             }
#             print("Hello my func");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             FloatType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('x la so chan')]),
#             Return(Id('x'))
#             ]),
#             Block([
#             For(BinaryOp('=',Id('j'),IntLiteral(0)),
#             BinaryOp('<',Id('j'),IntLiteral(10)),
#             BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('<=',Id('j'),Id('x')),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('j la so nho hon x')])
#             ])
#             )
#             ])
#             )
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('Hello my func')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 398))

#     def test_simple_program_00999(self):
#         input="""
#         void main(){
#             for (x=2;x<5;x=x+2){
#                 if (x%2==0) {
#                     print("x la so chan");
#                     return x;
#                 }
#             }
#             print("Hello! This is main");
#         }
#         """
#         expect = str(
#             Program([FuncDecl(Id('main'),
#             [],
#             VoidType(),
#             Block([
#             For(BinaryOp('=',Id('x'),IntLiteral(2)),
#             BinaryOp('<',Id('x'),IntLiteral(5)),
#             BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(2))),
#             Block([
#             If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(2)),IntLiteral(0)),
#             Block([
#             CallExpr(Id('print'),[StringLiteral('x la so chan')]),
#             Return(Id('x'))
#             ])
#             )
#             ])
#             ),
#             CallExpr(Id('print'),[StringLiteral('Hello! This is main')])
#             ]))
#             ])
#         )
#         self.assertTrue(TestAST.checkASTGen(input, expect, 399))