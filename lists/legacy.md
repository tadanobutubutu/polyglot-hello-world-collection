# Legacy Languages

Historical and classic programming languages that shaped the industry. Consolidated for a seamless museum experience.

---

### ABAP

```
REPORT ZHELLO_WORLD.

START-OF-SELECTION.
    WRITE: 'Hello World'.
```

[Source File](../languages/A/ABAP.abap)

---

### ABC

```
WRITE "Hello World"
```

[Source File](../languages/A/ABC.abc)

---

### APL

```
⎕←'Hello World'
```

[Source File](../languages/A/APL.apl)

---

### ActionScript 3

```
package {

import flash.display.Sprite;
import flash.text.TextField;
import flash.text.TextFieldAutoSize;
import flash.text.TextFormat;

[SWF(width='800', height='600', backgroundColor='#cccccc', frameRate='30')]

	public class HelloFlash extends Sprite
	{
		public function HelloFlash()
		{
			var format:TextFormat = new TextFormat();
			format.font = "Arial";
			format.size = 20;
			format.color = 0x0000;

			var textField:TextField = new TextField();
			textField.defaultTextFormat = format;

			textField.border = false;
			textField.autoSize = TextFieldAutoSize.LEFT;
			textField.selectable = false;

			textField.text = "Hello World";
			addChild(textField);


		}
	}
}
```

[Source File](../languages/A/ActionScript%203.as)

---

### Ada

```ada
with Ada.Text_IO;

procedure Hello_World is
   use Ada.Text_IO;
begin
   Put_line ("Hello World");
end Hello_World;
```

[Source File](../languages/A/Ada.adb)

---

### Algol 60

```
BEGIN
  DISPLAY "Hello World"
END.
```

[Source File](../languages/Algol%2060.algol60)

---

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
    mov edx, 12
    int 0x80
    mov eax, 1
    int 0x80
```

[Source File](../languages/Assembly.asm)

---

### AutoIt

```
Print, Hello World
```

[Source File](../languages/AutoIt.au3)

---

### BCPL

```
main() {
  BCPL.writef("Hello World\n");
}
```

[Source File](../languages/BCPL.bcpl)

---

### Forth

```
.( Hello World)
```

[Source File](../languages/Forth.fth)

---

### Fortran

```fortran
print *,'Hello World'
end
```

[Source File](../languages/Fortran.f90)

---

### Lisp

```
(format t "Hello World~%")
```

[Source File](../languages/Lisp.lisp)

---

### Pascal

```
program HelloWorld(output);
begin
        writeln('Hello World');
end.
```

[Source File](../languages/Pascal.p)

---

### Prolog

```
helloWorld :-
  write('Hello World').

:- helloWorld.
```

[Source File](../languages/Prolog.pro)

---

### Scheme

```scheme
(display "Hello World")
(newline)
```

[Source File](../languages/Scheme.scm)

---

### Smalltalk

```
Transcript show: 'Hello World'.
```

[Source File](../languages/SmallTalk.sm)

---

### Standard ML

```
fun hello() = print("Hello World\n");

hello()
```

[Source File](../languages/Standard%20ML.sml)

---

### VHDL

```
use std.textio.all;

entity hello_world is
end hello_world;

architecture behaviour of hello_world is
begin
	process
    begin
       write (output, String'("Hello World"));
       wait;
    end process;
end behaviour;
```

[Source File](../languages/VHDL.vhdl)

---

### Verilog

```coq
module main;
  initial
    begin
      $display("Hello World");
      $finish;
    end
endmodule
```

[Source File](../languages/Verilog.v)

---

### Visual Basic

```
Module HelloWorld
    Sub Main()
        MsgBox("Hello World")
    End Sub
End Module
```

[Source File](../languages/Visual%20Basic.vb)

---

[Back to README](../README.md)
