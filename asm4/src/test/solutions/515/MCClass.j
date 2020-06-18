.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_0
	ior
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_1
	ior
	iconst_1
	ior
	invokestatic io/putBoolLn(Z)V
	iconst_0
	iconst_0
	iconst_1
	ior
	ior
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 11
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
