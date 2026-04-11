# マイナー言語 Part 16

収録数: 50

---

## V-BASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/V-BASIC.bas)

## V-CORE
```vcore
print "Hello World"
```
[ソースファイル](../languages/V-CORE)

## V-NET
```vnet
print "Hello World"
```
[ソースファイル](../languages/V-NET)

## V3
```v3
print "Hello World"
```
[ソースファイル](../languages/V3)

## Vala
```vala
void main() { print("Hello World\n"); }
```
[ソースファイル](../languages/Vala.vala)

## Valie
```valie
print "Hello World"
```
[ソースファイル](../languages/Valie)

## Valkyrie
```valkyrie
print "Hello World"
```
[ソースファイル](../languages/Valkyrie)

## Van
```van
print "Hello World"
```
[ソースファイル](../languages/Van)

## Vas
```vas
print "Hello World"
```
[ソースファイル](../languages/Vas)

## Vast
```vast
print "Hello World"
```
[ソースファイル](../languages/Vast)

## Vault
```vault
print "Hello World"
```
[ソースファイル](../languages/Vault)

## Vaxe
```vaxe
print "Hello World"
```
[ソースファイル](../languages/Vaxe)

## Veale
```veale
print "Hello World"
```
[ソースファイル](../languages/Veale)

## Vento
```vento
print "Hello World"
```
[ソースファイル](../languages/Vento)

## Verilog
```verilog
module main; initial begin $display("Hello World"); $finish; end endmodule
```
[ソースファイル](../languages/Verilog.v)

## VHDL
```vhdl
use std.textio.all;
entity hello is end hello;
architecture sim of hello is
begin
  process begin
    variable l: line;
    write(l, string'("Hello World"));
    writeline(output, l);
    wait;
  end process;
end sim;
```
[ソースファイル](../languages/VHDL.vhd)

## Vim Script
```vim
echo "Hello World"
```
[ソースファイル](../languages/Vim Script.vim)

## Visual Basic
```vb
Module Hello
  Sub Main()
    Console.WriteLine("Hello World")
  End Sub
End Module
```
[ソースファイル](../languages/Visual Basic.vb)

## Visual Basic .NET
```vbnet
Module Hello
  Sub Main()
    Console.WriteLine("Hello World")
  End Sub
End Module
```
[ソースファイル](../languages/Visual Basic .NET.vb)

## Visual Basic For Applications
```vba
Sub Hello()
  MsgBox "Hello World"
End Sub
```
[ソースファイル](../languages/Visual Basic For Applications.vba)

## Visual FoxPro
```foxpro
? "Hello World"
```
[ソースファイル](../languages/Visual FoxPro.prg)

## Visual Objects
```vo
FUNCTION Start()
  ? "Hello World"
RETURN
```
[ソースファイル](../languages/Visual Objects.prg)

## Visual Prolog
```prolog
main() :- write("Hello World\n").
```
[ソースファイル](../languages/Visual Prolog.pro)

## Volt
```volt
module main; import watt.io; void main() { print("Hello World\n"); }
```
[ソースファイル](../languages/Volt.volt)

## Vrml
```vrml
Text { string "Hello World" }
```
[ソースファイル](../languages/Vrml.wrl)

## Vtml
```html
<vtml>Hello World</vtml>
```
[ソースファイル](../languages/Vtml)

## Vue
```vue
<template><div>{{ msg }}</div></template>
<script>export default { data() { return { msg: 'Hello World' } } }</script>
```
[ソースファイル](../languages/Vue.vue)

## Vyper
```vyper
@external
@view
def greet() -> String[24]:
    return "Hello World"
```
[ソースファイル](../languages/Vyper.vy)

## W-BASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/W-BASIC.bas)

## W-CORE
```wcore
print "Hello World"
```
[ソースファイル](../languages/W-CORE)

## WA-BASIC
```bas
PRINT "Hello World"
```
[ソースファイル](../languages/WA-BASIC.bas)

## WASM
```wasm
(module
  (import "console" "log" (func $log (param i32 i32)))
  (data (i32.const 0) "Hello World")
  (func (export "main") (call $log (i32.const 0) (i32.const 11)))
)
```
[ソースファイル](../languages/WASM.wat)

## WEB
```web
@* Hello World in WEB.
@c
print("Hello World\n");
```
[ソースファイル](../languages/WEB.web)

## WML
```xml
<wml><card><p>Hello World</p></card></wml>
```
[ソースファイル](../languages/WML.wml)

## WSH
```javascript
WScript.Echo("Hello World");
```
[ソースファイル](../languages/WSH.vbs)

## Wade
```wade
print "Hello World"
```
[ソースファイル](../languages/Wade)

## Wake
```wake
print "Hello World"
```
[ソースファイル](../languages/Wake.wake)

## Warp
```warp
print "Hello World"
```
[ソースファイル](../languages/Warp)

## Wave
```wave
print "Hello World"
```
[ソースファイル](../languages/Wave)

## Way
```way
print "Hello World"
```
[ソースファイル](../languages/Way)

## WebAssembly
```wasm
(module (func $main (import "env" "print") (param i32)) (data (i32.const 0) "Hello World\00") (export "main" (func $main)))
```
[ソースファイル](../languages/WebAssembly.wat)

## WebIDL
```webidl
// No print in IDL, just definitions
```
[ソースファイル](../languages/WebIDL.webidl)

## WebVTT
```vtt
WEBVTT
00:01.000 --> 00:04.000
Hello World
```
[ソースファイル](../languages/WebVTT.vtt)

## Whiley
```whiley
import whiley.lang.System
method main(System.Console console):
    console.out.println("Hello World")
```
[ソースファイル](../languages/Whiley.whiley)

## Wimple
```wimple
print "Hello World"
```
[ソースファイル](../languages/Wimple)

## Winforth
```forth
." Hello World" cr
```
[ソースファイル](../languages/Winforth)

## Winview
```winview
print "Hello World"
```
[ソースファイル](../languages/Winview)

## Wirk
```wirk
print "Hello World"
```
[ソースファイル](../languages/Wirk)

## Wise
```wise
print "Hello World"
```
[ソースファイル](../languages/Wise)

## Wolfram Language
```wolfram
Print["Hello World"]
```
[ソースファイル](../languages/Wolfram Language.wl)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 17 はこちら](minor_17.md)