.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Z
.field static c Ljava/lang/String;
.field static d F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass/a I
	iconst_1
	putstatic MCClass/b Z
	ldc "Hello world"
	putstatic MCClass/c Ljava/lang/String;
	ldc 1.2
	putstatic MCClass/d F
	getstatic MCClass/a I
	invokestatic io/putIntLn(I)V
	getstatic MCClass/b Z
	invokestatic io/putBoolLn(Z)V
	getstatic MCClass/c Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MCClass/d F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 7
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
