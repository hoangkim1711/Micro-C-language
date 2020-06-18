# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01b0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\6\2\177\n\2\r\2\16\2\u0080")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\7\4\u008a\n\4\f\4\16\4\u008d")
        buf.write("\13\4\3\4\3\4\3\4\3\4\7\4\u0093\n\4\f\4\16\4\u0096\13")
        buf.write("\4\3\4\3\4\3\4\7\4\u009b\n\4\f\4\16\4\u009e\13\4\3\4\3")
        buf.write("\4\5\4\u00a2\n\4\3\5\3\5\3\5\7\5\u00a7\n\5\f\5\16\5\u00aa")
        buf.write("\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00b4\n\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\5\b\u00bc\n\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d5\n\17\3")
        buf.write("\20\3\20\3\20\3\20\7\20\u00db\n\20\f\20\16\20\u00de\13")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u00e4\n\20\f\20\16\20\u00e7")
        buf.write("\13\20\3\20\3\20\5\20\u00eb\n\20\3\20\3\20\3\21\6\21\u00f0")
        buf.write("\n\21\r\21\16\21\u00f1\3\22\3\22\3\22\7\22\u00f7\n\22")
        buf.write("\f\22\16\22\u00fa\13\22\3\22\5\22\u00fd\n\22\3\22\3\22")
        buf.write("\3\22\5\22\u0102\n\22\3\22\3\22\3\22\5\22\u0107\n\22\3")
        buf.write("\23\3\23\5\23\u010b\n\23\3\23\3\23\3\24\3\24\5\24\u0111")
        buf.write("\n\24\3\25\3\25\3\25\7\25\u0116\n\25\f\25\16\25\u0119")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3&\3&\7&\u0176\n&\f&\16&\u0179\13&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3\u00e5\2?\3\3\5")
        buf.write("\4\7\5\t\6\13\2\r\2\17\7\21\b\23\t\25\n\27\13\31\f\33")
        buf.write("\r\35\16\37\17!\20#\21%\2\'\22)\23+\2-\24/\25\61\26\63")
        buf.write("\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q")
        buf.write("&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u")
        buf.write("8w9y:{;\3\2\17\4\2\n\f\16\17\b\2%&AB^^``bb\u0080\u0080")
        buf.write("\3\2$$\4\2\f\f\17\17\7\2$$))^^ddhh\3\2pp\4\2$$^^\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\2\u01c9\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3~\3\2\2\2\5\u0084\3")
        buf.write("\2\2\2\7\u00a1\3\2\2\2\t\u00a3\3\2\2\2\13\u00b3\3\2\2")
        buf.write("\2\r\u00b5\3\2\2\2\17\u00bb\3\2\2\2\21\u00bd\3\2\2\2\23")
        buf.write("\u00bf\3\2\2\2\25\u00c1\3\2\2\2\27\u00c3\3\2\2\2\31\u00c5")
        buf.write("\3\2\2\2\33\u00c7\3\2\2\2\35\u00cc\3\2\2\2\37\u00ea\3")
        buf.write("\2\2\2!\u00ef\3\2\2\2#\u0106\3\2\2\2%\u0108\3\2\2\2\'")
        buf.write("\u0110\3\2\2\2)\u0112\3\2\2\2+\u011c\3\2\2\2-\u011f\3")
        buf.write("\2\2\2/\u0127\3\2\2\2\61\u012d\3\2\2\2\63\u0136\3\2\2")
        buf.write("\2\65\u013b\3\2\2\2\67\u013f\3\2\2\29\u0145\3\2\2\2;\u0148")
        buf.write("\3\2\2\2=\u014c\3\2\2\2?\u0153\3\2\2\2A\u0158\3\2\2\2")
        buf.write("C\u015b\3\2\2\2E\u0161\3\2\2\2G\u0166\3\2\2\2I\u016c\3")
        buf.write("\2\2\2K\u0173\3\2\2\2M\u017a\3\2\2\2O\u017c\3\2\2\2Q\u017e")
        buf.write("\3\2\2\2S\u0180\3\2\2\2U\u0182\3\2\2\2W\u0184\3\2\2\2")
        buf.write("Y\u0186\3\2\2\2[\u0189\3\2\2\2]\u018c\3\2\2\2_\u018f\3")
        buf.write("\2\2\2a\u0192\3\2\2\2c\u0194\3\2\2\2e\u0196\3\2\2\2g\u0199")
        buf.write("\3\2\2\2i\u019c\3\2\2\2k\u019e\3\2\2\2m\u01a0\3\2\2\2")
        buf.write("o\u01a2\3\2\2\2q\u01a4\3\2\2\2s\u01a6\3\2\2\2u\u01a8\3")
        buf.write("\2\2\2w\u01aa\3\2\2\2y\u01ac\3\2\2\2{\u01ae\3\2\2\2}\177")
        buf.write("\t\2\2\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\b\2\2\2")
        buf.write("\u0083\4\3\2\2\2\u0084\u0085\t\3\2\2\u0085\6\3\2\2\2\u0086")
        buf.write("\u008b\7$\2\2\u0087\u008a\5+\26\2\u0088\u008a\5\r\7\2")
        buf.write("\u0089\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\u008d\3")
        buf.write("\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u00a2\n\4\2\2\u008f")
        buf.write("\u0094\7$\2\2\u0090\u0093\5+\26\2\u0091\u0093\5\r\7\2")
        buf.write("\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3")
        buf.write("\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097")
        buf.write("\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u009c\t\5\2\2\u0098")
        buf.write("\u009b\5+\26\2\u0099\u009b\5\r\7\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a\3")
        buf.write("\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009f\u00a2\7$\2\2\u00a0\u00a2\7$\2\2\u00a1\u0086")
        buf.write("\3\2\2\2\u00a1\u008f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\b\3\2\2\2\u00a3\u00a8\7$\2\2\u00a4\u00a7\5\r\7\2\u00a5")
        buf.write("\u00a7\5+\26\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3\2\2\2\u00ab\u00ac")
        buf.write("\5\13\6\2\u00ac\n\3\2\2\2\u00ad\u00ae\7^\2\2\u00ae\u00b4")
        buf.write("\n\6\2\2\u00af\u00b0\7^\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7^\2\2\u00b2\u00b4\n\7\2\2\u00b3\u00ad\3\2\2\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\n\b\2\2\u00b6")
        buf.write("\16\3\2\2\2\u00b7\u00bc\5\23\n\2\u00b8\u00bc\5\25\13\2")
        buf.write("\u00b9\u00bc\5\27\f\2\u00ba\u00bc\5\31\r\2\u00bb\u00b7")
        buf.write("\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\20\3\2\2\2\u00bd\u00be\5? \2\u00be")
        buf.write("\22\3\2\2\2\u00bf\u00c0\5-\27\2\u00c0\24\3\2\2\2\u00c1")
        buf.write("\u00c2\5;\36\2\u00c2\26\3\2\2\2\u00c3\u00c4\5\67\34\2")
        buf.write("\u00c4\30\3\2\2\2\u00c5\u00c6\5I%\2\u00c6\32\3\2\2\2\u00c7")
        buf.write("\u00c8\5K&\2\u00c8\u00c9\5k\66\2\u00c9\u00ca\5!\21\2\u00ca")
        buf.write("\u00cb\5m\67\2\u00cb\34\3\2\2\2\u00cc\u00d4\5\17\b\2\u00cd")
        buf.write("\u00ce\5K&\2\u00ce\u00cf\5k\66\2\u00cf\u00d0\5m\67\2\u00d0")
        buf.write("\u00d5\3\2\2\2\u00d1\u00d2\5k\66\2\u00d2\u00d3\5m\67\2")
        buf.write("\u00d3\u00d5\3\2\2\2\u00d4\u00cd\3\2\2\2\u00d4\u00d1\3")
        buf.write("\2\2\2\u00d5\36\3\2\2\2\u00d6\u00d7\7\61\2\2\u00d7\u00d8")
        buf.write("\7\61\2\2\u00d8\u00dc\3\2\2\2\u00d9\u00db\n\5\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00eb\3\2\2\2\u00de\u00dc\3")
        buf.write("\2\2\2\u00df\u00e0\7\61\2\2\u00e0\u00e1\7,\2\2\u00e1\u00e5")
        buf.write("\3\2\2\2\u00e2\u00e4\13\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e7\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2")
        buf.write("\u00e6\u00e8\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\7")
        buf.write(",\2\2\u00e9\u00eb\7\61\2\2\u00ea\u00d6\3\2\2\2\u00ea\u00df")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\b\20\2\2\u00ed")
        buf.write(" \3\2\2\2\u00ee\u00f0\t\t\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2")
        buf.write("\u00f2\"\3\2\2\2\u00f3\u00f4\5!\21\2\u00f4\u00f8\7\60")
        buf.write("\2\2\u00f5\u00f7\t\t\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa")
        buf.write("\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fd\5%\23\2")
        buf.write("\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u0107\3")
        buf.write("\2\2\2\u00fe\u00ff\7\60\2\2\u00ff\u0101\5!\21\2\u0100")
        buf.write("\u0102\5%\23\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0107\3\2\2\2\u0103\u0104\5!\21\2\u0104\u0105\5")
        buf.write("%\23\2\u0105\u0107\3\2\2\2\u0106\u00f3\3\2\2\2\u0106\u00fe")
        buf.write("\3\2\2\2\u0106\u0103\3\2\2\2\u0107$\3\2\2\2\u0108\u010a")
        buf.write("\t\n\2\2\u0109\u010b\t\13\2\2\u010a\u0109\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\5!\21\2")
        buf.write("\u010d&\3\2\2\2\u010e\u0111\5E#\2\u010f\u0111\5G$\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111(\3\2\2\2\u0112")
        buf.write("\u0117\7$\2\2\u0113\u0116\5+\26\2\u0114\u0116\n\b\2\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116\u0119\3")
        buf.write("\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7$\2\2\u011b")
        buf.write("*\3\2\2\2\u011c\u011d\7^\2\2\u011d\u011e\t\f\2\2\u011e")
        buf.write(",\3\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7q\2\2\u0121")
        buf.write("\u0122\7q\2\2\u0122\u0123\7n\2\2\u0123\u0124\7g\2\2\u0124")
        buf.write("\u0125\7c\2\2\u0125\u0126\7p\2\2\u0126.\3\2\2\2\u0127")
        buf.write("\u0128\7d\2\2\u0128\u0129\7t\2\2\u0129\u012a\7g\2\2\u012a")
        buf.write("\u012b\7c\2\2\u012b\u012c\7m\2\2\u012c\60\3\2\2\2\u012d")
        buf.write("\u012e\7e\2\2\u012e\u012f\7q\2\2\u012f\u0130\7p\2\2\u0130")
        buf.write("\u0131\7v\2\2\u0131\u0132\7k\2\2\u0132\u0133\7p\2\2\u0133")
        buf.write("\u0134\7w\2\2\u0134\u0135\7g\2\2\u0135\62\3\2\2\2\u0136")
        buf.write("\u0137\7g\2\2\u0137\u0138\7n\2\2\u0138\u0139\7u\2\2\u0139")
        buf.write("\u013a\7g\2\2\u013a\64\3\2\2\2\u013b\u013c\7h\2\2\u013c")
        buf.write("\u013d\7q\2\2\u013d\u013e\7t\2\2\u013e\66\3\2\2\2\u013f")
        buf.write("\u0140\7h\2\2\u0140\u0141\7n\2\2\u0141\u0142\7q\2\2\u0142")
        buf.write("\u0143\7c\2\2\u0143\u0144\7v\2\2\u01448\3\2\2\2\u0145")
        buf.write("\u0146\7k\2\2\u0146\u0147\7h\2\2\u0147:\3\2\2\2\u0148")
        buf.write("\u0149\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b\7v\2\2\u014b")
        buf.write("<\3\2\2\2\u014c\u014d\7t\2\2\u014d\u014e\7g\2\2\u014e")
        buf.write("\u014f\7v\2\2\u014f\u0150\7w\2\2\u0150\u0151\7t\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152>\3\2\2\2\u0153\u0154\7x\2\2\u0154")
        buf.write("\u0155\7q\2\2\u0155\u0156\7k\2\2\u0156\u0157\7f\2\2\u0157")
        buf.write("@\3\2\2\2\u0158\u0159\7f\2\2\u0159\u015a\7q\2\2\u015a")
        buf.write("B\3\2\2\2\u015b\u015c\7y\2\2\u015c\u015d\7j\2\2\u015d")
        buf.write("\u015e\7k\2\2\u015e\u015f\7n\2\2\u015f\u0160\7g\2\2\u0160")
        buf.write("D\3\2\2\2\u0161\u0162\7v\2\2\u0162\u0163\7t\2\2\u0163")
        buf.write("\u0164\7w\2\2\u0164\u0165\7g\2\2\u0165F\3\2\2\2\u0166")
        buf.write("\u0167\7h\2\2\u0167\u0168\7c\2\2\u0168\u0169\7n\2\2\u0169")
        buf.write("\u016a\7u\2\2\u016a\u016b\7g\2\2\u016bH\3\2\2\2\u016c")
        buf.write("\u016d\7u\2\2\u016d\u016e\7v\2\2\u016e\u016f\7t\2\2\u016f")
        buf.write("\u0170\7k\2\2\u0170\u0171\7p\2\2\u0171\u0172\7i\2\2\u0172")
        buf.write("J\3\2\2\2\u0173\u0177\t\r\2\2\u0174\u0176\t\16\2\2\u0175")
        buf.write("\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178L\3\2\2\2\u0179\u0177\3\2\2")
        buf.write("\2\u017a\u017b\7-\2\2\u017bN\3\2\2\2\u017c\u017d\7/\2")
        buf.write("\2\u017dP\3\2\2\2\u017e\u017f\7,\2\2\u017fR\3\2\2\2\u0180")
        buf.write("\u0181\7\61\2\2\u0181T\3\2\2\2\u0182\u0183\7#\2\2\u0183")
        buf.write("V\3\2\2\2\u0184\u0185\7\'\2\2\u0185X\3\2\2\2\u0186\u0187")
        buf.write("\7~\2\2\u0187\u0188\7~\2\2\u0188Z\3\2\2\2\u0189\u018a")
        buf.write("\7(\2\2\u018a\u018b\7(\2\2\u018b\\\3\2\2\2\u018c\u018d")
        buf.write("\7#\2\2\u018d\u018e\7?\2\2\u018e^\3\2\2\2\u018f\u0190")
        buf.write("\7?\2\2\u0190\u0191\7?\2\2\u0191`\3\2\2\2\u0192\u0193")
        buf.write("\7>\2\2\u0193b\3\2\2\2\u0194\u0195\7@\2\2\u0195d\3\2\2")
        buf.write("\2\u0196\u0197\7>\2\2\u0197\u0198\7?\2\2\u0198f\3\2\2")
        buf.write("\2\u0199\u019a\7@\2\2\u019a\u019b\7?\2\2\u019bh\3\2\2")
        buf.write("\2\u019c\u019d\7?\2\2\u019dj\3\2\2\2\u019e\u019f\7]\2")
        buf.write("\2\u019fl\3\2\2\2\u01a0\u01a1\7_\2\2\u01a1n\3\2\2\2\u01a2")
        buf.write("\u01a3\7}\2\2\u01a3p\3\2\2\2\u01a4\u01a5\7\177\2\2\u01a5")
        buf.write("r\3\2\2\2\u01a6\u01a7\7*\2\2\u01a7t\3\2\2\2\u01a8\u01a9")
        buf.write("\7+\2\2\u01a9v\3\2\2\2\u01aa\u01ab\7=\2\2\u01abx\3\2\2")
        buf.write("\2\u01ac\u01ad\7.\2\2\u01adz\3\2\2\2\u01ae\u01af\7\60")
        buf.write("\2\2\u01af|\3\2\2\2\35\2\u0080\u0089\u008b\u0092\u0094")
        buf.write("\u009a\u009c\u00a1\u00a6\u00a8\u00b3\u00bb\u00d4\u00dc")
        buf.write("\u00e5\u00ea\u00f1\u00f8\u00fc\u0101\u0106\u010a\u0110")
        buf.write("\u0115\u0117\u0177\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ERROR_CHAR = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4
    PRIM_TYPE = 5
    VOIDTYPE = 6
    BOOLEAN_TYPE = 7
    INTTYPE = 8
    FLOAT_TYPE = 9
    STRING_TYPE = 10
    ARRAY_TYPE = 11
    ARRAY_POINTER_TYPE = 12
    COMMENT = 13
    INTLIT = 14
    FLOATLIT = 15
    BOOLEANLIT = 16
    STRINGLIT = 17
    BOOLEAN = 18
    BREAK = 19
    CONTINUE = 20
    ELSE = 21
    FOR = 22
    FLOAT = 23
    IF = 24
    INT = 25
    RETURN = 26
    VOID = 27
    DO = 28
    WHILE = 29
    TRUE = 30
    FALSE = 31
    STRING = 32
    ID = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    NOT = 38
    MOD = 39
    OR = 40
    AND = 41
    NOT_EQUAL = 42
    EQUAL = 43
    LESS_THAN = 44
    GREAT_THAN = 45
    LESS_EQ = 46
    GREAT_EQ = 47
    ASSIGN = 48
    LSB = 49
    RSB = 50
    LP = 51
    RP = 52
    LB = 53
    RB = 54
    SEMI = 55
    COMA = 56
    DOT = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'continue'", "'else'", "'for'", "'float'", 
            "'if'", "'int'", "'return'", "'void'", "'do'", "'while'", "'true'", 
            "'false'", "'string'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", 
            "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
            "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "','", 
            "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "PRIM_TYPE", 
            "VOIDTYPE", "BOOLEAN_TYPE", "INTTYPE", "FLOAT_TYPE", "STRING_TYPE", 
            "ARRAY_TYPE", "ARRAY_POINTER_TYPE", "COMMENT", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "BOOLEAN", "BREAK", "CONTINUE", "ELSE", 
            "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", "WHILE", 
            "TRUE", "FALSE", "STRING", "ID", "ADD", "SUB", "MUL", "DIV", 
            "NOT", "MOD", "OR", "AND", "NOT_EQUAL", "EQUAL", "LESS_THAN", 
            "GREAT_THAN", "LESS_EQ", "GREAT_EQ", "ASSIGN", "LSB", "RSB", 
            "LP", "RP", "LB", "RB", "SEMI", "COMA", "DOT" ]

    ruleNames = [ "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "NOT_ESC_SEQ", "STR_CHAR", "PRIM_TYPE", "VOIDTYPE", "BOOLEAN_TYPE", 
                  "INTTYPE", "FLOAT_TYPE", "STRING_TYPE", "ARRAY_TYPE", 
                  "ARRAY_POINTER_TYPE", "COMMENT", "INTLIT", "FLOATLIT", 
                  "EXPONENT", "BOOLEANLIT", "STRINGLIT", "ESC_SEQ", "BOOLEAN", 
                  "BREAK", "CONTINUE", "ELSE", "FOR", "FLOAT", "IF", "INT", 
                  "RETURN", "VOID", "DO", "WHILE", "TRUE", "FALSE", "STRING", 
                  "ID", "ADD", "SUB", "MUL", "DIV", "NOT", "MOD", "OR", 
                  "AND", "NOT_EQUAL", "EQUAL", "LESS_THAN", "GREAT_THAN", 
                  "LESS_EQ", "GREAT_EQ", "ASSIGN", "LSB", "RSB", "LP", "RP", 
                  "LB", "RB", "SEMI", "COMA", "DOT" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            result.text = result.text[1:]
            for i in range(len(result.text)):
                if result.text[i] == '\n' or result.text[i] == '\r':
                    result.text = result.text[0:i]
                    break
            raise UncloseString(result.text);
        elif tk == self.STRINGLIT:
            result = super().emit();
            result.text = result.text[1:-1]
            return result
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            result.text = result.text[1:]
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


