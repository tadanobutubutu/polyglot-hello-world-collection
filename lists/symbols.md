<div align="center">

# 🔣 Symbols & Numerals

Languages named with symbols or digits.

**85 exhibits** in this wing

[⬅ Museum entrance](../README.md) · [🏛 Full catalog](all.md)

</div>

---

## !

```text
!-
#_Hello World
-!
```
<sub>📄 [Source File](../libraries/symbols/!)</sub>

## !@#$%^&* __+

```text
 ^dlroW ,olleH(@)
```
<sub>📄 [Source File](../libraries/symbols/!@%23$%^&*%20__+)</sub>

## !@$%^&* _+

```text
 ^dlroW ,olleH(@)
```
<sub>📄 [Source File](../libraries/symbols/!@$%^&*%20_+)</sub>

## !@sharp$pct^andstar_+

```text
 ^dlroW ,olleH(@)
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/!@sharp$pct^andstar_+.ecndpcaalr)</sub>

## $+-?

```text
$+++++++++A?b$++++++++$-aB$
$+++C?d$++++++++++$-cD$-
+++++++

+++
$++++++++E?f$--------$-eF$---
------------
$+++++++++G?h$++++++$-gH$+
$++++++I?j$++++$-iJ$
+++
------
--------
$++++++++K?l$--------$-kL$---
```
<sub>📄 [Source File](../libraries/symbols/$+-?)</sub>

## %^2^-1

```text
spmmmmmmiiiiiiiieiepssipeepipe'spmmmmemmiiiesiiepipeiieiise'spmmmmpipse
```
<sub>📄 [Source File](../libraries/symbols/%^2^-1)</sub>

## *><>

```text
"Hello, World!"r>Ool?u!|;
```
<sub>📄 [Source File](../libraries/symbols/*><>)</sub>

## ++

```text
int main() {
  while (1) {
  }
}
```
<sub>📄 [Source File](../libraries/symbols/++)</sub>

## +++

```text
72 !$ 101 !$ +7 !$ !$ +3 !$ 44 !$ 32 !$ 87 !$ 111 !$ 114 !$ 108 !$ +-8 !$ 33 !$
```
<sub>📄 [Source File](../libraries/symbols/+++)</sub>

## +

```text
def run_plus_period_star(code: str, starting_input=''):
    pointer = 0  # for instructions
    location = 0  # for tape
    tape = [0]
    input_string = starting_input  # allows multiple inputs to happen easily

    while pointer < len(code):
        if code[pointer] == '>':
            location += 1
            if location == len(tape):
                tape.append(0)
        elif code[pointer] == '<':
            if location <= 0:
                raise ValueError('Cannot move left from position 0')
            location -= 1
        elif code[pointer] == '+':
            tape[location] = (tape[location] + 1) % 256
        elif code[pointer] == '-':
            tape[location] = (tape[location] - 1) % 256
        elif code[pointer] == '.':
            print(chr(tape[location]), end='')
        elif code[pointer] == ',':
            if input_string == '':
                input_string = input(">>")
            if len(input_string) > 0:
                tape[location] = ord(input_string[0])
                input_string = input_string[1:]
        elif code[pointer] == '*':
            if tape[location] == 0:
                pointer = -1
        pointer += 1
    return tape
```
<sub>📄 [Source File](../libraries/symbols/+.*)</sub>

## ,,,

```text
"Hello, World!
```
<sub>📄 [Source File](../libraries/symbols/,,,)</sub>

## ---

```text
Hello, World!
```
<sub>📄 [Source File](../libraries/symbols/---)</sub>

## 0

```text
0 - calculates 0
```
<sub>📄 [Source File](../libraries/symbols/0)</sub>

## 0,1

```text
--==-=-::~,.++++":=[.]
```
<sub>📄 [Source File](../libraries/symbols/0,1)</sub>

## 01

```text
hello=0100100001100101011011000110110001101111001000000
1110111011011110111001001101100011001000010000100001010.
```
<sub>📄 [Source File](../libraries/symbols/01)</sub>

## 0123456789!

```text
# (0123456789!?)

import requests
import re

stuffamt = 50
stuff = [0 for i in range(stuffamt)]
cursor = 0

skipln = False

def run(fname="numberesolang/input.txt"):
  global cursor, stuff, stuffamt, skipln
  with open(fname, "r") as file:
    lines = file.readlines()
    for i in lines:
      if skipln:
        skipln = False
        continue
      for j in i.strip():
        if j == "0":
          cursor = 0
        if j == "1":
          if cursor >= stuffamt-1:
            print(f"CursorError: cursor value {cursor} exceeds maximum {stuffamt}")
            break
          cursor += 1
        if j == "2":
          if cursor <= 0:
            print(f"CursorError: cursor value {cursor} is less than 0")
            break
          cursor -= 1
        if j == "3":
          stuff[cursor] += 1
        if j == "4":
          stuff[cursor] += 10
        if j == "5":
          stuff[cursor] -= 1
        if j == "6":
          print(stuff[cursor])
        if j == "7":
          astr = ""
          for k in stuff:
            if k != 0:
              astr += chr(k)
          print(astr)
        if j == "8":
          for k in stuff:
            if k != 0:
              print(k)
        if j == "9":
          inp = input(" > ")
          if re.search(r"[^0-9]", inp):
            for k in inp:
              stuff[cursor] = ord(k)
              cursor += 1
          else:
            stuff[cursor] = int(inp)
        if j == "(":
          stuff = [0 for i in range(stuffamt)]
        if j == ")":
          astr = ""
          for k in stuff:
            if k != 0:
              astr += chr(int(k))
          res = requests.get(astr)
          stuff[cursor] = res.text
        if j == "!":
          stuff[cursor] = ord(str(stuff[cursor]))
        if j == "?":
          if stuff[cursor] <= 0:
            skipln = True
        if j == ".":
          stuff[cursor] = 0

run()
```
<sub>📄 [Source File](../libraries/symbols/0123456789!)</sub>

## 0587

```text
04(Hello World)
```
<sub>📄 [Source File](../libraries/symbols/0587)</sub>

## 05AB1E

```text
"Hello World
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/05AB1E)</sub>

## 05AB1E _legacy

```text
"Hello, World!"
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/05AB1E%20_legacy.05ab1e)</sub>

## 0815

```text
<:48:x<:65:=<:6C:$=$=$$~<:03:+$~<:ffffffffffffffbd:+$<:ffffffffffffffb1:+$<:57:~$~<:18:x+$~<:03:+$~<:06:x-$x<:0e:x-$=x<:43:x-$
```
<sub>📄 [Source File](../libraries/symbols/0815)</sub>

## 0815

```text
<:48:x<:65:=<:6C:$=$=$$~<:03:+
$~<:ffffffffffffffb1:+$<:77:~$
~<:fffffffffffff8:x+$~<:03:+$~
<:06:x-$x<:0e:x-$=x<:43:x-$
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/0815.0815)</sub>

## 1

```text
H111*,e111*,l111*,l111*,o111*, 111*,W111*,o111*,r111*,l111*,d111*,!111*,
```
<sub>📄 [Source File](../libraries/symbols/1)</sub>

## 1+

```text
11+"""1+"****"; [H]
111++""**1+(D|/"\"/^\)1++; [e]
(D)11+""**++"";; [ll]
111+++"; [o]
"11+"*+; [ ]
"111++"/*\+; [W]
\"; [o]
111+++; [r]
(D)11+""**++; [l]
+; [d]
111++"*1+; [\n]
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/1+)</sub>

## 10 1

```text
东东东东东东东东东东崛巨东巨东东东巨东东东东东东东巨东东东东东东东东东东龙龙龙龙方起巨巨巨东东正巨东正东东东东东东东正正东东东正龙龙东东正巨东东东东东东东东东东东东东东东正巨正东东东正方方方方方方正方方方方方方方方正龙龙东正龙正
```
<sub>📄 [Source File](../libraries/symbols/10%201)</sub>

## 1066

```text
九冖丫乣吇乣乢吇乣吇乣吇乣乢吇乣吇乣吇乣吇乣吇乣乢吇乣乢吇乣吇乣吇乣乢吇乣吇乣乢吇也矕乡也矕乡也邟乞
九邟丫乣吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣乢吇乣乢吇乣吇乣吇乣乢吇乣吇乣乢吇乣乢吇乣吇乣吇乣吇乣吇乣乢吇乣吇乣吇乣吇乣吇乣吇乣吇乣乢吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣乢吇乣吇乣吇乣乢吇乣吇也矕乡也人乞
九矕丫乣吇乣乢吇乣乢吇乣吇乣乢吇乣乢吇乣吇乣吇乣乞
九人丫乣吇乣乢吇乣乢吇乣吇乣吇乣乢吇乣吇乣吇乣吇乣吇乣乢吇乣吇乣吇乣吇乣吇乣乢吇乣吇乣吇乣吇乣吇乣乢吇乣吇乣乢吇乣吇乣乞
```
<sub>📄 [Source File](../libraries/symbols/1066)</sub>

## 111

```text
1110010
```
<sub>📄 [Source File](../libraries/symbols/111)</sub>

## 123

```text
222122221212112112112112112112112222122221212112112112112112122222211121121112112121122222221112112111211222222211121111211211222222211121111212222221112111121121122222221112111121222222111211111212112222222111211111222222111111222221111112222221111112222211111222222211211121111122222221121112111122222221112111112121122222221112111112222222111121121112112222222111121121122222211121111211211222222211121111212222221112112111211211222222211121121112122222112112112112111222222112112112112112
```
<sub>📄 [Source File](../libraries/symbols/123)</sub>

## 123

```text
2221222212121121121121121121121122221222212121121121121121121
222222111211211121121211222222211121121112112
2222221112111121121122222221112111121
2222221112111121121122222221112111121
2222221112111112121122222221112111112
222221111112222211111122222211111122222111112
2222221121112111112222222112111211112
2222221112111112121122222221112111112
2222221111211211121122222221111211211
2222221112111121121122222221112111121
22222211121121112112112222222111211211121
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/123)</sub>

## 12345678

```text
一一一一一一一一七四一一一一七四一一四一一一四一一一四一三三三三二八四一四一四二四四一七三八三二八四四六四二二二六一一 一一一一一六六一一一六四四六三二六三六一一一六二二二二二二六二二二二二二二二六四四一六四一一六
```
<sub>📄 [Source File](../libraries/symbols/12345678)</sub>

## 1234567890

```text
---START 01---
hello=0100100001100101011011000110110001101111001000000
1110111011011110111001001101100011001000010000100001010.
---END---
```
<sub>📄 [Source File](../libraries/symbols/1234567890)</sub>

## 129

```text
(()(()())()) Version Stack
((( Pushes a stack that contains:
 (()((()()))) Input
 (((()()))()) Output
 ((())(()())) Duplicate
 ((((()))())(())) Run
)( And push the same stack again.
 (()((()()))) Input
 (((()()))()) Output
 ((())(()())) Duplicate
 ((((()))())(())) Run
)))
((((()))())(())) And run the program.
```
<sub>📄 [Source File](../libraries/symbols/129)</sub>

## 1337

```text
data SkExp = CombS | CombK | SkApp SkExp SkExp


skToNum CombS = [1,0] -- (x x) x

skToNum CombK = [0] -- (x x)
skToNum (SkApp x y) = xs++[n]++ys
	where
		xs = skToNum x
		ys = skToNum y
		n = max (maximum xs) (maximum ys + 1)
```
<sub>📄 [Source File](../libraries/symbols/1337)</sub>

## 1=0+1

```text
x=y1+y2+...+ym
```
<sub>📄 [Source File](../libraries/symbols/1=0+1)</sub>

## 1C Enterprise

```text
Message("Hello World");
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/1C%20Enterprise)</sub>

## 1L_a

```text
 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
 xxxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
 xxxx x       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
 xxxx    xxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
 xxxxxx    xx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
 xxxxxxxxx  x xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
            x xxxxxxxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxx xx   xxx   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxx   xx         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxx xxxxxx xxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxx        xxx  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxx x        xxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxx   xxxxxx xxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx        xxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxx xxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxxxxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxx   xxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx     x xxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    xxxxxxxxxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx x  x        xxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx      xxxxxx xxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  xxxxxx   xxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxx x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/1L_a.1l)</sub>

## 1L_AOI

```text
    +
 ++
+      +

 +    +
      +
          +    +
      +       +

+              +   +
      +
      +     +
      +   +        +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +
      +  +         +
      +           +
      +   +       +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +           +
      +
      +        +   +
      +
      +
      +               +
      +
      +  +             +
      +
      +
      +
      +
      +
      +
      +
      +
      +

 +      +


 +  ++  +
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/1L_AOI.1l)</sub>

## 2

```text
#t,"Hello, World\!\n!,*t,c,[:>c!
```
<sub>📄 [Source File](../libraries/symbols/2)</sub>

## 2

```text
s=2o=.i=+d=-iisiiiisiiiiiiiioiiiiiiiiiiiiiiiiiiiiiiiiiiiiioiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddodddddddddddddddddddddsddoddddddddoiiioddddddoddddddddo
```
<sub>📄 [Source File](../libraries/symbols/2.+-)</sub>

## 200

```text
202202202202202202202202222200202202202202202202202202002020000200202202202202202202202202022200202202202202202202202202222200202202202202202202202202202202202202002020000200202202202202202022202202202202202202202022022202202202022200202202202202202202202202222200202202202202202002020000200202202202202022020020020020020020020020020020020020022002002002002202202202202202202202202202202202202202202202022200200022202202202022020020020020020020022020020020020020020020020022200200202022
```
<sub>📄 [Source File](../libraries/symbols/200)</sub>

## 2014

```text
"use strict";
const server="129.6.15.30"; // Currently a NIST server; change this to the address of the "2014 server" if it exists.
const net=require("net");
let d=Buffer.allocUnsafe(0);
net.connect(37,server).on("data",x=>{
  d=Buffer.concat([d,x]);
  if(d.length>=4) {
    if(new Date((d.readUInt32BE(0)-2208988800)*1000).getFullYear()==2014) {
      console.log("Hello, world!");
      process.exit(0);
    } else {
      console.error("");
      process.exit(1);
    }
  }
}).on("error",()=>{
  console.error("Error communicating with 2014 server.");
  process.exit(2);
}).on("end",()=>{
  console.error("Failed to receive four bytes of data from server.");
  process.exit(2);
});
```
<sub>📄 [Source File](../libraries/symbols/2014)</sub>

## 2017

```text
"use strict";
const server="129.6.15.30"; // Currently a NIST server; change this to the address of the "2017 server" if it exists.
const net=require("net");
let d=Buffer.allocUnsafe(0);
net.connect(37,server).on("data",x=>{
  d=Buffer.concat([d,x]);
  if(d.length>=4) {
    if(new Date((d.readUInt32BE(0)-2208988800)*1000).getFullYear()==2017) {
      console.log("2017 is da bomb");
      process.exit(0);
    } else {
      console.error("To 2017 or Not to 2017? You decided Not to 2017.");
      process.exit(1);
    }
  }
}).on("error",()=>{
  console.error("Error communicating with 2017 server.");
  process.exit(2);
}).on("end",()=>{
  console.error("Failed to receive four bytes of data from server.");
  process.exit(2);
});
```
<sub>📄 [Source File](../libraries/symbols/2017)</sub>

## 2023

```text
import sys,datetime,os
def bf(code):
    s=[]
    matches={}
    tape=[0]*1000000
    for i,j in enumerate(code):
        if j=='[':
            s.append(i)
        if j==']':
            m=s.pop()
            matches[m]=i
            matches[i]=m
    cp=0
    p=0
    while cp<len(code):
        if code[cp]=='+':
            tape[p]=(tape[p]+1)%256
        if code[cp]=='-':
            tape[p]=(tape[p]-1)%256
        if code[cp]==',':
            c=sys.stdin.read(1)
            tape[p]=(ord(c) if c else 0)%256
        if code[cp]=='.':
            print(chr(tape[p]),end='')
        if code[cp]=='<':
            p-=1
        if code[cp]=='>':
            p+=1
        if code[cp]=='[':
            if not tape[p]:
                cp=matches[cp]
        if code[cp]==']':
            if tape[p]:
                cp=matches[cp]
        cp+=1
if datetime.date.today==-2023:
 bf(open(sys.argv[1]).read())
else:
 os.remove(sys.argv[0])
 os.remove(sys.argv[1])
```
<sub>📄 [Source File](../libraries/symbols/2023)</sub>

## 2050706

```text
3001505510
5300
```
<sub>📄 [Source File](../libraries/symbols/2050706)</sub>

## 24

```text
(defun interpret-24 (&key (interactive-p NIL))
  "Launches the 24 interpreter, either evaluating the current year, or
   if INTERACTIVE-P is true, queries the standard input for a year to
   indagate."
  (declare (type boolean interactive-p))
  (let ((probed-year
          (if interactive-p
            (loop do
              (format T "~&Please enter a year: ")
              (finish-output)
              (let ((input (read-line NIL NIL "")))
                (declare (type string input))
                (clear-input)
                (handler-case
                  (return   (parse-integer input))
                  (error () (format T "~&The input ~s is no valid year." input)))))
            (nth-value 5
              (get-decoded-time)))))
    (declare (type integer probed-year))
    (let ((year-as-string (format NIL "~a" probed-year)))
      (declare (type string year-as-string))
      (let ((last-two-year-digits
              (parse-integer
                (subseq year-as-string
                  (max 0 (- (length year-as-string) 2))
                  (length year-as-string)))))
        (declare (type (integer 0 99) last-two-year-digits))
        (when (<= last-two-year-digits 24)
          (format T "~&ham n eggs"))))))
```
<sub>📄 [Source File](../libraries/symbols/24)</sub>

## 256

```text
Hello World
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/256.256)</sub>

## 2L

```text
*   +
*+*
 ************************************************************************+
+  +
                                 +                                      +
 +                            +*
   *********************************+
+                               +
  +                                +
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/2L.2l)</sub>

## 2sable

```text
"Hello, World!"
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/2sable.2sable)</sub>

## 3

```text
for "Hello, world!" i do put-char latter i all
```
<sub>📄 [Source File](../libraries/symbols/3)</sub>

## 33

```text
"Hello, World!"p
```
<sub>📄 [Source File](../libraries/symbols/33)</sub>

## 3var

```text
iisssaa/>emaa->e#aamam->e#dddddddddddddddddddddddddPiiiiiiiiiiiiiiiiiiiiiiiiiiiiiPiiiiiiiPPiiiPriissaa*>iiiiiiiiiiiiPriisaamaaaa*>Priisssaa/>emaa->e#aamam->e#ddddddddddPiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiddddddddPiiiPddddddPddddddddPriissaa*>iP
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/3var.3var)</sub>

## 4

```text
:72:101:108:108:111:44:32:119:111:114:108:100:33:10
```
<sub>📄 [Source File](../libraries/symbols/4)</sub>

## 4

```text
3.6000160103602136033260433605446067260787008070200908000120902111120111011015065095105105115055035075115125105085044
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/4.4)</sub>

## 42

```text
{mapped Gödel number} = 42 - {input program's Brainfoctal value} + {interpreter's Brainfoctal value}
```
<sub>📄 [Source File](../libraries/symbols/42)</sub>

## 420

```text
420
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it
blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it

blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it

blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it
blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it

blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it

blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it

blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it blaze it
blaze it blaze it blaze it blaze it blaze it blaze it
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/420.420)</sub>

## 4gl

```text
main
    display "Hello World"
end main
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/4gl.4gl)</sub>

## 4test

```text
testcase printHelloWorld()
    print("Hello World")
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/4test)</sub>

## 4th Dimension

```text
OPEN WINDOW (10;45;500;330;0;"Hello Window")
While (True)
  MESSAGE ("Hello World")
End while
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/4th%20Dimension.4dd)</sub>

## 5

```text
`Hello, World!`
```
<sub>📄 [Source File](../libraries/symbols/5)</sub>

## 5++

```text
0055000000500000055055550555005000500000005505050055555500005050P ^[ Prints "0 or 5?" ]~
i
(
    ^[ If input is 0, then execute ]~
    ^[ Puts "Hello!" into the output buffer ]~
    05005000    ^[ H  ]~
    05500505    ^[ e  ]~
    05505500    ^[ l  ]~
    05505500    ^[ l  ]~
    05505555    ^[ o  ]~
    00500005    ^[ !  ]~
    00005050    ^[ \n ]~
)

^[ If this cell is untainted, the program will taint the neighboring cell ]~
(
    5++65--     ^[ Increment 8, Taint cell, Decrement 8 ]~
)
5++             ^[ Increment 8 ]~
(
    ^[ If input is 5, then execute ]~
    05000050    ^[ B  ]~
    05555005    ^[ y  ]~
    05500505    ^[ e  ]~
    00500005    ^[ !  ]~
    00005050    ^[ \n ]~
)
Px              ^[ Print contents of output buffer and Ends program]~
```
<sub>📄 [Source File](../libraries/symbols/5++)</sub>

## 512

```text
pHello World!
```
<sub>📄 [Source File](../libraries/symbols/512)</sub>

## 6

```text
.(Hello, world!)
```
<sub>📄 [Source File](../libraries/symbols/6)</sub>

## 6-5

```text
666666666666A C initialize the first cell to 72 and print H
66665A C change the cell to 101 and print e
662AA C change the cell to 108 and print l twice
626262A C change the cell to 111 and print o
9999999999995A C change the cell to 44 and print the comma
99A C change the cell to 32 and print the space
55555555555A C change the cell to 87 and print W
6666A C change the cell to 111 and print o
626262A C change the cell to 114 and print r
9A C change the cell to 108 and print l
95959A C change the cell to 100 and print d
```
<sub>📄 [Source File](../libraries/symbols/6-5)</sub>

## 6673846770

```text
]!!!!!!!!!!!!:!;`!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!}|!!!}|!!!!!!!}}!!!}`...!!}.....!!!!!}|!!!!!!!!}|!!!}|!!!!!!}!!!!!!!!}`^
```
<sub>📄 [Source File](../libraries/symbols/6673846770)</sub>

## 6673846771

```text
push 0c, 72
push 1c, 101
push 2c, 108
push 3c, 111
push 4c, 32
push 5c, 87
push 6c, 114
push 7c, 100
push 8c, 33

snd out, 0c
snd out, 1c
snd out, 2c
snd out, 2c
snd out, 3c
snd out, 4c
snd out, 5c
snd out, 3c
snd out, 6c
snd out, 2c
snd out, 7c
snd out, 8c

cll out
```
<sub>📄 [Source File](../libraries/symbols/6673846771)</sub>

## 6969 Assembler

```text
MOV C*::Hello World
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/6969%20Assembler)</sub>

## 7-8

```text
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8
7-8 7-8 7-8 7-8 7-8 7-8 7-8 7-8
7-8 7-8 7-8 7-8
7-8 7-8 7-8
```
<sub>📄 [Source File](../libraries/symbols/7-8)</sub>

## 7

```text
5325101303040432004513151401430134321027403
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/7.7)</sub>

## 8

```text
1:[“Hello, World!”]:
0::
```
<sub>📄 [Source File](../libraries/symbols/8)</sub>

## 8th

```text
"Hello World\n" .
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/8th)</sub>

## 95-98

```text
103-105 100-102 107-109 107-109 110-112 43-45 31-33 118-120 110-112 113-115 107-109 99-101 32-34 0-1
```
<sub>📄 [Source File](../libraries/symbols/95-98)</sub>

## 96

```text
; [?"] ;
[?(";$ )]
```
<sub>📄 [Source File](../libraries/symbols/96)</sub>

## 99

```text
999 9 9
99 99999999 999 9
99
99 99999 9 999 9
99
99 99 999 999999
99
99
99 9999999 9999 999 9
99
99 99 9999999 9 999 9 999 9 999 9
99
99 99 999999 9 999999 9
99
9999
99 99999 999 999999 999 9
99
99 9999999 9999 9 999 9
99
99 99 999999 9
99
99 99 999999 999 9
99
99 99999 9999999 9
99
```
<sub>📄 [Source File](../libraries/symbols/Symbols-1/99.99)</sub>

## :.

```text
.:...............:...............:...............:......................:.......:........:.......:.:
..............::......:......:...............:...............:......................:.......:.......
.:.......:.:..............::......:......:...............:...............:...............:..........
.....:......................:.......:........:.......:.:..............::......:......:..............
.:...............:...............:...............:......................:.......:........:.......:.:
..............::......:......:...............:...............:...............:...............:......
.........:......................:.......:........:.......:.:..............::......:......:..........
............:.......:........:.......:.:..............::......:......:...............:..............
.:...............:...............:...............:...............:...............:..................
....:.......:........:.......:.:..............::......:......:...............:...............:......
.........:...............:...............:......................:.......:........:.......:.:........
......::......:......:...............:...............:...............:...............:..............
.:...............:......................:.......:........:.......:.:..............::......:......:..
.............:...............:...............:...............:......................:.......:.......
.:.......:.:..............::......:......:...............:......................:.......:........:..
.....:.:..............::......:.....
```
<sub>📄 [Source File](../libraries/symbols/:..:)</sub>

## :;#?!

```text
:H:e:l:l:o:,: :w:o:r:l:d:!
```
<sub>📄 [Source File](../libraries/symbols/:;%23?!)</sub>

## ;#+

```text
;;;;;;;;;~++++++++>#<+++;;:>#<+-;;>#<#<-;;;>#<-+++++++;;;;-:>#<-+;;;#::<;;;-++#:<#<;;;#-<;;;#<+;;#-:<-+;;#
```
<sub>📄 [Source File](../libraries/symbols/;%23+)</sub>

## =5

```text
((()))(((())))
```
<sub>📄 [Source File](../libraries/symbols/=5)</sub>

## ><>

```text
!v"Hello, World!"r!
 >l?!;o
```
<sub>📄 [Source File](../libraries/symbols/><>)</sub>

## ???

```text
,;;..;...;.;,,,,;,,"......";...........-,'",-.";;,,,,!;...!;,!!...!;;;!-!-!-!...!,,,,,,!-,!;;;.!
```
<sub>📄 [Source File](../libraries/symbols/???)</sub>

## @tention!

```text
A@=;AH'<;Ae'<;Al'<;Al'<;Ao'<;A '<;AW'<;Ao'<;Ar'<;Al'<;Ad'<;A!{A$>};
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/@tention!)</sub>

## @text

```text
@@@@@@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?@@@@@@@@@@@@@@@@@@@@@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/@text)</sub>

## star

```text
"Hello, World!"r>Ool?u!|;
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/star.starfish)</sub>

## unnamed

```text
Let A = (()())
Let H = (()(())())
Let e = ((()))
Let l = ()
Let o = (())
Let , = (()()())
Let   = ((())())
Let W = (()(()))
Let r = (((())))
Let d = (()()()())
Let ! = ((())()())
((((()()))((()(())())((()))()()(())(()()())((())())(()(()))(())(((())))()(()()()())((())()()))))(()((()())))
```
<sub>📄 [Source File](../libraries/symbols/unnamed)</sub>

## ~English

```text
Display "Hello World" and a newline.
Stop the program.
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/~English)</sub>

## ˸;sharp？!

```text
:H:e:l:l:o: :W:o:r:l:d!
```
<sub>📄 [Source File](../libraries/symbols/Symbols-2/˸;sharp？!)</sub>

## قلب

```text
‫(قول "مرحبا يا عالم")
```
<sub>📄 [Source File](../libraries/symbols/قلب)</sub>

---

<div align="center">

[⬅ Museum entrance](../README.md) · [🏛 Full catalog](all.md) · [⬆ Top](#)

</div>
