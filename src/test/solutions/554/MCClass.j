.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
	iconst_0
	istore_1
Label3:
	iconst_2
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label5:
	iconst_3
	istore_1
Label7:
	iconst_4
	istore_1
Label8:
	iload_1
	invokestatic io/putIntLn(I)V
Label6:
Label9:
	iconst_1
	istore_1
Label10:
Label4:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 11
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
