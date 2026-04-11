# マイナー言語 Part 1

収録数: 50

---

## !EXE
```
"Hello World!"
```
[ソースファイル](../languages/!EXE)

## 05AB1E
```
”Hello World”
```
[ソースファイル](../languages/05AB1E)

## 10001
```
"Hello World"
```
[ソースファイル](../languages/10001)

## 2048
```
"Hello World"
```
[ソースファイル](../languages/2048.2048)

## 2D
```
"Hello World"
```
[ソースファイル](../languages/2D)

## 4
```
"Hello World"
```
[ソースファイル](../languages/4)

## 7
```
"Hello World"
```
[ソースファイル](../languages/7)

## 8051 Assembly
```asm
; 8051 Assembly
ORG 0000H
AJMP START

ORG 0030H
START:
    MOV DPTR,#HELLO
LOOP:
    CLR A
    MOVC A,@A+DPTR
    JZ END_LOOP
    ACALL SEND_CHAR
    INC DPTR
    SJMP LOOP
END_LOOP:
    SJMP END_LOOP

SEND_CHAR:
    ; Send character in A to UART or Display
    RET

HELLO: DB 'Hello World',0
END
```
[ソースファイル](../languages/8051 Assembly.asm)

## 8th
```
"Hello World" . cr bye
```
[ソースファイル](../languages/8th)

## 99
```
"Hello World"
```
[ソースファイル](../languages/99)

## A
```
"Hello World"
```
[ソースファイル](../languages/A.a)

## ADL
```adl
program hello;
begin
    print("Hello World");
end hello.
```
[ソースファイル](../languages/ADL.adl)

## AGS Script
```ags
Display("Hello World");
```
[ソースファイル](../languages/AGS Script.ags)

## AMOS
```amos
Print "Hello World"
```
[ソースファイル](../languages/AMOS.amos)

## AMPL
```ampl
print "Hello World";
```
[ソースファイル](../languages/AMPL.ampl)

## APL
```apl
'Hello World'
```
[ソースファイル](../languages/APL.apl)

## ARX
```arx
print "Hello World"
```
[ソースファイル](../languages/ARX.arx)

## ASP
```asp
<%
Response.Write("Hello World")
%>
```
[ソースファイル](../languages/ASP.asp)

## AWK
```awk
BEGIN { print "Hello World" }
```
[ソースファイル](../languages/AWK.awk)

## AXE
```axe
Disp "Hello World
```
[ソースファイル](../languages/AXE.axe)

## ActionScript
```as
trace("Hello World");
```
[ソースファイル](../languages/ActionScript.as)

## Aeon
```aeon
print "Hello World"
```
[ソースファイル](../languages/Aeon.aeon)

## Aheui
```aheui
밤밞밞따밞밞밞밞따밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞밞따맣희
```
[ソースファイル](../languages/Aheui.aheui)

## Alchemist
```alchemist
main -> Hello World
```
[ソースファイル](../languages/Alchemist.alchemist)

## Aldor
```aldor
#include "aldor"
#include "aldorio"

import from TextWriter, String, Character;

stdout << "Hello World" << newline;
```
[ソースファイル](../languages/Aldor.as)

## Aleph
```aleph
(princ "Hello World")
```
[ソースファイル](../languages/Aleph.aleph)

## Alf
```alf
Hello World
```
[ソースファイル](../languages/Alf.alf)

## Algebird
```algebird
print "Hello World"
```
[ソースファイル](../languages/Algebird.algebird)

## Alice
```alice
val _ = TextIO.output (TextIO.stdOut, "Hello World\n")
```
[ソースファイル](../languages/Alice.aml)

## Allaire Spectra
```spectra
<cf_hello>
    Hello World
</cf_hello>
```
[ソースファイル](../languages/Allaire Spectra.cfm)

## Alore
```alore
WriteLn("Hello World")
```
[ソースファイル](../languages/Alore.alore)

## Alpaca
```alpaca
export hello_world

let main = print "Hello World"
```
[ソースファイル](../languages/Alpaca.alp)

## Ambi
```ambi
"Hello World" print
```
[ソースファイル](../languages/Ambi.ambi)

## AngelScript
```as
void Main()
{
    Print("Hello World\n");
}
```
[ソースファイル](../languages/AngelScript.as)

## Anubis
```anubis
global define One
   hello_world
     (
       List(String) args
     ) =
   print("Hello World\n").
```
[ソースファイル](../languages/Anubis.anubis)

## Apex
```apex
System.debug('Hello World');
```
[ソースファイル](../languages/Apex.cls)

## AppleScript
```applescript
display dialog "Hello World"
```
[ソースファイル](../languages/AppleScript.applescript)

## Arc
```arc
(prn "Hello World")
```
[ソースファイル](../languages/Arc.arc)

## ArnoldC
```arnoldc
IT'S SHOWTIME
TALK TO THE HAND "Hello World"
YOU HAVE BEEN TERMINATED
```
[ソースファイル](../languages/ArnoldC.arnoldc)

## ArrayFire
```cpp
#include <arrayfire.h>
#include <cstdio>

int main(int argc, char *argv[]) {
    printf("Hello World\n");
    return 0;
}
```
[ソースファイル](../languages/ArrayFire.cpp)

## Arrow
```arrow
/-----\
|Hello|
|World|
\-----/
```
[ソースファイル](../languages/Arrow)

## Asciidoc
```asciidoc
Hello World
```
[ソースファイル](../languages/Asciidoc.adoc)

## AspectJ
```java
public aspect HelloWorld {
    pointcut mainMethod() : execution(public static void main(String[]));

    after() : mainMethod() {
        System.out.println("Hello World");
    }
}
```
[ソースファイル](../languages/AspectJ.aj)

## Assembly 6502
```asm
; 6502 Assembly
LDX #0
LOOP:
    LDA HELLO,X
    BEQ END
    JSR $FFD2 ; PRINT CHAR
    INX
    BNE LOOP
END:
    RTS
HELLO: .ASCII "Hello World",0
```
[ソースファイル](../languages/Assembly 6502.asm)

## Atom
```atom
print "Hello World"
```
[ソースファイル](../languages/Atom.atom)

## AutoIt
```autoit
MsgBox(0, "Hello World", "Hello World")
```
[ソースファイル](../languages/AutoIt.au3)

## AutoHotkey
```autohotkey
MsgBox, Hello World
```
[ソースファイル](../languages/AutoHotkey.ahk)

## Avenue
```avenue
MsgBox("Hello World", "Hello World")
```
[ソースファイル](../languages/Avenue.ave)

## AviSynth
```avisynth
BlankClip()
Subtitle("Hello World")
```
[ソースファイル](../languages/AviSynth.avs)

## Axiom
```axiom
print "Hello World"
```
[ソースファイル](../languages/Axiom.axiom)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 2 はこちら](minor_2.md)