import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme("059907","059907,<EOF>",101))
    def test_error_int(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",102))
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("1.9abc","1.9,abc,<EOF>",103))
    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("1.null","1.,null,<EOF>",104))
    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme(".1ijk",".1,ijk,<EOF>",105))
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("9.1acs","9.1,acs,<EOF>",106))

    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("1e11abc","1e11,abc,<EOF>",107))
    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("1.E9def","1.E9,def,<EOF>",108))
    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme(".1e6ijk",".1e6,ijk,<EOF>",109))
    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("0.12E9xyz","0.12E9,xyz,<EOF>",110))

    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("1e-99abc","1e-99,abc,<EOF>",111))
    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("1.E-9def","1.E-9,def,<EOF>",112))
    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme(".1E-9ijk",".1E-9,ijk,<EOF>",113))
    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme("0.1299E-2xyz","0.1299E-2,xyz,<EOF>",114))

    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme("e-18","e,-,18,<EOF>",115))
    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme("e19","e19,<EOF>",116))
    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("123e","123,e,<EOF>",117))
    
    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("1+1=2","1,+,1,=,2,<EOF>",118))
    def test_operator_2(self):
        self.assertTrue(TestLexer.checkLexeme("(2*2)= 4","(,2,*,2,),=,4,<EOF>",119))
    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("4+1=5","4,+,1,=,5,<EOF>",120))
    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("5 ngon tay sach deu","5,ngon,tay,sach,deu,<EOF>",121))

    def test_separator(self):
        self.assertTrue(TestLexer.checkLexeme("{y x [b x c (f x e)]}","{,y,x,[,b,x,c,(,f,x,e,),],},<EOF>",122))
    def test_separator2(self):
        self.assertTrue(TestLexer.checkLexeme("XX,XX dep trai,XX sieu dep trai;","XX,,,XX,dep,trai,,,XX,sieu,dep,trai,;,<EOF>",123))

    def test_compare_op1(self):
        self.assertTrue(TestLexer.checkLexeme("x<y>z","x,<,y,>,z,<EOF>",124))
    def test_compare_op2(self):
        self.assertTrue(TestLexer.checkLexeme("!(q==w)","!,(,q,==,w,),<EOF>",125))
    def test_compare_op3(self):
        self.assertTrue(TestLexer.checkLexeme("q>=w<=e","q,>=,w,<=,e,<EOF>",126))
    def test_compare_op4(self):
        self.assertTrue(TestLexer.checkLexeme("i=<o","i,=,<,o,<EOF>",127))
    def test_compare_op5(self):
        self.assertTrue(TestLexer.checkLexeme("d=>f","d,=,>,f,<EOF>",128))

    def test_logic_op1(self):
        self.assertTrue(TestLexer.checkLexeme("x||y||z","x,||,y,||,z,<EOF>",129))
    def test_logic_op2(self):
        self.assertTrue(TestLexer.checkLexeme("a=b!=c","a,=,b,!=,c,<EOF>",130))
    def test_logic_op3(self):
        self.assertTrue(TestLexer.checkLexeme("x=y=z=t=1","x,=,y,=,z,=,t,=,1,<EOF>",131))
    
    def test_comment_block1(self):
        self.assertTrue(TestLexer.checkLexeme("/*qwer","/,*,qwer,<EOF>",132))
    def test_comment_block2(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*123qwe","/,*,/,*,123,qwe,<EOF>",133))
    def test_comment_block3(self):
        self.assertTrue(TestLexer.checkLexeme("/**/123qwe","123,qwe,<EOF>",134))
    def test_comment_block4(self):
        self.assertTrue(TestLexer.checkLexeme("/*123qwe*/","<EOF>",135))
    def test_comment_block5(self):
        self.assertTrue(TestLexer.checkLexeme("/123qwe**/","/,123,qwe,*,*,/,<EOF>",136))
    def test_comment_block6(self):
        self.assertTrue(TestLexer.checkLexeme("/123dfg**/","/,123,dfg,*,*,/,<EOF>",137))
    def test_comment_block7(self):
        self.assertTrue(TestLexer.checkLexeme("/*werthgfdawergsh*/","<EOF>",138))
    def test_comment_block8(self):
        self.assertTrue(TestLexer.checkLexeme("/*dfb1241543rdsaff@#$@#@!%DFFVSD*/","<EOF>",139))
    def test_comment_block9(self):
        self.assertTrue(TestLexer.checkLexeme("/*7893ewdgfn2abc*/*/","*,/,<EOF>",140))
    def test_comment_block10(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*av3243bc*//*1dsdf3**/*/","*,/,<EOF>",141))

    def test_comment_block11(self):
        self.assertTrue(TestLexer.checkLexeme("/*/*153451/*qwewq*/","<EOF>",142))
    def test_comment_block12(self):
        self.assertTrue(TestLexer.checkLexeme("/*235d/*1c23*/xyz/**/","xyz,<EOF>",143))

    def test_comment_line1(self):
        self.assertTrue(TestLexer.checkLexeme("///////abc//xyz","<EOF>",144))
    def test_comment_line2(self):
        self.assertTrue(TestLexer.checkLexeme("/abc//$//%//abc//xyz","/,abc,<EOF>",145))

    def test_comment_line3(self):
        self.assertTrue(TestLexer.checkLexeme("//abc1234","<EOF>",146))
    def test_comment_line4(self):
        self.assertTrue(TestLexer.checkLexeme("/1234/abcd","/,1234,/,abcd,<EOF>",147))
    
    def test_comment_block13(self):
        self.assertTrue(TestLexer.checkLexeme("/*//123/4/abcas*/","<EOF>",148))
    def test_comment_block14(self):
        self.assertTrue(TestLexer.checkLexeme("/*//123/4*///abcas*/","<EOF>",149))

    def test_comment_line5(self):
        self.assertTrue(TestLexer.checkLexeme("///*abeeeec*/","<EOF>",150))
    def test_comment_line6(self):
        self.assertTrue(TestLexer.checkLexeme("/axxbc*//**///*aqwebc*/","/,axxbc,*,<EOF>",151))

    def test_mix_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "/*qwe123*/" ""","""/*qwe123*/,<EOF>""",152))
    def test_mix_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "//qwe123" ""","""//qwe123,<EOF>""",153))
    def test_mix_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "1.5E2abc" ""","""1.5E2abc,<EOF>""",154))
    def test_mix_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "nothing@hcmut.edu.vn" ""","""nothing@hcmut.edu.vn,<EOF>""",155))
    def test_mix_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Python3""Antlr4" ""","""Python3,Antlr4,<EOF>""",156))
    def test_mix_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Java"And"Cplusplus" ""","""Java,And,Cplusplus,<EOF>""",157))
    def test_mix_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "php" ""","""123,php,<EOF>""",158))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Day la mot string" ""","""Day la mot string,<EOF>""",159))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "qwe\n123" ""","""Unclosed String: qwe""",160))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123x\\n123" ""","""123x\\n123,<EOF>""",161))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123x\\t123" ""","""123x\\t123,<EOF>""",162))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123x\\r123" ""","""123x\\r123,<EOF>""",163))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123x\\b123" ""","""123x\\b123,<EOF>""",164))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123x\\f123" ""","""123x\\f123,<EOF>""",165))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123b\\"123" ""","""123b\\"123,<EOF>""",166))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123w\\\\123" ""","""123w\\\\123,<EOF>""",167))


    def test_unclose_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123stringhihi ""","""Unclosed String: 123stringhihi """,168))
    def test_unclose_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "123qwe?? ""","""Unclosed String: 123qwe?? """,169))
    def test_unclose_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "qwe ""","""123,Unclosed String: qwe """,170))
    def test_unclose_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "/*123*/qwe ""","""Unclosed String: /*123*/qwe """,171))
    def test_unclose_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "//123c\\n123 ""","""Unclosed String: //123c\\n123 """,172))
    def test_unclose_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" qwe "hihi\n ,""","""qwe,Unclosed String: hihi""",173))
    def test_unclose_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" " ""","""Unclosed String:  """,174))

    def test_error_token1(self):
        self.assertTrue(TestLexer.checkLexeme("abc?123","abc,Error Token ?",175))
    def test_error_token2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "$100" $100""","$100,Error Token $",176))
    def test_error_token3(self):
        self.assertTrue(TestLexer.checkLexeme("/*qwe#123*/#qwe","Error Token #",177))
    def test_error_token4(self):
        self.assertTrue(TestLexer.checkLexeme("//*qwe#qwe*/#qwe","<EOF>",178))

    def test_mix_error1(self):
        self.assertTrue(TestLexer.checkLexeme(""" qwe^ "qwe ""","""qwe,Error Token ^""",179))
    def test_mix_error2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "qwe\\k $100 ""","""Illegal Escape In String: qwe\\k""",180))

    def test_illegal_escape(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\m456" ""","""123,Illegal Escape In String: 123a\\m""",181))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 123 "123a\\n\\m456" ""","""123,Illegal Escape In String: 123a\\n\\m""",182))

    def test_indent(self):
        self.assertTrue(TestLexer.checkLexeme("1void23","1,void23,<EOF>",183))
    
    def test_program1(self):
        self.assertTrue(TestLexer.checkLexeme("int main() {}","int,main,(,),{,},<EOF>",184))

    def test_program2(self):
        test = """ 
        <?php
            $name = "Hello Kim";
            echo $name;
        ?>
        """
        result = """<,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(test,result,185))
    def test_program3(self):
        test = """ 
        <!DOCTYPE html>
        <head>
            <title>Hello Kim</title>
        </head>
        """
        result = """<,!,DOCTYPE,html,>,<,head,>,<,title,>,Hello,Kim,<,/,title,>,<,/,head,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,186))

    def test_program4(self):
        test = """ 
        private class Hello{
            public static void main(String []args){
                System.out.println("Hello Kim");
            }
        }
        """
        result = """private,class,Hello,{,public,static,void,main,(,String,[,],args,),{,System,.,out,.,println,(,Hello Kim,),;,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,187))
    def test_program5(self):
        test = """ 
        <script>
            alert("Hello Kim");
        </script>
        """
        result = """<,script,>,alert,(,Hello Kim,),;,<,/,script,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,188))
    def test_program6(self):
        test = """ 
        #include<iostream>
        """
        result = """Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(test,result,189))
    def test_program7(self):
        test = """ 
        using namespace std;
        int main(){
            cout << "Hello word !!!";
            return 0;
        }
        """
        result = """using,namespace,std,;,int,main,(,),{,cout,<,<,Hello word !!!,;,return,0,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,190))
    def test_program8(self):
        test = """ 
        var m = "Hello word";
        console.log(m);
        """
        result = """var,m,=,Hello word,;,console,.,log,(,m,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,191))
    def test_program9(self):
        test = """ 
        package main
        import "fmt"
        func main(){
            fmt.Printf("Hello word")
        }
        """
        result = """package,main,import,fmt,func,main,(,),{,fmt,.,Printf,(,Hello word,),},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,192))
    def test_program10(self):
        test = """ 
        int main () {
        int a, b, c;
        a = 1;
        }
        """
        result = """int,main,(,),{,int,a,,,b,,,c,;,a,=,1,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,193))
    def test_program11(self):
        test = """ 
        void Function({}){}
        int main() {
            {a=5;}
            {}
        }
        """
        result = """void,Function,(,{,},),{,},int,main,(,),{,{,a,=,5,;,},{,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,194))
    def test_program12(self):
        test = """ 
        void main() {
            boolean x;
            int y;
            x = true;
            y = getInt();
            if (y > 10) x=!x;
            else x = x && (y > 15);
            putBoolLn(x);
        }
        """
        result = """void,main,(,),{,boolean,x,;,int,y,;,x,=,true,;,y,=,getInt,(,),;,if,(,y,>,10,),x,=,!,x,;,else,x,=,x,&&,(,y,>,15,),;,putBoolLn,(,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,195))
    def test_program13(self):
        test = """ 
        void main() {
            boolean x;
            int y;
            x = true;
            y = getInt();
            if (y > 10)
                if ( y > 15)
                    x = !x && (y>20);
                else
                    x = x && (y >15 );
            else x = x && (y > 7);
            putBoolLn(x);
        }
        """
        result = """void,main,(,),{,boolean,x,;,int,y,;,x,=,true,;,y,=,getInt,(,),;,if,(,y,>,10,),if,(,y,>,15,),x,=,!,x,&&,(,y,>,20,),;,else,x,=,x,&&,(,y,>,15,),;,else,x,=,x,&&,(,y,>,7,),;,putBoolLn,(,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,196))
    def test_program14(self):
        test = """ 
        void Dog_Function(){{}}
        int main() {
            {a=5; {}}
            {}
            if (true) {
                {
                    for(i=1;i<10;i=i+1) b = 10;
                }
            }
        }
        """
        result = """void,Dog_Function,(,),{,{,},},int,main,(,),{,{,a,=,5,;,{,},},{,},if,(,true,),{,{,for,(,i,=,1,;,i,<,10,;,i,=,i,+,1,),b,=,10,;,},},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,197))
    def test_program15(self):
        test = """ 
        int main() {
            int i,j;
            do break;
            while(i==1);
        }
        """
        result = """int,main,(,),{,int,i,,,j,;,do,break,;,while,(,i,==,1,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,198))
    def test_program16(self):
        test = """ 
        int main() {
            int i,j;
            for(i=1;i<10;i=i+1){
                i = i + 1;
                do {} {} break; while(true);
                for(i=1;i<10;i=i+1) a=10;
                if(i>=1000) break;
            }
        }
        """
        result = """int,main,(,),{,int,i,,,j,;,for,(,i,=,1,;,i,<,10,;,i,=,i,+,1,),{,i,=,i,+,1,;,do,{,},{,},break,;,while,(,true,),;,for,(,i,=,1,;,i,<,10,;,i,=,i,+,1,),a,=,10,;,if,(,i,>=,1000,),break,;,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,199))
    def test_program17(self):
        test = """ 
        int main() {
            int i,j;
            for(i=0; i<=10 ; i=i+1)
            break
        }
        """
        result = """int,main,(,),{,int,i,,,j,;,for,(,i,=,0,;,i,<=,10,;,i,=,i,+,1,),break,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(test,result,200))
