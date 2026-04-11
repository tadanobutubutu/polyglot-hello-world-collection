# マイナー言語 Part 4

収録数: 50

---

## Databus
```
DISPLAY "Hello World"
STOP
```
[ソースファイル](../languages/Databus)

## Datalog
```datalog
p("Hello World").
?- p(X).
```
[ソースファイル](../languages/Datalog.dl)

## Datastic
```datastic
print "Hello World"
```
[ソースファイル](../languages/Datastic)

## Delphi
```pascal
program HelloWorld;
{$APPTYPE CONSOLE}
begin
  Writeln('Hello World');
end.
```
[ソースファイル](../languages/Delphi.pas)

## Deno
```typescript
console.log("Hello World");
```
[ソースファイル](../languages/Deno.ts)

## Desire
```desire
print "Hello World"
```
[ソースファイル](../languages/Desire)

## Digiblast
```digiblast
print "Hello World"
```
[ソースファイル](../languages/Digiblast)

## Digital Command Language
```dcl
$ write sys$output "Hello World"
```
[ソースファイル](../languages/Digital Command Language.com)

## Dilworth
```dilworth
print "Hello World"
```
[ソースファイル](../languages/Dilworth)

## DogeScript
```dogescript
shh SUCH HELLO
plz console.loge with 'Hello World'
```
[ソースファイル](../languages/DogeScript.doge)

## Dolittle
```dolittle
「Hello World」と　言う。
```
[ソースファイル](../languages/Dolittle.dtl)

## Doo
```doo
print "Hello World"
```
[ソースファイル](../languages/Doo)

## Dot
```dot
graph G { label="Hello World"; }
```
[ソースファイル](../languages/Dot.dot)

## Dylan
```dylan
module: hello

define method main(name, arguments)
  format-out("Hello World\n");
  exit(exit-code: 0);
end method main;

main(application-name(), application-arguments());
```
[ソースファイル](../languages/Dylan.dylan)

## Dynpro
```abap
REPORT  ZHELLO.
WRITE 'Hello World'.
```
[ソースファイル](../languages/Dynpro.abap)

## E
```e
println("Hello World")
```
[ソースファイル](../languages/E.e)

## E-YEB
```eyeb
print "Hello World"
```
[ソースファイル](../languages/E-YEB)

## EASY
```easy
print "Hello World"
```
[ソースファイル](../languages/EASY)

## ECMAScript
```javascript
print("Hello World");
```
[ソースファイル](../languages/ECMAScript.js)

## ED
```ed
a
Hello World
.
p
q
```
[ソースファイル](../languages/ED.ed)

## EDIF
```edif
(edif hello (edifVersion 2 0 0) (edifLevel 0) (keywordMap (keywordLevel 0))
  (info "Hello World")
)
```
[ソースファイル](../languages/EDIF.edif)

## EGL
```egl
program HelloWorld
    function main()
        SysLib.writeStdout("Hello World");
    end
end
```
[ソースファイル](../languages/EGL.egl)

## Eiffel
```eiffel
class HELLO_WORLD
create make
feature
   make is
   do print("Hello World%N") end
end
```
[ソースファイル](../languages/Eiffel.e)

## Elaine
```elaine
print "Hello World"
```
[ソースファイル](../languages/Elaine)

## Elena
```elena
public program
{
    eval() { console.writeLine("Hello World") }
}
```
[ソースファイル](../languages/Elena.l)

## Elm
```elm
import Html exposing (text)
main = text "Hello World"
```
[ソースファイル](../languages/Elm.elm)

## Elm 0.19
```elm
module Main exposing (main)
import Html exposing (text)
main = text "Hello World"
```
[ソースファイル](../languages/Elm 0.19.elm)

## Elvish
```elvish
echo "Hello World"
```
[ソースファイル](../languages/Elvish.elv)

## Emoticon
```emoticon
Hello World :-P
```
[ソースファイル](../languages/Emoticon.emoticon)

## Engen
```engen
print "Hello World"
```
[ソースファイル](../languages/Engen)

## Epiphany
```epiphany
print "Hello World"
```
[ソースファイル](../languages/Epiphany)

## Euphoria
```euphoria
puts(1, "Hello World\n")
```
[ソースファイル](../languages/Euphoria.ex)

## Everest
```everest
print "Hello World"
```
[ソースファイル](../languages/Everest)

## Exec 2
```exec2
&TYPE Hello World
```
[ソースファイル](../languages/Exec 2)

## Expect
```expect
send_user "Hello World\n"
```
[ソースファイル](../languages/Expect.exp)

## F
```f
print *, "Hello World"
end
```
[ソースファイル](../languages/F.f)

## F-Sharp
```fsharp
printfn "Hello World"
```
[ソースファイル](../languages/F-Sharp.fs)

## F77
```f77
      PROGRAM HELLOW
      WRITE(UNIT=*, FMT=*) 'Hello World'
      END
```
[ソースファイル](../languages/F77.f77)

## FALSE
```false
"Hello World
"
```
[ソースファイル](../languages/FALSE.f)

## FAX
```fax
print "Hello World"
```
[ソースファイル](../languages/FAX)

## FOCAL
```focal
TYPE "Hello World",!
```
[ソースファイル](../languages/FOCAL)

## FONT
```font
print "Hello World"
```
[ソースファイル](../languages/FONT)

## FOX-BASIC
```fox
? "Hello World"
```
[ソースファイル](../languages/FOX-BASIC)

## FSH
```fsh
echo "Hello World"
```
[ソースファイル](../languages/FSH.fsh)

## FTH
```fth
." Hello World" cr
```
[ソースファイル](../languages/FTH.fth)

## Factor
```factor
USING: io ;
"Hello World" print
```
[ソースファイル](../languages/Factor.factor)

## Fantom
```fantom
class HelloWorld {
  static Void main() { echo("Hello World") }
}
```
[ソースファイル](../languages/Fantom.fan)

## Fanx
```fanx
print "Hello World"
```
[ソースファイル](../languages/Fanx)

## Fasm
```asm
format ELF64
public _start
section '.text' executable
_start:
    mov edx, 12
    mov rsi, msg
    mov edi, 1
    mov eax, 1
    syscall
    mov edi, 0
    mov eax, 60
    syscall
section '.data' writeable
msg db 'Hello World', 10
```
[ソースファイル](../languages/Fasm.asm)

## Felix
```felix
print "Hello World"; println;
```
[ソースファイル](../languages/Felix.flx)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 5 はこちら](minor_5.md)