.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass/a I
Label2:
	iconst_2
	putstatic MCClass/a I
	getstatic MCClass/a I
	invokestatic io/putIntLn(I)V
Label4:
	iconst_3
	putstatic MCClass/a I
	getstatic MCClass/a I
	invokestatic io/putIntLn(I)V
Label5:
Label3:
	getstatic MCClass/a I
	invokestatic io/putIntLn(I)V
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
