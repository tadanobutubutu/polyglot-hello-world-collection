# マイナー言語 Part 8

収録数: 50

---

## Love2D
```lua
function love.draw() love.graphics.print("Hello World", 400, 300) end
```
[ソースファイル](../languages/Love2D.lua)

## Low-Level Virtual Machine
```llvm
@.str = private unnamed_addr constant [13 x i8] c"Hello World\0A\00"
declare i32 @puts(i8*)
define i32 @main() {
  %1 = call i32 @puts(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @.str, i32 0, i32 0))
  ret i32 0
}
```
[ソースファイル](../languages/Low-Level Virtual Machine.ll)

## Lucent
```lucent
print "Hello World"
```
[ソースファイル](../languages/Lucent)

## Lucid
```lucid
print "Hello World"
```
[ソースファイル](../languages/Lucid)

## Luminary
```luminary
print "Hello World"
```
[ソースファイル](../languages/Luminary)

## Lush
```lush
(print "Hello World")
```
[ソースファイル](../languages/Lush.lsh)

## Lustre
```lustre
node hello() returns (o: bool); let o = true; tel
```
[ソースファイル](../languages/Lustre.lus)

## Lux
```lux
(print "Hello World")
```
[ソースファイル](../languages/Lux)

## Lynx
```lynx
print "Hello World"
```
[ソースファイル](../languages/Lynx)

## Lyris
```lyris
print "Hello World"
```
[ソースファイル](../languages/Lyris)

## M
```m
W "Hello World",!
```
[ソースファイル](../languages/M.m)

## M4
```m4
Hello World
```
[ソースファイル](../languages/M4.m4)

## MACRO-11
```asm
.TITLE HELLO
.MCALL .TTYOUT,.EXIT
START:  MOV #MSG,R0
LOOP:   MOVB (R0)+,R1
        BEQ DONE
        .TTYOUT R1
        BR LOOP
DONE:   .EXIT
MSG:    .ASCIZ /Hello World/
.END START
```
[ソースファイル](../languages/MACRO-11.mac)

## MAGMA
```magma
print "Hello World";
```
[ソースファイル](../languages/MAGMA.magma)

## MAPLE
```maple
print("Hello World");
```
[ソースファイル](../languages/MAPLE.mpl)

## MAXScript
```maxscript
print "Hello World"
```
[ソースファイル](../languages/MAXScript.ms)

## MHEG-5
```mheg
(:Scene (Hello World))
```
[ソースファイル](../languages/MHEG-5)

## MIIS
```miis
W "Hello World",!
```
[ソースファイル](../languages/MIIS)

## MIMIC
```mimic
print "Hello World"
```
[ソースファイル](../languages/MIMIC)

## ML
```ml
print "Hello World\n";
```
[ソースファイル](../languages/ML.ml)

## MOO
```moo
player:tell("Hello World");
```
[ソースファイル](../languages/MOO.moo)

## MOONBlock
> [!NOTE]
> この言語のプログラムはバイナリまたは専用形式のため、ソースファイル自体をご確認ください。
[ソースファイル](../languages/MOONBlock.png)

## MPD
```mpd
resource hello()
   process main
      write("Hello World")
   end
end
```
[ソースファイル](../languages/MPD.mpd)

## MS-DOS Batch
```batch
@echo Hello World
```
[ソースファイル](../languages/MS-DOS Batch.bat)

## MSIL
```cil
.assembly Hello {}
.method public static void Main() {
    .entrypoint
    ldstr "Hello World"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
}
```
[ソースファイル](../languages/MSIL.il)

## MTM
```mtm
print "Hello World"
```
[ソースファイル](../languages/MTM)

## MUF
```muf
: main "Hello World" notify ;
```
[ソースファイル](../languages/MUF.muf)

## MUR
```mur
print "Hello World"
```
[ソースファイル](../languages/MUR)

## MUMPS
```m
W "Hello World",!
```
[ソースファイル](../languages/MUMPS.m)

## MUSHCode
```mush
@pemit me=Hello World
```
[ソースファイル](../languages/MUSHCode.mush)

## Macsyma
```macsyma
print("Hello World")$
```
[ソースファイル](../languages/Macsyma.macsyma)

## Magik
```magik
write("Hello World")
$
```
[ソースファイル](../languages/Magik.magik)

## Makefile
```makefile
all:
	@echo Hello World
```
[ソースファイル](../languages/Makefile)

## Make
```make
hello:
	@echo "Hello World"
```
[ソースファイル](../languages/Make)

## Managed Extensions for C++
```cpp
using namespace System;
int main() { Console::WriteLine("Hello World"); return 0; }
```
[ソースファイル](../languages/Managed Extensions for C++.cpp)

## Maple
```maple
print("Hello World");
```
[ソースファイル](../languages/Maple.mpl)

## Marc
```marc
print "Hello World"
```
[ソースファイル](../languages/Marc)

## MariaDB
```sql
SELECT 'Hello World';
```
[ソースファイル](../languages/MariaDB.sql)

## Markdown
```markdown
Hello World
```
[ソースファイル](../languages/Markdown.md)

## Mary
```mary
BEGIN PRINT(("Hello World", newline)) END
```
[ソースファイル](../languages/Mary.mary)

## Masm
```asm
.model small
.stack 100h
.data
msg db 'Hello World$', 0
.code
start:
    mov ax, @data
    mov ds, ax
    lea dx, msg
    mov ah, 09h
    int 21h
    mov ax, 4c00h
    int 21h
end start
```
[ソースファイル](../languages/Masm.asm)

## Mathematica
```wolfram
Print["Hello World"]
```
[ソースファイル](../languages/Mathematica.m)

## MathML
```xml
<math><mtext>Hello World</mtext></math>
```
[ソースファイル](../languages/MathML.mathml)

## Maude
```maude
fmod HELLO-WORLD is
  protecting STRING .
  op hello : -> String .
  eq hello = "Hello World" .
endfm
```
[ソースファイル](../languages/Maude.maude)

## Max
```max
; Graphical Max/MSP patch
```
[ソースファイル](../languages/Max.maxpat)

## Maya Embedded Language
```mel
print "Hello World";
```
[ソースファイル](../languages/Maya Embedded Language.mel)

## Mentor
```mentor
print "Hello World"
```
[ソースファイル](../languages/Mentor)

## Mercury
```mercury
:- module hello.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
main(!IO) :- io.write_string("Hello World\n", !IO).
```
[ソースファイル](../languages/Mercury.m)

## Meridian
```meridian
print "Hello World"
```
[ソースファイル](../languages/Meridian)

## Mesa
```mesa
HelloWorld: PROGRAM = BEGIN
  Put["Hello World\n"];
END.
```
[ソースファイル](../languages/Mesa.mesa)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 9 はこちら](minor_9.md)