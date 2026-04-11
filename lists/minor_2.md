# マイナー言語 Part 2

収録数: 50

---

## B
```b
main( ) {
	putchar('hell');
	putchar('o wo');
	putchar('rld\n');
}
```
[ソースファイル](../languages/B.b)

## B-Sharp
```bsharp
main() {
    print("Hello World\n");
}
```
[ソースファイル](../languages/B-Sharp.bsharp)

## BC
```bc
print "Hello World\n"
quit
```
[ソースファイル](../languages/BC.bc)

## BCPL
```bcpl
GET "libhdr"

LET START() BE
$(
    WRITES("Hello World*N")
$)
```
[ソースファイル](../languages/BCPL.bcpl)

## BQN
```bqn
"Hello World"
```
[ソースファイル](../languages/BQN.bqn)

## BS
```bs
print "Hello World"
```
[ソースファイル](../languages/BS.bs)

## BS2000 ASSEMBLY
```asm
HELLO    START
         PRINT 'Hello World'
         END
```
[ソースファイル](../languages/BS2000 ASSEMBLY.asm)

## Bash
```bash
#!/bin/bash
echo "Hello World"
```
[ソースファイル](../languages/Bash.sh)

## Batch
```batch
@echo off
echo Hello World
```
[ソースファイル](../languages/Batch.bat)

## BeanShell
```java
print("Hello World");
```
[ソースファイル](../languages/BeanShell.bsh)

## Beat
```beat
H e l l o   W o r l d
```
[ソースファイル](../languages/Beat.beat)

## Bee
```bee
print "Hello World"
```
[ソースファイル](../languages/Bee.bee)

## Befunge
```befunge
 > v
 v"Hello World" <
 > :, ^
 @
```
[ソースファイル](../languages/Befunge.be)

## Beta
```beta
(# do 'Hello World' -> screen.putLine #)
```
[ソースファイル](../languages/Beta.bet)

## BibTeX
```bib
@misc{hello,
  note = "Hello World"
}
```
[ソースファイル](../languages/BibTeX.bib)

## Bigwig
```bigwig
service {
    session main() {
        exit "Hello World";
    }
}
```
[ソースファイル](../languages/Bigwig.bigwig)

## Bistro
```bistro
package hello;

public class World {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```
[ソースファイル](../languages/Bistro.bistro)

## Bit
```bit
10101010
```
[ソースファイル](../languages/Bit.bit)

## BitBaka
```bitbaka
print "Hello World"
```
[ソースファイル](../languages/BitBaka.bitbaka)

## BlitzBasic
```bb
Print "Hello World"
WaitKey
```
[ソースファイル](../languages/BlitzBasic.bb)

## BlitzMax
```bmx
Print "Hello World"
```
[ソースファイル](../languages/BlitzMax.bmx)

## BlooP
```bloop
DEFINE PROCEDURE ''HELLO-WORLD'' [N]:
    PRINT ['Hello World'].
```
[ソースファイル](../languages/BlooP.bloop)

## Blue
```blue
class HelloWorld is
    main is
        System.out.println("Hello World");
    end
end
```
[ソースファイル](../languages/Blue.blue)

## BlueSpec
```bsv
module mkHelloWorld(Empty);
    rule say_hello;
        $display("Hello World");
        $finish;
    endrule
endmodule
```
[ソースファイル](../languages/BlueSpec.bsv)

## Boo
```boo
print "Hello World"
```
[ソースファイル](../languages/Boo.boo)

## Boomerang
```boomerang
print "Hello World"
```
[ソースファイル](../languages/Boomerang.boomerang)

## Borbo
```borbo
print "Hello World"
```
[ソースファイル](../languages/Borbo.borbo)

## Bosque
```bosque
namespace Main;

entrypoint function main(): String {
    return "Hello World";
}
```
[ソースファイル](../languages/Bosque.bsq)

## Bourne Shell
```sh
#!/bin/sh
echo Hello World
```
[ソースファイル](../languages/Bourne Shell.sh)

## Bowl
```bowl
print "Hello World"
```
[ソースファイル](../languages/Bowl.bowl)

## Brat
```brat
p "Hello World"
```
[ソースファイル](../languages/Brat.brat)

## Brightscript
```brs
sub main()
    print "Hello World"
end sub
```
[ソースファイル](../languages/Brightscript.brs)

## Britefury
```britefury
print "Hello World"
```
[ソースファイル](../languages/Britefury.britefury)

## Brix
```brix
print "Hello World"
```
[ソースファイル](../languages/Brix.brix)

## Bud
```bud
print "Hello World"
```
[ソースファイル](../languages/Bud.bud)

## Burns
```burns
print "Hello World"
```
[ソースファイル](../languages/Burns.burns)

## Burp
```burp
print "Hello World"
```
[ソースファイル](../languages/Burp.burp)

## Business Basic
```
10 PRINT "Hello World"
```
[ソースファイル](../languages/Business Basic)

## Byte
```byte
print "Hello World"
```
[ソースファイル](../languages/Byte.byte)

## C-Shell
```csh
#!/bin/csh
echo "Hello World"
```
[ソースファイル](../languages/C-Shell.csh)

## C-dash
```c
print "Hello World"
```
[ソースファイル](../languages/C-dash)

## C--
```c--
target byteorder little;
import "printf";

export main;

section "data" {
    hello: byte[] "Hello World\n\0";
}

foreign "C" main() {
    foreign "C" printf(hello);
    return 0;
}
```
[ソースファイル](../languages/C--.cmm)

## CAPL
```capl
includes { }
variables { }
on start {
  write("Hello World");
}
```
[ソースファイル](../languages/CAPL.can)

## CA-Realizer
```realizer
Print "Hello World"
```
[ソースファイル](../languages/CA-Realizer.rlz)

## CDuce
```cduce
print [ 'Hello World' ]
```
[ソースファイル](../languages/CDuce.cd)

## CFML
```cfm
<cfoutput>Hello World</cfoutput>
```
[ソースファイル](../languages/CFML.cfm)

## CHILL
```chill
hello:
  procedure;
    print ("Hello World");
  end hello;
```
[ソースファイル](../languages/CHILL.chill)

## CHIP-8
```chi
00E0 ; CLS
6000 ; V0 = 0
610A ; V1 = 10
...
```
[ソースファイル](../languages/CHIP-8.chi)

## CIL
```cil
.assembly hello {}
.method public static void Main() cil managed {
    .entrypoint
    ldstr "Hello World"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
}
```
[ソースファイル](../languages/CIL.il)

## CLIPS
```clips
(printout t "Hello World" crlf)
```
[ソースファイル](../languages/CLIPS.clp)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 3 はこちら](minor_3.md)