[← Back to Home](../README.md)

# Research Languages

Theoretical and academic programming languages.

##### Coq
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
[Source File](../libraries/c/C-3/Coq.v)

##### Agda
```agda
module agda where
open import IO

main = run (putStrLn "Hello World")
```
[Source File](../libraries/a/A-1/Agda.agda)

##### Idris
```idr
module Main

main : IO ()
main = putStrLn "Hello World"
```
[Source File](../libraries/i/I-1/Idris.idr)

##### Lean
```lean
#print "Hello World"
```
[Source File](../libraries/l/L-1/Lean.lean)

##### Mercury
```m
:- module hello.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.

:- implementation.
main(!IO) :-
	io.write_string("Hello World
", !IO).
```
[Source File](../libraries/m/M-1/Mercury.m)


[← Back to Home](../README.md)
