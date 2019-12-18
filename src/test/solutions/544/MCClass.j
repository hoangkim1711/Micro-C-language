.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass/a I
	ldc 1.5
	dup
	putstatic MCClass/c F
	putstatic MCClass/b F
	getstatic MCClass/a I
	bipush 10
	iconst_1
	iconst_3
	iadd
	imul
	imul
	invokestatic io/putIntLn(I)V
	getstatic MCClass/b F
	ldc 1.5
	fmul
	bipush 20
	bipush 40
	imul
	i2f
	fmul
	invokestatic io/putFloatLn(F)V
	getstatic MCClass/a I
	i2f
	ldc 2.5
	fmul
	getstatic MCClass/c F
	ldc 2.1
	fsub
	fmul
	getstatic MCClass/b F
	fmul
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 12
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
