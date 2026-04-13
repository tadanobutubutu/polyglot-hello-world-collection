# Research Languages Exhibition Hall

Formal systems, academic proofs, and experimental logic.

---

### Coq

```coq
Require Import Io.Standard.
Definition main := print_line "Hello World".
```

[Source File](../languages/Coq.v)

---

### Lean

```lean
def main : IO Unit :=
  IO.println "Hello World"
```

[Source File](../languages/Lean.lean)

---

### Agda

```agda
module hello-world where
open import IO
main = run (putStrLn "Hello World")
```

[Source File](../languages/Agda.agda)

---

### Idris

```idris
module Main
main : IO ()
main = putStrLn "Hello World"
```

[Source File](../languages/Idris.idr)

---

### Prolog

```prolog
main :- write('Hello World'), nl.
```

[Source File](../languages/Prolog.pl)

---

### Mercury

```mercury
:- module hello.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
main(!IO) :- io.write_string("Hello World\n", !IO).
```

[Source File](../languages/Mercury.m)

---

### Curry

```curry
main = putStrLn "Hello World"
```

[Source File](../languages/Curry.curry)

---

[Back to README](../README.md)
