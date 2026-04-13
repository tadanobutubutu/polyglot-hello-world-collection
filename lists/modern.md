# Modern Languages

The latest and greatest in the programming world. High-performance, memory-safe, and productive.

---

### Carbon

```cpp
package Sample api;
fn Main() -> i32 {
    Print(\"Hello World\");
    return 0;
}
```

[Source File](../languages/Carbon.carbon)

### Clojure

```clojure
(println \"Hello World\")
```

[Source File](../languages/Clojure.clj)

### Crystal

```crystal
puts \"Hello World\"
```

[Source File](../languages/Crystal.cr)

### D

```d
import std.stdio;
void main() {
    writeln(\"Hello World\");
}
```

[Source File](../languages/D.d)

### Dart

```dart
void main() {
  print('Hello World');
}
```

[Source File](../languages/Dart.dart)

### Elixir

```elixir
IO.puts \"Hello World\"
```

[Source File](../languages/Elixir.ex)

### Elm

```elm
import Html exposing (text)
main = text \"Hello World\"
```

[Source File](../languages/Elm.elm)

### Erlang

```erlang
-module(hello).
-export([hello_world/0]).
hello_world() -> io:format(\"Hello World~n\").
```

[Source File](../languages/Erlang.erl)

### F#

```fsharp
printfn \"Hello World\"
```

[Source File](../languages/F#.fs)

### Gleam

```gleam
import gleam/io
pub fn main() {
  io.println(\"Hello World\")
}
```

[Source File](../languages/Gleam.gleam)

### Groovy

```groovy
println \"Hello World\"
```

[Source File](../languages/Groovy.groovy)

### Hack

```hack
<?hh
<<__EntryPoint>>
function main(): void {
  echo \"Hello World\\n\";
}
```

[Source File](../languages/Hack.hh)

### Haskell

```haskell
main = putStrLn \"Hello World\"
```

[Source File](../languages/Haskell.hs)

### Haxe

```haxe
class Main {
    static function main() {
        trace(\"Hello World\");
    }
}
```

[Source File](../languages/Haxe.hx)

### Julia

```julia
println(\"Hello World\")
```

[Source File](../languages/Julia.jl)

### Lua

```lua
print(\"Hello World\")
```

[Source File](../languages/Lua.lua)

### Nim

```nim
echo \"Hello World\"
```

[Source File](../languages/Nim.nim)

### OCaml

```ocaml
print_endline \"Hello World\"
```

[Source File](../languages/OCaml.ml)

### Perl

```perl
print \"Hello World\\n\";
```

[Source File](../languages/Perl.pl)

### R

```r
cat(\"Hello World\\n\")
```

[Source File](../languages/R.R)

### Racket

```racket
#lang racket
(displayln \"Hello World\")
```

[Source File](../languages/Racket.rkt)

### ReScript

```rescript
Js.log(\"Hello World\")
```

[Source File](../languages/ReScript.res)

### Rust

```rust
fn main() {
    println!(\"Hello World\")
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
print(\"Hello World\")
```

[Source File](../languages/Swift.swift)

### Tcl

```tcl
puts \"Hello World\"
```

[Source File](../languages/Tcl.tcl)

### TypeScript

```typescript
console.log(\"Hello World\")
```

[Source File](../languages/TypeScript.ts)

### V

```v
println(\"Hello World\")
```

[Source File](../languages/V.v)

### Vala

```vala
static void main (string[] args)
{
	stdout.printf (\"Hello World\\n\")
}
```

[Source File](../languages/Vala.vala)

### WebAssembly

```wat
(module
    (import \"wasi_unstable\" \"fd_write\"
        (func $fd_write (param i32 i32 i32 i32) (result i32))
    )
    (memory 1)
    (export \"memory\" (memory 0))
    (data (i32.const 0) \"\\08\\00\\00\\00\\0c\\00\\00\\00Hello World\\n\")
    (func $main (export \"_start\")
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
IO.print(\"Hello World\")
```

[Source File](../languages/Wren.wren)

### Zig

```zig
const std = @import(\"std\")
pub fn main() !void {
    const stdout = std.io.getStdOut().writer()
    try stdout.print(\"Hello World\", .{})
}
```

[Source File](../languages/Zig.zig)

---

[Back to README](../README.md)
