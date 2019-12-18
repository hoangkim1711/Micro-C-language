.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is b F from Label3 to Label1
Label3:
.var 3 is c Ljava/lang/String; from Label4 to Label1
Label4:
.var 4 is d Z from Label5 to Label1
Label5:
	bipush 10
	istore_1
	ldc 6.9
	fstore_2
	ldc "Hello world"
	astore_3
	iconst_1
	istore 4
	iload_1
	invokestatic io/putIntLn(I)V
	fload_2
	invokestatic io/putFloatLn(F)V
	aload_3
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload 4
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 7
.limit locals 5
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
