# Research カテゴリー

収録数: 11

---

## Agda
```agda
module agda where
open import IO

main = run (putStrLn "Hello World")
```
[ソースファイル](../languages/Agda.agda)

## Coq
```v
Require Import Coq.Lists.List.
Require Import Io.All.
Require Import Io.System.All.
Require Import ListString.All.

Import ListNotations.
Import C.Notations.

(** The classic Hello World program. *)
Definition hello_world (argv : list LString.t) : C.t System.effect unit :=
  System.log (LString.s "Hello World").
```
[ソースファイル](../languages/Coq.v)

## Curry
```curry
-- "Hello World" demo for the Tcl/Tk library

import Tk

main = runWidget "Hello"
          (TkCol [] [TkLabel [TkText "Hello World"],
                     TkButton tkExit [TkText "Stop"]])
```
[ソースファイル](../languages/Curry.curry)

## Elixir
```exs
#!/usr/bin/env elixir
IO.puts "Hello World"
```
[ソースファイル](../languages/Elixir.exs)

## Elixir
```ex
IO.puts "Hello World"
```
[ソースファイル](../languages/Elixir.ex)

## Erlang
```erl
-module(erlang_hw).
-export([start/0]).

start() ->
  io:format("Hello World~n").
```
[ソースファイル](../languages/Erlang.erl)

## Erlang EScript
```erl
#!/usr/bin/env escript

main(_) ->
    io:format("Hello World~n").
```
[ソースファイル](../languages/Erlang EScript.erl)

## Gocaml
```ml
println_str "Hello World"
```
[ソースファイル](../languages/Gocaml.ml)

## Idris
```idr
module Main

main : IO ()
main = putStrLn "Hello World"
```
[ソースファイル](../languages/Idris.idr)

## OCaml
```ml
print_string "Hello World\n"
```
[ソースファイル](../languages/OCaml.ml)

## Standard ML
```sml
fun hello() = print("Hello World\n");

hello()
```
[ソースファイル](../languages/Standard ML.sml)

---
### 🚀 次のリストへ進む
**[マイナー言語 Part 1 はこちら](minor_1.md)**