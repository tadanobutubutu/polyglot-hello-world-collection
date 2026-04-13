# Research Languages

Academic and experimental paradigms showcasing the future of computation.

---

### Agda

```agda
module agda where
open import IO
main = run (putStrLn \"Hello World\")
```

[Source File](../languages/Agda.agda)

### Coq

```coq
Require Import Io.System.All.
Import ListNotations.
Definition hello_world : C.t System.effect unit :=
  System.log (LString.s \"Hello World\").
```

[Source File](../languages/Coq.v)

### J

```j
'Hello World'
```

[Source File](../languages/J.j)

### K

```k
\"Hello World\\n\"
```

[Source File](../languages/K.k)

---

[Back to README](../README.md)
