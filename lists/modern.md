# Modern Languages

State-of-the-art programming languages with standard hello-world implementations. Consolidated for a seamless museum experience.

---

### Bun

```javascript
console.log("Hello World");
```

[Source File](../languages/Bun.js)

### Carbon

```carbon
package HelloWorld api
fn Main() -> i32 {
  Print("Hello World")
  return 0
}
```

[Source File](../languages/Carbon.carbon)

### Crystal

```crystal
puts "Hello World"
```

[Source File](../languages/Crystal.cr)

### Dart

```dart
main() {
  print('Hello World')
}
```

[Source File](../languages/Dart.dart)

### Elixir

```elixir
IO.puts "Hello World"
```

[Source File](../languages/Elixir.ex)

### Elm

```elm
import Html exposing (text)
main =
  text "Hello World"
```

[Source File](../languages/Elm.elm)

### F#

```fsharp
printfn "Hello World"
```

[Source File](../languages/FSharp.fs)

### Gleam

```gleam
import gleam/io
pub fn main() {
  io.println("Hello World")
}
```

[Source File](../languages/Gleam.gleam)

### Go

```go
package main
import "fmt"
func main() {
  fmt.Println("Hello World")
}
```

[Source File](../languages/Go.go)

### Haxe

```haxe
class HelloWorld {
    static function main() {
        trace("Hello World")
    }
}
```

[Source File](../languages/Haxe.hx)

### Idris

```idris
module Main
main : IO ()
main = putStrLn "Hello World"
```

[Source File](../languages/Idris.idr)

### Kotlin

```kotlin
fun main() {
  println("Hello World")
}
```

[Source File](../languages/Kotlin.kt)

### Mojo

```python
fn main():
    print("Hello World")
```

[Source File](../languages/Mojo.mojo)

### Nim

```nim
echo("Hello World")
```

[Source File](../languages/Nim.nim)

### Odin

```odin
package main
import "core:fmt"
main :: proc() {
  fmt.println("Hello World")
}
```

[Source File](../languages/Odin.odin)

### PureScript

```haskell
module Main where
import Debug.Trace
main = trace "Hello World"
```

[Source File](../languages/PureScript.purs)

### Reason

```ocaml
print_string "Hello World"
```

[Source File](../languages/Reason.re)

### ReScript

```rescript
Js.log("Hello World")
```

[Source File](../languages/ReScript.res)

### Rust

```rust
fn main() {
    println!("Hello World")
}
```

[Source File](../languages/Rust.rs)

### Solidity

```solidity
pragma solidity ^0.8.9
contract HelloWorld {
    function render () public pure returns (string memory) {
        return 'Hello World'
    }
}
```

[Source File](../languages/Solidity.sol)

### Swift

```swift
print("Hello World")
```

[Source File](../languages/Swift.swift)

### Tcl

```tcl
puts "Hello World"
```

[Source File](../languages/Tcl.tcl)

### TypeScript

```typescript
console.log("Hello World")
```

[Source File](../languages/TypeScript.ts)

### V

```v
println("Hello World")
```

[Source File](../languages/V.v)

### Vala

```vala
static void main (string[] args)
{
	stdout.printf ("Hello World\n")
}
```

[Source File](../languages/Vala.vala)

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

### Wren

```wren
IO.print("Hello World")
```

[Source File](../languages/Wren.wren)

### Zig

```zig
const std = @import("std")
pub fn main() !void {
    const stdout = std.io.getStdOut().writer()
    try stdout.print("Hello World", .{})
}
```

[Source File](../languages/Zig.zig)

---

[Back to README](../README.md)
