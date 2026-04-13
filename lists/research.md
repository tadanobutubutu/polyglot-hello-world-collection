# Research Languages

Academic and experimental paradigms showcasing the future of computation.

---

### Agda

```agda
module agda where
open import IO

main = run (putStrLn "Hello World")
```

[Source File](../languages/A/Agda.agda)

---

### Coq

```coq
class Main inherits IO {
   main(): Object {
		out_string("Hello World.\n")
   };
};
```

[Source File](../languages/Coq.v)

---

### J

```
print "Hello World"
```

[Source File](../languages/J.ijs)

---

[Back to README](../README.md)
