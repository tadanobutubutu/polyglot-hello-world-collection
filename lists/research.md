# Research Languages

41 curated entries.

##### Agda
```text
-- Hello world in Agda

module hello where
  open import IO
  main = run (putStrLn "Hello, World!")
```
[Source File](../libraries/a/A-2/Agda)

##### Agda
```text
module agda where
open import IO

main = run (putStrLn "Hello World")
```
[Source File](../libraries/a/A-1/Agda.agda)

##### AntLang
```text
echo["Hello, World!"]
```
[Source File](../libraries/a/A-3/AntLang)

##### AntLang
```text
"Hello World"
```
[Source File](../libraries/a/A-2/AntLang.ant)

##### ATS
```text
// Hello world in ATS

implement main () = begin
  print ("Hello, world!"); print_newline ()
end
```
[Source File](../libraries/a/A-4/ATS)

##### ATS2
```text
implement main0 () = println! "Hello World"
```
[Source File](../libraries/a/A-3/ATS2.dats)

##### Batsh
```text
// Hello world in Batsh

println("Hello world!");
```
[Source File](../libraries/b/B-1/Batsh)

##### Batsh
```text
println("Hello World");
```
[Source File](../libraries/b/B-1/Batsh.batsh)

##### Clean
```text
// Hello World in Clean

module hello

Start :: String
Start = "Hello World!\n"
```
[Source File](../libraries/c/C-3/Clean)

##### Clean
```text
module hello
Start :: {#Char}
Start = "Hello World"
```
[Source File](../libraries/c/C-2/Clean.icl)

##### Coq
```text
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

##### Curry  _PAKCS
```text
main = putStr "Hello, World!"
```
[Source File](../libraries/c/C-4/Curry  _PAKCS)

##### Curry  _Sloth
```text
import IO

main = putStr "Hello, World!"
```
[Source File](../libraries/c/C-4/Curry  _Sloth)

##### Curry _PAKCS
```text
main = putStr "Hello, World!"
```
[Source File](../libraries/c/C-3/Curry _PAKCS.curry)

##### Curry _Sloth
```text
import IO

main = putStr "Hello, World!"
```
[Source File](../libraries/c/C-3/Curry _Sloth.curry)

##### Curry
```text
-- "Hello World" demo for the Tcl/Tk library

import Tk

main = runWidget "Hello"
          (TkCol [] [TkLabel [TkText "Hello World"],
                     TkButton tkExit [TkText "Stop"]])
```
[Source File](../libraries/c/C-3/Curry.curry)

##### Dotlang
```text
•v
 #`Hello World`
 #
```
[Source File](../libraries/d/D-2/Dotlang)

##### Fetlang
```text
(Hello world in Fetlang)

Make slave scream "Hello World!"
```
[Source File](../libraries/f/F-1/Fetlang)

##### Fetlang
```text
Make slave scream "Hello World"
```
[Source File](../libraries/f/F-1/Fetlang.fet)

##### Idris
```text
-- Hello world in Idris

module Main

main : IO ()
main = putStrLn "Hello world"
```
[Source File](../libraries/i/I-1/Idris)

##### Idris
```text
module Main

main : IO ()
main = putStrLn "Hello World"
```
[Source File](../libraries/i/I-1/Idris.idr)

##### Isabelle
```text
theory Scratch
  imports Main
begin
  value ‹''Hello world!''›
end
```
[Source File](../libraries/i/I-4/Isabelle)

##### Lean
```text
#print "Hello, World!"
```
[Source File](../libraries/l/L-1/Lean)

##### Lean Mean Bean Machine
```text
OOOOOOOOOOOOO
"""""""""""""
Hello, World!
UUUUUUUUUUUUU
```
[Source File](../libraries/l/L-1/Lean Mean Bean Machine.lmbm)

##### Lean
```text
#print "Hello World"
```
[Source File](../libraries/l/L-1/Lean.lean)

##### ListLang
```text
0dlroW391+*2+491+*4+olleH["],
```
[Source File](../libraries/l/L-1/ListLang)

##### MATLAB
```text
% Hello World in MATLAB.

disp('Hello World');
```
[Source File](../libraries/m/M-1/MATLAB)

##### MATLAB 1.0
```text
fprintf('Hello World\n')
```
[Source File](../libraries/m/M-1/MATLAB 1.0.m)

##### MATLAB
```text
disp('Hello World')
```
[Source File](../libraries/m/M-1/MATLAB.m)

##### Mercury
```text
:- module hello.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.

:- implementation.
main(!IO) :-
	io.write_string("Hello World\n", !IO).
```
[Source File](../libraries/m/M-1/Mercury.m)

##### Poketlang
```text
print("Hello World")
```
[Source File](../libraries/p/P-2/Poketlang.pk)

##### Prolog  _Ciao
```text
main :-
     write('Hello, World!').
```
[Source File](../libraries/p/P-4/Prolog  _Ciao)

##### Prolog  _SWI
```text
?-write('Hello, World!').
```
[Source File](../libraries/p/P-4/Prolog  _SWI)

##### Prolog _Ciao
```text
main :-
     write('Hello, World!').
```
[Source File](../libraries/p/P-2/Prolog _Ciao.prolog)

##### Prolog _SWI
```text
?-write('Hello, World!').
```
[Source File](../libraries/p/P-2/Prolog _SWI.prolog)

##### Prolog
```text
helloWorld :-
  write('Hello World').

:- helloWorld.
```
[Source File](../libraries/p/P-2/Prolog.pro)

##### Setlang
```text
("Hello World!")
```
[Source File](../libraries/s/S-1/Setlang)

##### Stack Cats
```text
-*(:^-_-_:-_:-_:-_:-_-_:[:^]]:^!-*!->[!_>[!_>[{]>[^-_-_:]]<<<}>[!-:^[[\\>]:^[[>:[>:^[<<]]\\>[*>+:^:-_]:^[[-_*[>>>[-_[/<]>+^[>[<<]]*>[)
```
[Source File](../libraries/s/S-3/Stack Cats.stackcats)

##### TESTLANG
```text
out Hello, out char 32 out world! end
```
[Source File](../libraries/t/T-1/TESTLANG)

##### Visual Prolog
```text
/* Hello World in Visual Prolog */

goal
    console::init(),
    stdio::write("Hello World!").
```
[Source File](../libraries/nonenglish/Visual Prolog)

##### WhatLang
```text
`Hello, world!\n`
```
[Source File](../libraries/w/W-2/WhatLang)

