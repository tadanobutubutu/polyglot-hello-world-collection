# Legacy Languages

Historical and classic programming languages that shaped the industry. Consolidated for a seamless museum experience.

---

### ABAP

```abap
REPORT ZHELLO_WORLD.
START-OF-SELECTION.
    WRITE: 'Hello World'.
```

[Source File](../languages/ABAP.abap)

### ABC

```abc
WRITE \"Hello World\"
```

[Source File](../languages/ABC.abc)

### ActionScript 3

```actionscript
package {
import flash.display.Sprite
import flash.text.TextField
public class HelloFlash extends Sprite {
    public function HelloFlash() {
        var textField:TextField = new TextField()
        textField.text = \"Hello World\"
        addChild(textField)
    }
}
}
```

[Source File](../languages/ActionScript%203.as)

### Ada

```ada
with Ada.Text_IO;
procedure Hello_World is
begin
   Ada.Text_IO.Put_Line (\"Hello World\");
end Hello_World;
```

[Source File](../languages/Ada.adb)

### Algol 60

```algol
BEGIN
  FILE F(KIND=REMOTE);
  WRITE(F, *, \"HELLO WORLD\");
END.
```

[Source File](../languages/Algol%2060.algol60)

### Algol 68

```algol
print((\"Hello World\", newline))
```

[Source File](../languages/Algol%2068.a68)

### APL

```apl
⎕←'Hello World'
```

[Source File](../languages/APL.apl)

### Assembly

```asm
section .data
    msg db 'Hello World', 0xa
section .text
    global _start
_start:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, 13
    int 0x80
    mov eax, 1
    int 0x80
```

[Source File](../languages/Assembly.asm)

### AutoIt

```autoit
MsgBox(0, \"Message Box\", \"Hello World\")
```

[Source File](../languages/AutoIt.au3)

### BASIC

```basic
10 PRINT \"Hello World\"
20 END
```

[Source File](../languages/BASIC.bas)

### BCPL

```bcpl
GET \"LIBHDR\"
LET START() BE
{
  WRITES(\"Hello World*N\")
}
```

[Source File](../languages/BCPL.bcpl)

### COBOL

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
PROCEDURE DIVISION.
    DISPLAY 'Hello World'.
    STOP RUN.
```

[Source File](../languages/Cobol.cobol)

### Forth

```forth
.\" Hello World\" CR
```

[Source File](../languages/Forth.forth)

### Fortran

```fortran
print *,'Hello World'
end
```

[Source File](../languages/Fortran.f90)

### Lisp

```lisp
(print \"Hello World\")
```

[Source File](../languages/Lisp.lisp)

### Logo

```logo
print [Hello World]
```

[Source File](../languages/Logo.logo)

### Objective-C

```objectivec
#import <Foundation/Foundation.h>
int main() {
    @autoreleasepool {
        NSLog(@\"Hello World\");
    }
    return 0;
}
```

[Source File](../languages/Objective-C.m)

### Pascal

```pascal
program HelloWorld;
begin
  writeln('Hello World');
end.
```

[Source File](../languages/Pascal.pas)

### Prolog

```prolog
main :- write('Hello World'), nl, halt.
```

[Source File](../languages/Prolog.pl)

### Scheme

```scheme
(display \"Hello World\") (newline)
```

[Source File](../languages/Scheme.scm)

### Smalltalk

```smalltalk
Transcript show: 'Hello World'; cr.
```

[Source File](../languages/Smalltalk.st)

### Standard ML

```sml
fun hello() = print(\"Hello World\\n\");
hello();
```

[Source File](../languages/Standard%20ML.sml)

### Verilog

```verilog
module main;
  initial begin
    $display(\"Hello World\");
    $finish;
  end
endmodule
```

[Source File](../languages/Verilog.v)

### VHDL

```vhdl
use std.textio.all;
entity hello is
end entity;
architecture sim of hello is
begin
  process
    variable l: line;
  begin
    write(l, string'(\"Hello World\"));
    writeline(output, l);
    wait;
  end process;
end architecture;
```

[Source File](../languages/VHDL.vhd)

### Visual Basic

```vb
Module HelloWorld
    Sub Main()
        MsgBox(\"Hello World\")
    End Sub
End Module
```

[Source File](../languages/Visual%20Basic.vb)

---

[Back to README](../README.md)
