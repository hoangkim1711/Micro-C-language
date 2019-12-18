.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 69
	dup
	putstatic MCClass/c I
	dup
	putstatic MCClass/b I
	putstatic MCClass/a I
	getstatic MCClass/a I
	getstatic MCClass/b I
	isub
	getstatic MCClass/c I
	bipush 10
	isub
	isub
	invokestatic io/putIntLn(I)V
	getstatic MCClass/b I
	i2f
	getstatic MCClass/a I
	i2f
	getstatic MCClass/c I
	getstatic MCClass/a I
	isub
	i2f
	ldc 100.1
	fsub
	fsub
	fsub
	invokestatic io/putFloatLn(F)V
	getstatic MCClass/a I
	i2f
	ldc 2.5
	fsub
	getstatic MCClass/c I
	i2f
	ldc 212.1
	fsub
	fsub
	getstatic MCClass/b I
	i2f
	fsub
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 9
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
