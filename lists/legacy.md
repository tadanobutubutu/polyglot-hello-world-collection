# Legacy カテゴリー

収録数: 44

---

## ALGOL 68
```algol68
begin
  print(("Hello World",newline))
end
```
[ソースファイル](../languages/ALGOL 68.algol68)

## ALGOL W
```algol
begin
    write( "Hello World" )
end.
```
[ソースファイル](../languages/ALGOL W.algol)

## Ada
```adb
with Ada.Text_IO;

procedure Hello_World is
   use Ada.Text_IO;
begin
   Put_line ("Hello World");
end Hello_World;
```
[ソースファイル](../languages/Ada.adb)

## Applesoft BASIC
```
10 PRINT "HELLO WORLD"
```
[ソースファイル](../languages/Applesoft BASIC)

## AutoLISP
```lsp
(alert "Hello World")
```
[ソースファイル](../languages/AutoLISP.lsp)

## BASIC
```bas
10 PRINT "Hello World"
20 END
```
[ソースファイル](../languages/BASIC.bas)

## BASIC 256
```kbs
Print "Hello World"
```
[ソースファイル](../languages/BASIC 256.kbs)

## BBC BASIC
```bbc
PRINT "Hello World"
```
[ソースファイル](../languages/BBC BASIC.bbc)

## CLISP
```lisp
(write-line "Hello World")
```
[ソースファイル](../languages/CLISP.lisp)

## COBOL
```cbl
identification division.
       program-id. cobol.
       procedure division.
       main.
           display 'Hello World.' end-display.
           stop run.
```
[ソースファイル](../languages/COBOL.cbl)

## Casio BASIC
```
"Hello World"
```
[ソースファイル](../languages/Casio BASIC)

## CobolScript
```cbl
DISPLAY `Content-type: text/html `.
DISPLAY LINEFEED.
DISPLAY `<HTML><BODY>`.
DISPLAY `<CENTER>Hello World</CENTER>`.
DISPLAY `</BODY></HTML>`.
GOBACK.
```
[ソースファイル](../languages/CobolScript.cbl)

## Common Lisp
```lisp
(print "Hello World")
```
[ソースファイル](../languages/Common Lisp.lisp)

## EchoLisp
```echolisp
(display "Hello World" "color:blue")
```
[ソースファイル](../languages/EchoLisp.echolisp)

## EmacsLisp
```el
(message "Hello World")
```
[ソースファイル](../languages/EmacsLisp.el)

## Fortran
```f90
print *,'Hello World'
end
```
[ソースファイル](../languages/Fortran.f90)

## Fortran77
```f77
PROGRAM HELLOW
      WRITE(UNIT=*, FMT=*) 'Hello World'
      END
```
[ソースファイル](../languages/Fortran77.f77)

## G-BASIC
```
カケ Hello World
```
[ソースファイル](../languages/G-BASIC)

## GFA Basic
```
PRINT "Hello World"
```
[ソースファイル](../languages/GFA Basic)

## ISLISP
```lisp
(format (standard-output) "Hello World")
```
[ソースファイル](../languages/ISLISP.lisp)

## LibreOffice Basic
```bas
﻿REM  *****  BASIC  *****

Sub Main
 msgbox "Hello World"
End Sub
```
[ソースファイル](../languages/LibreOffice Basic.bas)

## Lisp
```lsp
; LISP
(DEFUN hello ()
  (PRINT (LIST 'HELLO 'WORLD))
)

(hello)
```
[ソースファイル](../languages/Lisp.lsp)

## Locomotive Basic
```b
10 print "Hello World"
run
```
[ソースファイル](../languages/Locomotive Basic.b)

## Logo
```lg
print [Hello World]
```
[ソースファイル](../languages/Logo.lg)

## MacLisp
```lisp
(comment) ;-*- Lisp -*-
(progn
  (defun hello-world ()
    (princ "Hello World")
    (quit))
  (close (prog1 infile (inpush -1)))
  (sstatus feature noldmsg)
  (gctwa)
  (gc)
  (sstatus flush t)
  (suspend ":KILL " '(ts hello))
  (hello-world))
```
[ソースファイル](../languages/MacLisp.lisp)

## MemeAssembly
```memeasm
I like to have fun, fun, fun, fun, fun, fun, fun, fun, fun, fun main
    what can I say except H
    what can I say except e
    what can I say except l
    what can I say except l
    what can I say except o
    what can I say except \s
    what can I say except W
    what can I say except o
    what can I say except r
    what can I say except l
    what can I say except d
    what can I say except \n

    I see this as an absolute win
```
[ソースファイル](../languages/MemeAssembly.memeasm)

## NewLISP
```lsp
#!/usr/bin/newlisp
(print "Hello World\n")
(exit)
```
[ソースファイル](../languages/NewLISP.lsp)

## Object Pascal
```pp
program ObjectPascalExample;

type
   THelloWorld = class
      procedure Put;
   end;

procedure THelloWorld.Put;
begin
   Writeln('Hello World');
end;

var
   HelloWorld: THelloWorld;

begin
   HelloWorld := THelloWorld.Create;
   HelloWorld.Put;
   HelloWorld.Free;
end.
```
[ソースファイル](../languages/Object Pascal.pp)

## Pascal
```p
program HelloWorld(output);
begin
        writeln('Hello World');
end.
```
[ソースファイル](../languages/Pascal.p)

## PureBasic
```pb
If OpenConsole()
  PrintN("Hello World")
EndIf
```
[ソースファイル](../languages/PureBasic.pb)

## QBasic
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/QBasic.bas)

## RealBasic
```realbasic
Function Run(args() as String) As Integer
  Print "Hello World"
  Quit
End Function
```
[ソースファイル](../languages/RealBasic.realbasic)

## S Algol
```
write "Hello World"
?
```
[ソースファイル](../languages/S Algol)

## SmallTalk
```sm
Transcript show: 'Hello World'.
```
[ソースファイル](../languages/SmallTalk.sm)

## SmallTalk GNU
```st
'Hello World' printNl !
```
[ソースファイル](../languages/SmallTalk GNU.st)

## SmileBASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/SmileBASIC.bas)

## TIBasic
> [!NOTE]
> この言語のプログラムはバイナリまたは専用形式のため、ソースファイル自体をご確認ください。
[ソースファイル](../languages/TIBasic.ti)

## Visual Basic
```vb
Module HelloWorld
    Sub Main()
        MsgBox("Hello World")
    End Sub
End Module
```
[ソースファイル](../languages/Visual Basic.vb)

## Visual Basic Script
```vbs
MsgBox "Hello World"
```
[ソースファイル](../languages/Visual Basic Script.vbs)

## Visual Basic for Applications
```vba
Sub HelloWorld()
    Call MsgBox("Hello World")
End Sub
```
[ソースファイル](../languages/Visual Basic for Applications.vba)

## WebAssembly
```wat
(module
    (import "wasi_unstable" "fd_write"
        (func $fd_write (param i32 i32 i32 i32) (result i32))
    )

    (memory 1)
    (export "memory" (memory 0))

    (data (i32.const 0) "\08\00\00\00\0c\00\00\00Hello World\n")

    (func $main (export "_start")
        i32.const 1
        i32.const 0
        i32.const 1
        i32.const 20
        call $fd_write
        drop
    )
)
```
[ソースファイル](../languages/WebAssembly.wat)

## XBasic
```x
IMPORT "xst"
DECLARE FUNCTION  Hello ()

FUNCTION  Hello ()
 XstDisplayConsole ()
 PRINT "Hello World"
END FUNCTION
END PROGRAM
```
[ソースファイル](../languages/XBasic.x)

## XLisp
```xlisp
(DISPLAY "Hello World")
(NEWLINE)
```
[ソースファイル](../languages/XLisp.xlisp)

## Xlogo
```lgo
to HelloWorld
 resetall
 hideturtle
 fd 20 left 180
 fd 40 left 180
 fd 20 right 90
 fd 20 left 90
 fd 20 left 180
 fd 40 left 90
 fd 20 left 90
 fd 20 right 90
 fd 20 right 90
 fd 10 right 90
 fd 20 left 90
 fd 10 left 90
 fd 30 left 90
 fd 40 left 180
 fd 40 left 90
 fd 20 left 90
 fd 40 left 180
 fd 40 left 90
 fd 40 left 90
 fd 20 left 90
 fd 20 left 90
 fd 20 left 90
 fd 60 left 90
 fd 40 left 180
 fd 40 left 90
 fd 20 left 90
 fd 20 left 180
 fd 20 left 90
 fd 20 left 90
 fd 40 left 180
 fd 40 left 90
 fd 40 left 90
 fd 20 left 90
 fd 20 left 90
 fd 20 left 90
 fd 40 left 90
 fd 20 right 90
 fd 20 right 90
 fd 5  left 90  
 fd 5  left 90  
 fd 25 left 180
 fd 40 left 90
 fd 40 left 90
 fd 20 left 90
 fd 20 left 90
 fd 20 left 90
 fd 20 left 90
 fd 40 left 180
 fd 40
end
```
[ソースファイル](../languages/Xlogo.lgo)

---
### 🚀 次のリストへ進む
**[Esoteric カテゴリー はこちら](esoteric.md)**