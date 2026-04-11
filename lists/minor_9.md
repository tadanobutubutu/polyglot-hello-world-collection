# マイナー言語 Part 9

収録数: 50

---

## Metal
```cpp
#include <metal_stdlib>
using namespace metal;
// Metal shader version of Hello World
```
[ソースファイル](../languages/Metal.metal)

## Metapost
```metapost
beginfig(1);
  draw (0,0)--(100,100);
  label("Hello World", (50,50));
endfig;
end
```
[ソースファイル](../languages/Metapost.mp)

## MicroBASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/MicroBASIC)

## MicroFocus COBOL
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.
PROCEDURE DIVISION.
    DISPLAY "Hello World".
    STOP RUN.
```
[ソースファイル](../languages/MicroFocus COBOL.cbl)

## Micros
```micros
print "Hello World"
```
[ソースファイル](../languages/Micros)

## Mimic
```mimic
print "Hello World"
```
[ソースファイル](../languages/Mimic)

## Mini-D
```d
import std.io;
void main() { writeln("Hello World") }
```
[ソースファイル](../languages/Mini-D.md)

## MiniD
```d
print("Hello World")
```
[ソースファイル](../languages/MiniD.minid)

## Mint
```mint
component Main {
  fun render : Html {
    <div>"Hello World"</div>
  }
}
```
[ソースファイル](../languages/Mint.mint)

## Miranda
```miranda
main = [ "Hello World\n" ]
```
[ソースファイル](../languages/Miranda.m)

## Miva Script
```xml
<Miva Expression="{ 'Hello World' }">
```
[ソースファイル](../languages/Miva Script.mv)

## Mixal
```asm
TERM    EQU    19
        ORIG   3000
START   OUT    MSG(TERM)
        HLT
MSG     ALF    "HELLO"
        ALF    " WORL"
        ALF    "D    "
        END    START
```
[ソースファイル](../languages/Mixal.mixal)

## Modelica
```modelica
model HelloWorld
  initial equation
    print("Hello World");
end HelloWorld;
```
[ソースファイル](../languages/Modelica.mo)

## Modula-2
```modula2
MODULE Hello;
FROM InOut IMPORT WriteString, WriteLn;
BEGIN
  WriteString("Hello World"); WriteLn;
END Hello.
```
[ソースファイル](../languages/Modula-2.mod)

## Modula-3
```modula3
MODULE Main;
IMPORT IO;
BEGIN
  IO.Put("Hello World\n");
END Main.
```
[ソースファイル](../languages/Modula-3.m3)

## Mohol
```mohol
print "Hello World"
```
[ソースファイル](../languages/Mohol)

## Monk
```monk
(print "Hello World")
```
[ソースファイル](../languages/Monk)

## Moo
```moo
player:tell("Hello World");
```
[ソースファイル](../languages/Moo)

## MoonScript
```moonscript
print "Hello World"
```
[ソースファイル](../languages/MoonScript.moon)

## Mouse
```mouse
"Hello World"
$
```
[ソースファイル](../languages/Mouse.mouse)

## Mu
```mu
fn main {
  "Hello World\n" print
}
```
[ソースファイル](../languages/Mu.mu)

## Multics
```multics
print "Hello World"
```
[ソースファイル](../languages/Multics)

## MySQL
```sql
SELECT 'Hello World';
```
[ソースファイル](../languages/MySQL.sql)

## N-BASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/N-BASIC.bas)

## NASM
```asm
section .data
    msg db 'Hello World', 0xa
section .text
    global _start
_start:
    mov edx, 12
    mov ecx, msg
    mov ebx, 1
    mov eax, 4
    int 0x80
    mov eax, 1
    int 0x80
```
[ソースファイル](../languages/NASM.asm)

## NCL
```ncl
begin
  print("Hello World")
end
```
[ソースファイル](../languages/NCL.ncl)

## NDS
```c
#include <nds.h>
#include <stdio.h>
int main() {
    consoleDemoInit();
    iprintf("Hello World");
    while(1) { swiWaitForVBlank(); }
    return 0;
}
```
[ソースファイル](../languages/NDS.c)

## NEKO
```neko
$print("Hello World\n");
```
[ソースファイル](../languages/NEKO.neko)

## NQC
```nqc
task main() {
  TextOut(0, LCD_LINE1, "Hello World");
}
```
[ソースファイル](../languages/NQC.nqc)

## NSIS
```nsis
Name "Hello World"
OutFile "Hello.exe"
Section "Display"
  MessageBox MB_OK "Hello World"
SectionEnd
```
[ソースファイル](../languages/NSIS.nsi)

## NXT-G
> [!NOTE]
> この言語のプログラムはバイナリまたは専用形式のため、ソースファイル自体をご確認ください。
[ソースファイル](../languages/NXT-G)

## NATURAL
```natural
WRITE "Hello World"
END
```
[ソースファイル](../languages/NATURAL.nat)

## Nemerle
```nemerle
System.Console.WriteLine("Hello World");
```
[ソースファイル](../languages/Nemerle.n)

## NesC
```c
module HelloC {
  uses interface Boot;
}
implementation {
  event void Boot.booted() {
    trace("Hello World\n");
  }
}
```
[ソースファイル](../languages/NesC.nc)

## NetLinx
```netlinx
PROGRAM_NAME='Hello'
DEFINE_START
SEND_STRING 0,"'Hello World'"
```
[ソースファイル](../languages/NetLinx.axs)

## NetLogo
```netlogo
to hello
  print "Hello World"
end
```
[ソースファイル](../languages/NetLogo.nlogo)

## NewLISP
```newlisp
(println "Hello World")
(exit)
```
[ソースファイル](../languages/NewLISP.lsp)

## Newspeak
```newspeak
class HelloWorld = ( | | ) (
  public main = ( print: 'Hello World' )
)
```
[ソースファイル](../languages/Newspeak.ns)

## NewtonScript
```newtonscript
print("Hello World")
```
[ソースファイル](../languages/NewtonScript.ns)

## Nextflow
```nextflow
process hello {
    script:
    """
    echo 'Hello World'
    """
}
```
[ソースファイル](../languages/Nextflow.nf)

## Nickle
```nickle
printf ("Hello World\n");
```
[ソースファイル](../languages/Nickle.5c)

## Nim
```nim
echo "Hello World"
```
[ソースファイル](../languages/Nim.nim)

## Nit
```nit
print "Hello World"
```
[ソースファイル](../languages/Nit.nit)

## Nix
```nix
"Hello World"
```
[ソースファイル](../languages/Nix.nix)

## Noot
```noot
noot noot "Hello World"
```
[ソースファイル](../languages/Noot.noot)

## Nu
```nu
(puts "Hello World")
```
[ソースファイル](../languages/Nu.nu)

## Nutrient
```nutrient
print "Hello World"
```
[ソースファイル](../languages/Nutrient)

## Nyquist
```lisp
(print "Hello World")
```
[ソースファイル](../languages/Nyquist.ny)

## O-JEE
```ojee
print "Hello World"
```
[ソースファイル](../languages/O-JEE)

## O-PPL
```oppl
print "Hello World"
```
[ソースファイル](../languages/O-PPL)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 10 はこちら](minor_10.md)