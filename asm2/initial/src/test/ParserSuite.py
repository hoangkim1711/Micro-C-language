import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_simple_program2(self):
        input = """int float() {}"""
        expect = "Error on line 1 col 4: float"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_simple_program3(self):
        input = """int program_test() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_simple_program4(self):
        input = """boolean i;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_simple_program5(self):
        input = """void test(int a, float b) {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_more_complex_program1(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_more_complex_program2(self):
        input = """int main () {
            null_func();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_more_complex_program3(self):
        input = """int main () {
            int a, b, c;
            a = 1;
            b = 2;
            c = a + b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_more_complex_program4(self):
        input = """int main () {
            putIntLn(4);
            string a;
            a = "asvb";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_more_complex_program5(self):
        input = """int main () {
            int i = 10;
            return 0;
        }"""
        expect = "Error on line 2 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,210))                        
    def test277(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do  a = a + 1; 
                while a < b;
                return 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211)) 
    def test278zzz(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 1000;
                do  a = a + 1; 
                    b = b - 1;
                while a < b;
                add(a,b);
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))  

    
    def test_decl_5(self):
        """error id is keyword"""
        testcase = """
        int[] true(int a[],int b[], int c){

            return a;
        }
        float x,y,int[5];
        string t;
        void main(){
            null()[a+b*-c+d] = (!a) || b && !(!c) && d || (!(!e));
            fooo(a, b, 10)[a*b%c+5] = -a% (-x[0] * -c / d - f[1]);
            yasuo[c*c*c*d/a/b/-c%-d] = -a / ((b + -c) * (c * -d)) + e;
            yasuo(5.1e-2) = -1e2 * -.1 / -f[2] * -9.0;
            f = b = c = d = -x[0] / -f[a*-b%2];
            return;
        }
        boolean m[20];
        float yasuo(float x){
            return x*-x
        }
        """
        expect = """Error on line 2 col 14: true"""
        self.assertTrue(TestParser.checkParser(testcase,expect,213))


    def test_statement_expression_2(self):
        input = """int main() {
           a=b*/c;
        }"""
        expect = "Error on line 2 col 15: /"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_simple_program_100(self):
        input = """
        void swap(int a, int b){}          
        int main()
        {
            int m;
            swap(m, n);                         
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_program_11(self):
        input = """
        // An example function that takes two parameters 'x' and 'y' 
        // as input and returns max of two input numbers 
        int max(int x, int y) 
        { 
            if (x > y) 
                return x; 
            else
                return y; 
        } 
  
        // main function that doesn't receive any parameter and 
        // returns integer. 
        int main() 
        { 
            int a = 10, b = 20; 
  
            // Calling above function to find max of 'a' and 'b' 
            int m = max(a, b); 
            return 0; 
        } 
        """
        expect = "Error on line 16 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_program_12(self):
        input = """
        {int main() {
            {a=5;}
            {}
        }}"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_program_13(self):
        input = """
        int main() {
            int i,j,arr[4];
            arr[2] = for(;;){
                        i = i + 1;
                        do {} {} break; while(true);
                        if(i>=1000) break; else continue;
                    }
        }"""
        expect = "Error on line 4 col 21: for"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_var_decl_297(self):
        input = """
            int a,b,c[2],x,y,z;
            float f,g,h;
            boolean i,j,k[12];
            string str,m[1],n[5];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_program_124(self):
        testcase = """
        void main(){
            int i;
            do{
                i=i+1;
                string _;
                float a, b,c,intt[5] ;
                d[5]=12e5;
                _ = "day la string||124&&^\\\\";
                putString(_);
                c= d[0] * d[1] - d[2];
                // /*blocasdawe*/
                /*
                    comment block
                */
                putall(c * i);
                putall("print string !\\n")
                if(i> 10) break;
            }while(true);
        }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(testcase,expect,220))
    def test_statement_expression_3(self):
        input = """
            a=b/c;
            int main() {
                a=b/c;
        }"""
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_statement_expression_4(self):
        input = """
            a=b/c;
            int main() {
                a>==c;
        }"""
        expect = "Error on line 2 col 12: a"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_statement_expression_5(self):
        input = """
            int main() {
                a=b+c>=d-e+f!=g==h; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    """Simple program test"""
    def test_program_1(self):
        input = """
            int ucln(int a, int b)
            {
                int u;
                if (a<b)
                    u=a;
                else
                    u=b;
                do{u=u-1;}
                while ((a%u !=0) || (b%u!=0));
                return u;
            } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_program_3(self):
        input = """
            int ucln(int a,int b){
                int u;
                if (a<b)
                    u=a;
                else
                    u=b;
                do{u=u-1};   //Sai do dau ';' o ben ngoai '{}'
                while ((a%u !=0) || (b%u!=0));
                return u;
            }
            """
        expect = "Error on line 8 col 24: }"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_program_4(self):
        input = """
            void printArray(){
                for (i=0;j<n;j=j++){}
                }
            """
        expect = "Error on line 3 col 30: ="
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_statement_block_9(self):
        input = """
        void Function(){{}}
        int main() {
            {a=5; {}}
            {}
            if (true) {
                {
                    for(i=1;i<10;i=i+1) b = 9;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    """Test break stmt"""
    def test_statement_break_1(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
                if (i%2 == 1) break;
            j = 10;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_statement_break_2(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
            j = j + 2;
            break;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_program_5(self):
        input = """
            int a;
            int b;
            int c;
            void printArray(int a,int m, int n){
                for (i=0; i < m ; i = i + 1){
                    for (i=0;j<n;j=j+1){
                    }
                }
            }
            int main(){ 
                printArray(a,b,c);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_program_6(self):
        input = """
            int a;
            int b;
            int c;
            printArray(int a,int m, int n){ //Sai do thieu TYPE
                for (i=0; i < m ; i = i + 1){
                    for (i=0;j<n;j=j+1){
                    }
                }
            }
            int main(){ 
                printArray(a,b,c);
            }"""
        expect = "Error on line 5 col 12: printArray"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_wrong_miss_close1(self):
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_wrong_miss_close2(self):
        input = """int main) {}"""
        expect = "Error on line 1 col 8: )"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_statement_block_6(self):
        input = """
        int main() {
            {a=5; {}}
            {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_function_decl_14(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = get();
            if (y > 10) x=!x;
            else x = x && (y > 15);
            funcall(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    
    def test_function_decl_15(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = get();
            if (y > 10)
                if ( y > 15)
                    x = !x && (y>20);
                else
                    x = x && (y >15 );
            else x = x && (y > 7);
            funccall(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))


   
    def test_statement_break_3(self):
        input = """
        string tr;
        int main() {
            int i,j;
            do break;
            while(i==1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_statement_break_4(self):
        input = """
        int main() {
            int i,j;
            for(i=1;i<10;i=i+1){
                i = i + 1;
                do {} {} break; while(true);
                for(i=1;i<10;i=i+1) a=10;
                if(i>=1000) break;
            }
            j = 100;
            return i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_wrong_miss_close3(self):
        input = """main() {}"""
        expect = "Error on line 1 col 0: main"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_wrong_miss_close4(self):
        input = """int x"""
        expect = "Error on line 1 col 5: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_wrong_miss_close5(self):
        input = """float x,y"""
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,241))       


    def test_more_program1(self):
        input = """int add(int a, int b){
            return a+b;
            }
            int main(){
                add(1,2);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_more_program2(self):
        input = """int add(int a, int b){
            return a+b;
            }
            int main(){
                int x, y;
                x = 1;
                y = 2;
                add(x, y);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_more_program3(self):
        input = """float x;
            string y;
            int main(){
                return;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_more_program4(self):
        input = """
            int main(){
                int a;
                a = 1 + 2;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_more_program5(self):
        input = """int add(int a, int b){
            int sum;
            sum = a + b;
            return sum;
            }
            int main(){
                add(1,2);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))                            

    def test_program_7(self):
        input = """
            int Fibonaci(int i) {
            if (i == 0) { return 0; }
            if(i == 1) { return 1;}
            return Fibonaci(i-1) + Fibonaci(i-2);
        }
        int  main() {
            int i;
            for (i = 0; i < 10; i=i+1) { printf("%f", Fibonaci(i)); }
            printf("===========================");
            return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_equal_exp_1(self):
        testcase = """
        void main(){
            null()[0] = (a == (b == (c != d)));
            fooo(a, b, 10)[0] = (a==((b!=c)==d));
            yasuo[4] = a != (b != (c == (d == e)));
            i = true != (false == false);
            f = b = c = d = (i == (true != !false));
            return;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(testcase,expect,248))
    
    def test_exp_1(self):
        testcase = """
        void main(){
            null()[0] = (a >= (b > (c < d)));
            fooo(a, b, 10)[0] = (a<=((b>=c)>d));
            yasuo[4] = a >= (b <= (c == (d > e)));
            i = true <= (false >= false);
            f = b = c = d = (i <= (true != !false));
            return;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(testcase,expect,249))
    def test_simple_program_10(self):
        input = """
        class c{};
        int main() {
            return 0;
        }"""
        expect = "Error on line 2 col 8: class"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    
    def test_program_1124(self):
        testcase = """
        void main(){
            int i;
            putString("nhap i:");
            i = getInt();
            int foo(){
                return 2; 
            }
            do{ i = i++;        
            }while(true);
        }
        """
        expect = 'Error on line 6 col 19: ('
        self.assertTrue(TestParser.checkParser(testcase,expect,251))

    def test_program_9999(self):
        testcase = """
            void print(string tr){}
            int main(){
                string tr;
                tr = "hello word!";
                print(str);
                return 0;
            }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(testcase,expect,252))

    def test21(self):
        input = """int arr[5];
            int main(){
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test22(self):
        input = """
            int[] main(){
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254)) 
    def test23(self):
        input = """
            int main(int a[]){
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))                  
    def test24(self):
        input = """
            void main(int arr[3]){
                }"""
        expect = "Error on line 2 col 26: arr[3]"
        self.assertTrue(TestParser.checkParser(input,expect,256)) 
    def test25(self):
        input = """
            int [4] test(){
                }"""
        expect = "Error on line 2 col 16: ["
        self.assertTrue(TestParser.checkParser(input,expect,257)) 



    def test26(self):
        input = """
            int arr[100];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258)) 
    def test27(self):
        input = """
            string arr[100];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test28(self):
        input = """
            boolean x;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test29(self):
        input = """
            int arr[100], b, c, d;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test30(self):
        input = """
            boolean a;
            float x;
            int main(){
                x = 10.2e3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))     


    def test31(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 2;
                if(a = 1) c = a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))    
    def test32(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 2;
                if(a = 1) c = a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))  
    def test33(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 2;
                if(a = 1) c = a + b;
                else c = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))  
    def test34(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do a = a + 1;
                while a < b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))  
    def test35(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do  a = a + 1; 
                    b = b - 1;
                while a < b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))  



    def test36(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do
                while a < b;
            }
        """
        expect = "Error on line 7 col 16: while"
        self.assertTrue(TestParser.checkParser(input,expect,268)) 
    def test37(self):
        input = """
            int main(){
                int i;
                i = 0;
                for (i; i = 10; i = i + 1)
                    print("hello");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269)) 
    def test38(self):
        input = """
            int main(){
                int i;
                i = 0;
                for (i; i = 10; i = i + 1)
                }
        """
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,270)) 
    def test39(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do  a = a + 1; 
                    b = b - 1;
                while a < b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271)) 
    def test40(self):
        input = """
            int main(){
                int a, b, c;
                a = 1;
                b = 20;
                do  a = a + 1; 
                    b = b - 1;
                while a < b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))   

    """Test error break"""
    def test_statement_break_5(self):
        input = """
        break;
        int main() {
        }"""
        expect = "Error on line 2 col 8: break"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_statement_break_6(self):
        input = """
        int main() {
            int i;
            for(i=0; i<=10 ; i=i+1)
            break
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_function_decl_13(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = get();
            if (y > 10) x=!x;
            funcall(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_function_decl_1422(self):
        input = """void main() {
            boolean x;
            int y;
            x = true;
            y = get();
            if (y > 10) x=!x;
            else x = x && (y > 15);
            funcall(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))


    def test_statement_continue_2(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
            continue;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_statement_continue_3(self):
        input = """
        int main() {
            int i,j;
            do continue;
            while(i==1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_statement_continue_4(self):
        input = """
        int main() {
            int i,j;
            for(i=1;i<10;i=i+1){
                i = i + 1;
                do {} {} continue; while(true);
                for(i=1;i<10;i=i+1) a=10;
                if(i>=1000) continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    """Test error continue"""
    def test_statement_continue_1(self):
        input = """
        continue;
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1){}
        }"""
        expect = "Error on line 2 col 8: continue"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_statement_continue_2123(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
            continue
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_statement_continue_312412(self):
        input = """
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
            continue i;
        }"""
        expect = "Error on line 5 col 21: i"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    """Test expression"""
    def test_statement_expression_1(self):
        input = """
        int main() {
            a=a+1;
            b=b-2;
            c=c-3;
            d=d-4;
            e=a+b-c*d/c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_block_stmt_for_3(self):
        input = """
        int a;
        int main() {
            int i;
            for(i=0;i<=10;i=i+1){
            do{x=2;}
            while x=1;
            if(x=1){x=x+1;}
            else return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_statement_for_1(self):
        input = """
        void main() {
            int i;
            for{
            x=x-1;}
        }"""
        expect = "Error on line 4 col 15: {"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_statement_for_2(self):
        input = """
        int main() {
            int i;
            for(i=0;i<=10;i=i+1)
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_statement_for_3(self):
        input = """
        int main() {
            int i,j;
            for(i=0,i<=10,i=i+1){}
        }"""
        expect = "Error on line 4 col 19: ,"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_statement_for_4(self):
        input = """
        int main() {
            int i;
            for(){}
        }"""
        expect = "Error on line 4 col 16: )"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    def test_246xx(self):
        testcase = """
            int i ;
            int f() {
                return 0;
            }
            void main() {
                int main ;
                main = f();
                putIntLn(main);
                {
                    int i ;
                    int main ;
                    int f ;
                    main = f = i = 100;
                    putIntLn( i ) ;
                    putIntLn ( main ) ;
                    putIntLn ( f ) ;
                }
                putIntLn( main ) ;
            }
        """
        expect = 'successful'
        self.assertTrue(TestParser.checkParser(testcase,expect,289))

    def test_statement_for6(self):
        input = """
        int main() {
            int i;
            for(i=0){}
        }"""
        expect = "Error on line 4 col 19: )"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_statement_for_7(self):
        input = """
        int main() {
            int i;
            for(i=0;i<=10;i=i+1;i=1){}
        }"""
        expect = "Error on line 4 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_statement_for_8(self):
        input = """
        int main() {
            int i;
            for;
        }"""
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_statement_for_9(self):
        input = """
        for(i=0;i<=10;i=i+1){}
        int main() {
            int i;
            for;
        }"""
        expect = "Error on line 2 col 8: for"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_statement_for_10(self):
        input = """
            int main(){
                int i;
                i = 0;
                for (i; i = 10; i = i + 1)
                    print("hello");
                string a, v, c;
                v = "sdf";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294)) 

    def test_statement_for_11(self):
        input = """
            int main(){
                int i;
                i = 0;
                a = 10;
                for (i; i = 10; i = i + 1)
                    a = a - i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295)) 

    def test_statement_block_1(self):
        input = """
        {a=5;}
        int main() {
            return 0;
        }"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test_statement_block_2(self):
        input = """
        int main() {
            {a=5;}
            {
                for(i=1;i<10;i=i+1) a=9;
            }
            float f;
            int a;
            a = 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_statement_block_3(self):
        input = """
        int main() {
            {a=5;}
            {
                for(i=1;i<10;i=i+1) a=10;
                int a;
            };
        }"""
        expect = "Error on line 7 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_statement_block_4(self):
        input = """
        {int main() {
            {a=5;}
            {}
        }}"""
        expect = "Error on line 2 col 8: {"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_statement_block_5(self):
        input = """
        void Function({}){}
        int main() {
        }"""
        expect = "Error on line 2 col 22: {"
        self.assertTrue(TestParser.checkParser(input,expect,300))
