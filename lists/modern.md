# Modern Languages

High-performance, memory-safe, and contemporary programming languages. Consolidated for a seamless museum experience.

---

### Carbon

```cpp
package Sample api;

fn Main() -> i32 {
    Print("Hello World");
    return 0;
}
```

[Source File](../languages/Carbon.carbon)

---

### Crystal

```crystal
puts "Hello World"
```

[Source File](../languages/Crystal.cr)

---

### D

```d
import std.stdio;

void main() {
    writeln("Hello World");
}
```

[Source File](../languages/D.d)

---

### Dart

```dart
void main() {
  print('Hello World');
}
```

[Source File](../languages/Dart.dart)

---

### Elixir

```elixir
IO.puts "Hello World"
```

[Source File](../languages/Elixir.ex)

---

### Elm

```elm
import Html exposing (text)

main =
  text "Hello World"
```

[Source File](../languages/Elm.elm)

---

### F#

```fsharp
printfn "Hello World"
```

[Source File](../languages/F#.fs)

---

### Grain

```grain
print("Hello World")
```

[Source File](../languages/Grain.gr)

---

### Mojo

```mojo
fn main():
    print("Hello World")
```

[Source File](../languages/Mojo.mojo)

---

### Nim

```nim
echo "Hello World"
```

[Source File](../languages/Nim.nim)

---

### Pony

```pony
actor Main
  new create(env: Env) =>
    env.out.print("Hello World")
```

[Source File](../languages/Pony.pony)

---

### Swift

```swift
print("Hello World")
```

[Source File](../languages/Swift.swift)

---

### V

```v
fn main() {
    println('Hello World')
}
```

[Source File](../languages/V.v)

---

### Vala

```vala
void main() {
    print("Hello World\n");
}
```

[Source File](../languages/Vala.vala)

---

### WebAssembly

```wat
(module
    (import "wasi_unstable" "fd_write"
        (func $fd_write (param i32 i32 i32 i32) (result i32))
    )

    (memory 1)
    (export "memory" (memory 0))

    (data (i32.const 0) "\08\00\00\00\0c\00\00\00Hello World\n")

    (func $main (export "_start")
        i32.const 1
        i32.const 0
        i32.const 1
        i32.const 20
        call $fd_write
        drop
    )
)
```

[Source File](../languages/WebAssembly.wat)

---

### Wren

```wren
IO.print("Hello World")
```

[Source File](../languages/Wren.wren)

---

### Zig

```zig
const std = @import("std");

pub fn main() !void {
    std.debug.print("Hello World\n", .{});
}
```

[Source File](../languages/Zig.zig)

---

[Back to README](../README.md)
