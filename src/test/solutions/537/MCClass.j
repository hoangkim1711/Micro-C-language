.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	iconst_2
	idiv
	invokestatic io/putIntLn(I)V
	ldc 3.6
	ldc 1.2
	fdiv
	invokestatic io/putFloatLn(F)V
	ldc 6.4
	iconst_4
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 5
.limit locals 1
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
