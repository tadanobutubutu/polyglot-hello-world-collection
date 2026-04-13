# Legacy Languages Exhibition Hall

The titans of the past that laid the foundation for modern computing.

---

### FORTRAN

```fortran
      PROGRAM HELLO
      PRINT *, 'Hello World'
      END
```

[Source File](../languages/FORTRAN)

---

### COBOL

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.
       PROCEDURE DIVISION.
           DISPLAY 'Hello World'.
           STOP RUN.
```

[Source File](../languages/COBOL)

---

### ALGOL 60

```algol
begin
  outstring(1, "Hello World");
end
```

[Source File](../languages/ALGOL%2060.algol)

---

### BASIC

```basic
10 PRINT "Hello World"
20 END
```

[Source File](../languages/BASIC)

---

### Pascal

```pascal
program HelloWorld;
begin
  writeln('Hello World');
end.
```

[Source File](../languages/Pascal.pas)

---

### Ada

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
  Put_Line ("Hello World");
end Hello;
```

[Source File](../languages/Ada.adb)

---

### Lisp

```lisp
(write-line "Hello World")
```

[Source File](../languages/Lisp.lisp)

---

### Smalltalk

```smalltalk
Transcript show: 'Hello World'; cr.
```

[Source File](../languages/Smalltalk.st)

---

### PL/I

```pli
HELLO: PROCEDURE OPTIONS (MAIN);
  PUT LIST ('Hello World');
END HELLO;
```

[Source File](../languages/PL-I.pli)

---

### Forth

```forth
." Hello World" CR
```

[Source File](../languages/Forth.fs)

---

### Simula

```simula
Begin
   OutText ("Hello World");
   Outimage;
End;
```

[Source File](../languages/Simula.sim)

---

### BCPL

```bcpl
GET "LIBHDR"
LET START() BE
$(
    WRITES("Hello World*N")
$)
```

[Source File](../languages/BCPL.bcpl)

---

### B

```b
main() {
  putchar('hell');
  putchar('o wo');
  putchar('rld\n');
}
```

[Source File](../languages/B.b)

---

### Assembly (x86)

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

[Back to README](../README.md)
