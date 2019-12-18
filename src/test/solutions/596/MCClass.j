.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass/a I
Label2:
.var 1 is a I from Label2 to Label3
	bipush 6
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label3:
Label4:
.var 1 is a F from Label4 to Label5
	iconst_1
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
Label5:
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
