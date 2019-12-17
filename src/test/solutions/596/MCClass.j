.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static j I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is b I from Label3 to Label1
Label3:
.var 3 is iSum I from Label4 to Label1
Label4:
	bipush 10
	putstatic MCClass/i I
Label5:
.var 4 is i F from Label5 to Label6
	ldc 14.3
	fstore 4
Label7:
.var 5 is i I from Label7 to Label8
	bipush 19
	istore 5
	iload 5
	invokestatic io/putInt(I)V
Label8:
	fload 4
	invokestatic io/putFloat(F)V
Label6:
	getstatic MCClass/i I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 6
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
