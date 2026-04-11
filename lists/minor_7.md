# マイナー言語 Part 7

収録数: 50

---

## K-OS
```k-os
print "Hello World"
```
[ソースファイル](../languages/K-OS)

## KRC
```krc
main = "Hello World\n"
```
[ソースファイル](../languages/KRC.krc)

## KRL
```krl
&ACCESS RVP
&REL 1
DEF hello_world( )
  MsgBox("Hello World")
END
```
[ソースファイル](../languages/KRL.src)

## KSH
```ksh
#!/bin/ksh
echo "Hello World"
```
[ソースファイル](../languages/KSH.ksh)

## Kaminari
```kaminari
print "Hello World"
```
[ソースファイル](../languages/Kaminari)

## Karel
```karel
BEGIN-PROGRAM
  output "Hello World";
END-PROGRAM
```
[ソースファイル](../languages/Karel.kl)

## Kayak
```kayak
print "Hello World"
```
[ソースファイル](../languages/Kayak)

## Kerboscript
```kerbo
PRINT "Hello World".
```
[ソースファイル](../languages/Kerboscript.ks)

## Kixtart
```kix
"Hello World"
```
[ソースファイル](../languages/Kixtart.kix)

## Koka
```koka
fun main() { println("Hello World") }
```
[ソースファイル](../languages/Koka.kk)

## Konoha
```konoha
System.p("Hello World");
```
[ソースファイル](../languages/Konoha.k)

## Kouros
```kouros
print "Hello World"
```
[ソースファイル](../languages/Kouros)

## Kuin
```kuin
func main()
	do cui@print("Hello World\n")
end func
```
[ソースファイル](../languages/Kuin.kn)

## Kylix
```pascal
program Hello;
{$APPTYPE CONSOLE}
begin
  Writeln('Hello World');
end.
```
[ソースファイル](../languages/Kylix.pas)

## L
```l
print "Hello World"
```
[ソースファイル](../languages/L.l)

## LABView
```labview
; Graphical G code
```
[ソースファイル](../languages/LABView)

## LANSA
```lansa
MESSAGE MSGTXT('Hello World')
```
[ソースファイル](../languages/LANSA.lansa)

## LFE
```lfe
(io:format "Hello World~n" '())
```
[ソースファイル](../languages/LFE.lfe)

## LLVM IR
```llvm
@str = private unnamed_addr constant [13 x i8] c"Hello World\0A\00"
declare i32 @puts(i8*)
define i32 @main() {
  %1 = call i32 @puts(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @str, i32 0, i32 0))
  ret i32 0
}
```
[ソースファイル](../languages/LLVM IR.ll)

## LOLCODE
```lolcode
HAI 1.2
  VISIBLE "Hello World"
KTHXBYE
```
[ソースファイル](../languages/LOLCODE.lol)

## LPC
```c
void create() { write("Hello World\n"); }
```
[ソースファイル](../languages/LPC.c)

## LSL
```lsl
default { state_entry() { llSay(0, "Hello World"); } }
```
[ソースファイル](../languages/LSL.lsl)

## LUA
```lua
print("Hello World")
```
[ソースファイル](../languages/LUA.lua)

## LabVIEW
```labview
; G code
```
[ソースファイル](../languages/LabVIEW)

## Lace
```lace
print "Hello World"
```
[ソースファイル](../languages/Lace)

## Lang5
```forth
"Hello World" println
```
[ソースファイル](../languages/Lang5.lang5)

## Lasso
```lasso
'Hello World'
```
[ソースファイル](../languages/Lasso.lasso)

## Latte
```latte
print "Hello World"
```
[ソースファイル](../languages/Latte)

## Lead
```lead
print "Hello World"
```
[ソースファイル](../languages/Lead)

## Lean
```lean
#eval "Hello World"
```
[ソースファイル](../languages/Lean.lean)

## Lego Mindstorms NXT
```nxt
task main() { TextOut(0, LCD_LINE1, "Hello World"); }
```
[ソースファイル](../languages/Lego Mindstorms NXT.nxc)

## LeslieLamport
```tex
Hello World
```
[ソースファイル](../languages/LeslieLamport.tex)

## Less
```css
.hello { content: "Hello World"; }
```
[ソースファイル](../languages/Less.less)

## Lex
```lex
%%
. ;
%%
int main() { printf("Hello World\n"); return 0; }
```
[ソースファイル](../languages/Lex.l)

## Ligo
```ligo
let main (a, s : unit * string) : operation list * string =
  (([] : operation list), "Hello World")
```
[ソースファイル](../languages/Ligo.ligo)

## Limbo
```limbo
implement Hello;
include "sys.m";
include "draw.m";
Hello: module { init: fn(ctxt: ref Draw->Context, args: list of string); };
init(ctxt: ref Draw->Context, args: list of string) {
    sys := load Sys Sys->PATH;
    sys->print("Hello World\n");
}
```
[ソースファイル](../languages/Limbo.b)

## Limbo
```limbo
print "Hello World";
```
[ソースファイル](../languages/Limbo)

## Linden Scripting Language
```lsl
default { state_entry() { llOwnerSay("Hello World"); } }
```
[ソースファイル](../languages/Linden Scripting Language.lsl)

## Line
```line
print "Hello World"
```
[ソースファイル](../languages/Line)

## Lingua::Romana::Perligata
```perl
use Lingua::Romana::Perligata;
meo->ecce("Hello World");
```
[ソースファイル](../languages/Lingua::Romana::Perligata.pl)

## Linux Kernel Module
```c
#include <linux/module.h>
int init_module(void) { printk(KERN_INFO "Hello World\n"); return 0; }
void cleanup_module(void) { printk(KERN_INFO "Goodbye World\n"); }
```
[ソースファイル](../languages/Linux Kernel Module.c)

## Lip
```lip
print "Hello World"
```
[ソースファイル](../languages/Lip)

## Lisaac
```lisaac
Section Header + name := HELLO_WORLD;
Section Public - main <- ( "Hello World\n".print; );
```
[ソースファイル](../languages/Lisaac.li)

## Lithe
```lithe
print "Hello World"
```
[ソースファイル](../languages/Lithe)

## LiveScript
```livescript
console.log "Hello World"
```
[ソースファイル](../languages/LiveScript.ls)

## Livewire
```livewire
write("Hello World");
```
[ソースファイル](../languages/Livewire)

## Lm
```lm
print "Hello World"
```
[ソースファイル](../languages/Lm)

## Logtalk
```logtalk
:- object(hello_world).
    :- public(say_hello/0).
    say_hello :- write('Hello World'), nl.
:- end_object.
```
[ソースファイル](../languages/Logtalk.lgt)

## Look
```look
print "Hello World"
```
[ソースファイル](../languages/Look)

## LotusScript
```vb
Print "Hello World"
```
[ソースファイル](../languages/LotusScript.lss)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 8 はこちら](minor_8.md)