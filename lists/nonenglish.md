# nonenglish

152 entries.

##### !@#$%^&∗ __+
```text
dlroW olleH(@)
```
[Source File](../libraries/nonenglish/!@#$%^&∗ __+)

##### ACPI Source Language
```text
// Hello world in ACPI Source Language

Scope(\) {
	Method(_WAK) {
		Store ("Hello World", Debug)
		Return(Package(2){0x00000000,0})
	}	
}
```
[Source File](../libraries/nonenglish/ACPI Source Language)

##### Actionscript  _Flash 5
```text
// Hello World in Actionscript (up to Flash 5, IDE only)

trace ("Hello World");
```
[Source File](../libraries/nonenglish/Actionscript  _Flash 5)

##### ActionScript  _Flash 8
```text
// Hello World in ActionScript 2.0 (Flash 8)
class HelloWorld
{
    private var helloWorldField:TextField;
 
    public function HelloWorld( mc:MovieClip )
    {
        mc.helloWorldField = mc.createTextField("helloWorldField", mc.getNextHighestDepth(), 0, 0, 100, 100);
        mc.helloWorldField.autoSize = "left";
	mc.helloWorldField.html = true;
        mc.helloWorldField.htmlText = '<font size="20" color="#0000FF">Hello World!</font>';
    }
}

// on a frame
import HelloWorld;
var hw:HelloWorld = new HelloWorld( this );
```
[Source File](../libraries/nonenglish/ActionScript  _Flash 8)

##### Actionscript  _Flash MX
```text
// Hello World in Actionscript (Flash MX onwards) 

_root.createTextField("mytext",1,100,100,300,100);
mytext.multiline = true;
mytext.wordWrap = true;
mytext.border = false;

myformat = new TextFormat();
myformat.color = 0xff0000;
myformat.bullet = false;
myformat.underline = true;

mytext.text = "Hello World!";
mytext.setTextFormat(myformat);
```
[Source File](../libraries/nonenglish/Actionscript  _Flash MX)

##### ActionScript 3
```text
// Hello World in ActionScript 3. Place code in the first frame Actions.
var t:TextField=new TextField();
t.text="Hello World!";
addChild(t);
```
[Source File](../libraries/nonenglish/ActionScript 3.0)

##### Amazon States Language
```text
{
    "Comment": "Hello world in Amazon States Language",
    "StartAt": "Hello World",
    "States": {
    "Hello World": { 
      "Type": "Task",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloWorld",
      "End": true
    }
  }
}
```
[Source File](../libraries/nonenglish/Amazon States Language)

##### ASP  _C♯
```text
<!-- Hello World for ASP.NET using C# -->
<% @ Page Language="C#" %>
<% ="Hello World!" %>
```
[Source File](../libraries/nonenglish/ASP  _C♯)

##### ASP  _JavaScript
```text
Hello World for Microsoft ASP (in JavaScript)

<%@ language="javascript" %>
<html><body>
<%
Response.Write('Hello World!');
%>
</body></html>
```
[Source File](../libraries/nonenglish/ASP  _JavaScript)

##### ASP  _VBE
```text
<!-- Hello World in ASP-VBE (Visual Basic Script Encided) -->
<html>
<script language="VBScript.Encode">#@~^HQAAAA==@#@&HdTAK6PrCsVKP    WMV[Zr@#@&HwcAAA==^#~@</script>
</html>
```
[Source File](../libraries/nonenglish/ASP  _VBE)

##### ASP  _VBS
```text
Hello World for Microsoft ASP (in VBScript)

<%@ language="vbscript" %>
<html><body>
<%
Response.write "Hello World!"
%>
</body></html>
```
[Source File](../libraries/nonenglish/ASP  _VBS)

##### Assembler  _6502, Apple II
```text
**********************************
*                                *
*      HELLO WORLD FOR 6502      *
*    APPLE ][, MERLIN ASSEMBLER  *
*                                *
**********************************

STROUT 	EQU	$DB3A ;OUTPUTS AY-POINTED NULL TERMINATED STRING
	LDY	#>HELLO
	LDA	#<HELLO
	JMP	STROUT

HELLO	ASC	"HELLO WORLD!",00
```
[Source File](../libraries/nonenglish/Assembler  _6502, Apple II)

##### Assembler  _6502, C64
```text
; Hello World for 6502 Assembler (C64)

ldy #0
beq in
loop:
jsr $ffd2
iny
in:
lda hello,y
bne loop
rts
hello: .tx "Hello World!"
       .by 13,10,0
```
[Source File](../libraries/nonenglish/Assembler  _6502, C64)

##### Assembler  _68000, Amiga
```text
; Hello World in 68000 Assembler for dos.library (Amiga)

        move.l  #DOS
        move.l  4.w,a6
        jsr     -$0198(a6)      ;OldOpenLibrary
        move.l  d0,a6
        beq.s   .Out
        move.l  #HelloWorld,d1

A)      moveq   #13,d2
        jsr     -$03AE(a6)      ;WriteChars

B)      jsr     -$03B4          ;PutStr

        move.l  a6,a1
        move.l  4.w,a6
        jsr     -$019E(a6)      ;CloseLibrary
.Out    rts

DOS          dc.b    'dos.library',0
HelloWorld   dc.b    'Hello World!',$A,0
```
[Source File](../libraries/nonenglish/Assembler  _68000, Amiga)

##### Assembler  _68000, Atari ST
```text
; Hello World in 68000 Assembler (Atari ST)

     move.l #helloworld,-(A7)
     move   #9,-(A7)
     trap   #1
     addq.l #6,A7
     move   #0,-(A7)
     trap   #1
helloworld:
     dc.b "Hello World!",$0d,$0a,0
```
[Source File](../libraries/nonenglish/Assembler  _68000, Atari ST)

##### Assembler  _8051
```text
-- Hello World in Assembler for the Intel 8051 (MSC51)

 Org 0
 
   mov dptr,#msg
   mov R0,#30h  
loop:
   clr a
   movc a,@a+dptr
   jz end
   mov @R0,a
   inc R0
   inc dptr
   sjmp  loop
 
end:
    jmp $
 
msg:
    db 'Hello World",0
```
[Source File](../libraries/nonenglish/Assembler  _8051)

##### Assembler  _ARM, Android
```text
/* Hello world in ARM assembly (Android devices) */

.data

msg:
    .ascii      "Hello, World!\n"
len = . - msg

.text

.globl _start
_start:
    mov     %r0, $1
    ldr     %r1, =msg
    ldr     %r2, =len
    mov     %r7, $4
    swi     $0
    mov     %r0, $0
    mov     %r7, $1
    swi     $0
```
[Source File](../libraries/nonenglish/Assembler  _ARM, Android)

##### Assembler  _ARM, RISC OS
```text
; Hello World in ARM code assembler, with RISC OS software interrupt

SWI "OS_WriteS"
EQUS "Hello World!"
EQUB 0
ALIGN
MOV PC,R14
```
[Source File](../libraries/nonenglish/Assembler  _ARM, RISC OS)

##### Assembler  _DG-Nova
```text
                        .TITL HELLO
02                      ; "HELLO, WORLD" FOR NOVA RUNNING RDOS
03                      ; USES PCHAR SYSTEM CALL
04                      .NREL
05                      .ENT START
06
07              START:
08 00000'022424 DOCHAR: LDA 0,@PMSG     ; LOAD AC0 WITH NEXT CHARACTER,
09 00001'101015         MOV# 0,0,SNR    ; TEST AC0;
10 00002'000412          JMP DONE ; SKIPPED IF NONZERO
11 00003'006017         .SYSTM
12 00004'010000         .PCHAR          ; PRINT FIRST
13 00005'000413          JMP ER ; SKIPPED IF OK
14 00006'101300         MOVS 0,0        ; SWAP BYTES
15 00007'006017         .SYSTM
16 00010'010000         .PCHAR          ; PRINT SECOND
17 00011'000407          JMP ER ; SKIPPED IF OK
18 00012'010412         ISZ PMSG        ; POINT TO NEXT WORD
19 00013'000765         JMP DOCHAR      ; GO AROUND AGAIN
20
21 00014'006017 DONE:   .SYSTM          ; NORMAL EXIT
22 00015'004400         .RTN
23 00016'000402          JMP ER
24 00017'063077         HALT
25 00020'006017 ER:     .SYSTM          ; ERROR EXIT
26 00021'006400         .ERTN
27 00022'063077          HALT
28 00023'063077         HALT
29
30 00024'000025'PMSG:   .+1     ; ADDRESS OF FIRST WORD OF TEXT
31                      ; NOTE BYTES ARE PACKED RIGHT-TO-LEFT BY DEFAULT
32 00025'042510         .TXT /HELLO, WORLD!<15><12>/ ; THAT'S CR LF
33       046114
34       026117
35       053440
36       051117
37       042114
38       006441
39       000012
40 00035'000000         0 ; FLAG WORD TO END STRING
41
42                      .END START
```
[Source File](../libraries/nonenglish/Assembler  _DG-Nova)

##### Assembler  _HLA
```text
; Hello World for Intel compatible High Level Assembler

program HELLO;
       #include( "stdlib.hhf" );
begin HELLO;
       stdout.put("Hello World",nl);
end HELLO;
```
[Source File](../libraries/nonenglish/Assembler  _HLA)

##### Assembler  _HP-85
```text
010 ! Hello world in Assembler for the HP-85
020         NAM HELLO
030         DEF RUNTIM
040         DEF TOKENS
050         DEF PARSE
060         DEF ERMSG
070         DEF INIT
100 PARSE   BYT 0,0
110 RUNTIM  BYT 0,0,377,377
120 TOKENS  BYT 377
130 ERMSG   BYT 377
140 !
150 INIT    LDM R26,=MSG
160         ADMD R26,=BINTAB
170         LDM R36,=12D,0
180         JSB =OUTSTR
190         RTN
200 MSG     ASC "Hello World!"
210 BINTAB  DAD 101233
220 OUTSTR  DAD 35052
300         FIN
```
[Source File](../libraries/nonenglish/Assembler  _HP-85)

##### Assembler  _IBM 370
```text
ITLE 'Hello World for IBM Assembler/370 (VM/CMS)'
HELLO    START
BALR  12,0
USING *,12
*
WRTERM 'Hello World!'
*
SR    15,15
BR    14
*
END   HELLO
```
[Source File](../libraries/nonenglish/Assembler  _IBM 370)

##### Assembler  _Intel
```text
; Hello World for Intel Assembler (MSDOS)

mov ax,cs
mov ds,ax
mov ah,9
mov dx, offset Hello
int 21h
xor ax,ax
int 21h

Hello:
  db "Hello World!",13,10,"$"
```
[Source File](../libraries/nonenglish/Assembler  _Intel)

##### Assembler  _Itanium
```text
/* Hello world for IA64 (Itanium) Assembly */

.HW:
        stringz "Hello World"
        .text
        .align 16
        .global main#
        .proc main#
main:
        .prologue 14, 32
        .save ar.pfs, r33
        alloc r33 = ar.pfs, 0, 4, 1, 0
        .vframe r34
        mov r34 = r12
        adds r12 = -16, r12
        mov r35 = r1
        .save rp, r32
        mov r32 = b0
        .body
        addl r14 = @ltoffx(.HW), r1
        ;;
        ld8.mov r14 = [r14], .HW
        ;;
        st8 [r34] = r14
        ld8 r36 = [r34]
        br.call.sptk.many b0 = puts#
        mov r1 = r35
        ;;
        mov ar.pfs = r33
        mov b0 = r32
        .restore sp
        mov r12 = r34
        br.ret.sptk.many b0
```
[Source File](../libraries/nonenglish/Assembler  _Itanium)

##### Assembler  _MIPS
```text
## Hello Word in Assemlber for the MIPS Architecture

.globl main

main:   jal hwbody              #call Hello Word Procedure
       trap 10                 #exit

hwbody: addi $30, $30,-4        #we need to preserve
       sw $4, 0($30)           #existing values in register 4

       addi $4,$0,72           # H
       trap 101
       addi $4,$0,101          # e
       trap 101
       addi $4,$0,108          # l
       trap 101
       trap 101                # l
       addi $4,$0,111          # o
       trap 101
       addi $4,$0,32           # <space>
       trap 101
       addi $4,$0,87           # W
       trap 101
       addi $4,$0,111          # o
       trap 101
       addi $4,$0,114          # r
       trap 101
       addi $4,$0,108          # l
       trap 101
       addi $4,$0,100          # d
       trap 101
       addi $4,$0,33           # !
       trap 101
       addi $4,$0,10           # \n
       trap 101

done:   lw $4, 0($30)           #restore values
       addi $30, $30, 4        #in register 4
       jr $31                  #return to the main
```
[Source File](../libraries/nonenglish/Assembler  _MIPS)

##### Assembler  _MMIX
```text
*	Hello World in Assembler 
*	for the MMIX Computer 

       LOC   #100
Main   GETA  $255,String
       TRAP  0,Fputs,StdOut
       TRAP  0,Halt,0
String BYTE  "Hello, world!",#a,0
```
[Source File](../libraries/nonenglish/Assembler  _MMIX)

##### Assembler  _PA-RISC
```text
// Hello World written in PA-RISC 2.0 assembly code

    .LEVEL  2.0N

    .SPACE  $TEXT$,SORT=8
    .SUBSPA $CODE$,QUAD=0,ALIGN=4,ACCESS=0x2c,CODE_ONLY,SORT=24
main
    .PROC
    .CALLINFO CALLER,FRAME=16,SAVE_RP,ORDERING_AWARE
        .ENTRY
        STW     %r2,-20(%r30)   ;offset 0x0
        LDO     64(%r30),%r30   ;offset 0x4
        ADDIL   LR'M$3-$global$,%r27,%r1        ;offset 0x8
        LDO     RR'M$3-$global$(%r1),%r1        ;offset 0xc
        STW     %r1,-56(%r30)   ;offset 0x10
        ADDIL   LR'M$3-$global$+16,%r27,%r1     ;offset 0x14
        LDO     RR'M$3-$global$+16(%r1),%r26    ;offset 0x18
        LDW     -56(%r30),%r25  ;offset 0x1c
        LDIL    L'printf,%r31   ;offset 0x20
        .CALL   ARGW0=GR,ARGW1=GR,RTNVAL=GR     ;in=25,26;out=28;
        BE,L    R'printf(%sr4,%r31),%r31        ;offset 0x24
        COPY    %r31,%r2        ;offset 0x28
        LDW     -84(%r30),%r2   ;offset 0x2c
        BVE     (%r2)   ;offset 0x30
        .EXIT
        LDO     -64(%r30),%r30  ;offset 0x34
    .PROCEND    ;


    .SPACE  $TEXT$
    .SUBSPA $CODE$
    .SPACE  $PRIVATE$,SORT=16
    .SUBSPA $DATA$,QUAD=1,ALIGN=8,ACCESS=0x1f,SORT=16
M$3
    .ALIGN  8
    .STRINGZ    "Hello World"
    .BLOCK  4
    .STRINGZ    "%s\n"
    .IMPORT $global$,DATA
    .SPACE  $TEXT$
    .SUBSPA $CODE$
    .EXPORT main,ENTRY,PRIV_LEV=3,LONG_RETURN
    .IMPORT printf,CODE
    .END
```
[Source File](../libraries/nonenglish/Assembler  _PA-RISC)

##### Assembler  _PDP-11
```text
;       Hello World in Assembler for the DEC PDP-11 with the
;	RSX-11M-PLUS operating system
;
        .title Hello
        .ident /V0001A/
        .mcall qiow$s, exit$s
        .psect $code,ro,i
start:  qiow$s #5,#5,,,,<#str, #len, #40>
        exit$s
        .psect $data,ro,d
str:    .ascii / Hello World!/
        len=.-str
        .end start
```
[Source File](../libraries/nonenglish/Assembler  _PDP-11)

##### Assembler  _PDP-8
```text
/ Hello World in Assembler for the DEC PDP-8
*200
hello,    cla cll
        tls            / tls to set printer flag.
        tad charac    / set up index register
        dca ir1        / for getting characters.
        tad m6        / set up counter for
        dca count    / typing characters.
next,    tad i ir1    / get a character.
        jms type    / type it.
        isz count    / done yet?
        jmp next    / no: type another.
        hlt

type,    0            / type subroutine
        tsf
        jmp .-1
        tls
        cla
        jmp i type
charac,    .            / used as initial value of ir1
        310 / H
        305 / E
        314 / L
        314 / L
        317 / O
        254 / ,
        240 /
        327 / W
        317 / O
        322 / R
        314 / L
        304 / D
        241 / !
m6,        -15
count,    0
ir1 = 10
$
```
[Source File](../libraries/nonenglish/Assembler  _PDP-8)

##### Assembler  _PPC, Darwin
```text
; Hello World in Assembler for the Darwin Power-PC

.data
.cstring
.align 2
msg:
.asciz "Hello world!\n"
len = . - msg
.text
.align 2
.globl _start
_start:
li r0,4
li r3,1
lis r4,ha16(msg)
ori r4,r4,lo16(msg)
li r5,len
sc
li r0,1
li r3,0
sc
```
[Source File](../libraries/nonenglish/Assembler  _PPC, Darwin)

##### Assembler  _SPARC
```text
! Hello world in SPARC Assembly Language

	.section			".data1"
	.align		4
.L16:
	.ascii   "hello world\n\0"

	.section  ".text"
	.global  main
main:
	save  %sp,-96,%sp
	set  .L16,%o0
	call  printf,1
	nop
	restore
```
[Source File](../libraries/nonenglish/Assembler  _SPARC)

##### Assembler  _TAS
```text
-- Hello world in TAS Assembler for the TR 440 --

HELLO.=SEGM,XBA VB616, SSR 6 16,
FB616=R&ENDE,
 
VB616=FB616/AG, 3/H, TEXT/AG, 3/H,
TEXT=''*020Hello World!'',
ENDE,
```
[Source File](../libraries/nonenglish/Assembler  _TAS)

##### Assembler  _VP
```text
; Hello World in VP Assembler for intent (Amiga Anywhere)

.include 'tao'

tool 'home/hello',VP,TF_MAIN,8192,0
	ent (-:-)
		qcall lib/print,(hello_world.p : i~)
		ret ()
	entend

	data

hello_world:
	dc.b "Hello World!",ASCII_LF,0

toolend
```
[Source File](../libraries/nonenglish/Assembler  _VP)

##### Assembler  _Win32
```text
; Hello world in Assembler for the Win32 architecture

TITLE Hello world in win32. Tasm

VERSION T310
Model use32 Flat,StdCall

start_code segment byte public 'code' use32
begin:
 Call MessageBox, 0, offset sHallo, offset caption, 0
 Call ExitProcess, 0
start_code Ends

start_data segment byte public 'data' use32

sHallo  db 'Hello world',0
caption	db "Hi",0

start_data Ends
End begin
```
[Source File](../libraries/nonenglish/Assembler  _Win32)

##### Assembler  _X1
```text
                  dp zz 0 x 5

                  da 0 zz 0   di
	      0   2b 1       a		       set address increment to 1
	 3->  1   2a 4 zz 0  c p	       load next character to A
	      2   6y 2 xp    		       print it
	      3 y 2t 1 zz 0  a		       loop if not last char
	      4   7p   	  		       and halt
	      5 dn + 19			       lower case
	      6	  + 28			       h
	      7	  + 25			       e
	      8	  + 32			       l
	      9	  + 32			       l
	     10	  + 35			       o
	     11	  + 15			       comma
	     12	  + 20			       space
	     13   + 43			       w
	     14	  + 35			       o
	     15	  + 38			       r
	     16	  + 32			       l
	     17	  + 24			       d
	     18	  - 52			       clrf, negative = last char

                  de 0 zz 0
```
[Source File](../libraries/nonenglish/Assembler  _X1)

##### Assembler  _X8
```text
" Hello world in Assembler for the Electrologica X8 (ca. 1965)

'BEGIN' TEL='1 000 000',  TTY=8
M[24]:
        GOTO(:START)
M[(64+TTY*4)]:
TAR:
M[(64+38*4)]:
TPAR:
        
M['400']:
        
START:
        A=:HELLO DESCR                  " point to I/O descriptor
        TAR[0]=A                        " set address of string
        TAR[1]=-A                       " set IFT = -1
        A=D18
        TAR[2]=A
        AFON(TTY)                       " send the message
LOOP:   GOTO(:LOOP)                     " spin (since there is no halt)
        
D18:    '001 000 000'

HELLO DESCR:
        0
        (17*TEL + :DAG[-1])
        0

DAG:    37                              " letters, red print
        5                               " H
        16                              " E
        9                               " L
        9                               " L
        3                               " O
        27                              " figures
        6                               " comma
        31                              " letters
        4                               " space
        25                              " W
        3                               " O
        10                              " R
        9                               " L
        18                              " D
        2                               " cr
        8                               " nl
```
[Source File](../libraries/nonenglish/Assembler  _X8)

##### Assembler  _z390
```text
; Hello World for z390 IBM compatible mainframe assembler

HELLO CSECT
     USING *,15
     WTO 'Hello World'
     BR 14
     END
```
[Source File](../libraries/nonenglish/Assembler  _z390)

##### Assembler  _Z80 Console
```text
; This is a "Hello World" program for Z80 and TMS9918 / TMS9928 / TMS9929 /
; V9938 or V9958 VDP.
; That means that this should work on SVI, MSX, Colecovision, Memotech,
; and many other Z80 based home computers or game consoles.
;
; Because we don't know what system is used, we don't know where RAM
; is, so we can't use stack in this program.
;
; This version of Hello World was written by Timo "NYYRIKKI" Soilamaa
; 17.10.2001
;
;----------------------------------------------------------------------
; Configure this part:

DATAP: EQU #98 ; VDP Data port #98 works on all MSX models
; (TMS9918/TMS9929/V9938 or V9958)
; #80 works on SVI 
; (for other platforms you have to figure this out by your self)

CMDP: EQU #99 ; VDP Command port #99 works on all MSX models
; (TMS9918/TMS9929/V9938 or V9958)
; #81 works on SVI
; (for other platforms you have to figure this out by your self)
;-----------------------------------------------------------------------
; Program starts here:

ORG 0 ; Z80 starts always from here when power is turned on
DI ; We don't know, how interrupts works in this system, so we disable them.

; Let's set VDP write address to #0000
XOR A
OUT (CMDP),A
LD A,#40
OUT (CMDP),A

; Now let's clear first 16Kb of VDP memory
LD B,0
LD HL,#3FFF
LD C,DATAP
CLEAR:
OUT (C),B
DEC HL
LD A,H
OR L
NOP ; Let's wait 8 clock cycles just in case VDP is not quick enough.
NOP
JR NZ,CLEAR

; Now it is time to set up VDP registers:
;----------------------------------------
; Register 0 to #0
;
; Set mode selection bit M3 (maybe also M4 & M5) to zero and 
; disable external video & horizontal interrupt
LD C,CMDP
LD E,#80

OUT (C),A
OUT (C),E
;---------------------------------------- 
; Register 1 to #50
;
; Select 40 column mode, enable screen and disable vertical interrupt

LD A,#50
INC E
OUT (C),A
OUT (C),E
;---------------------------------------- 
; Register 2 to #0
;
; Set pattern name table to #0000

XOR A
INC E
OUT (C),A
OUT (C),E
;---------------------------------------- 
; Register 3 is ignored as 40 column mode does not need color table
;
INC E
;---------------------------------------- 
; Register 4 to #1
; Set pattern generator table to #800

INC A
INC E

OUT (C),A
OUT (C),E
;---------------------------------------- 
; Registers 5 (Sprite attribute) & 6 (Sprite pattern) are ignored 
; as 40 column mode does not have sprites

INC E
INC E
;---------------------------------------- 
; Register 7 to #F0
; Set colors to white on black

LD A,#F0
INC E
OUT (C),A
OUT (C),E
;----------------------------------------

; Let's set VDP write address to #808 so, that we can write
; character set to memory
; (No need to write SPACE it is clear char already)
LD A,8
OUT (C),A
LD A,#48
OUT (C),A

; Let's copy character set
LD HL,CHARS
LD B, CHARS_END-CHARS
COPYCHARS:
LD A,(HL)
OUT (DATAP),A
INC HL
NOP ; Let's wait 8 clock cycles just in case VDP is not quick enough.
NOP
DJNZ COPYCHARS

; Let's set write address to start of name table
XOR A
OUT (C),A
LD A,#40
OUT (C),A

; Let's put characters to screen
LD HL,ORDER
LD B,ORDER_END-ORDER
COPYORDER:
LD A,(HL)
OUT (DATAP),A
INC HL

JR OVERNMI
NOP
NOP

; Here is address #66, that is entry for NMI
RETN ;Return from NMI

OVERNMI:
DJNZ COPYORDER

; The end
HALT

; Character set:
; --------------
ORDER:
DEFB 1,2,3,3,4,0,5,4,6,3,7
ORDER_END:

CHARS:

; H
DEFB %10001000
DEFB %10001000
DEFB %10001000
DEFB %11111000
DEFB %10001000
DEFB %10001000
DEFB %10001000
DEFB %00000000
; e
DEFB %00000000
DEFB %00000000
DEFB %01110000
DEFB %10001000
DEFB %11111000
DEFB %10000000
DEFB %01110000
DEFB %00000000
; l
DEFB %01100000
DEFB %00100000
DEFB %00100000
DEFB %00100000
DEFB %00100000
DEFB %00100000
DEFB %01110000
DEFB %00000000
; o
DEFB %00000000
DEFB %00000000
DEFB %01110000
DEFB %10001000
DEFB %10001000
DEFB %10001000
DEFB %01110000
DEFB %00000000
; W
DEFB %10001000
DEFB %10001000
DEFB %10001000
DEFB %10101000
DEFB %10101000
DEFB %11011000
DEFB %10001000
DEFB %00000000

; r
DEFB %00000000
DEFB %00000000
DEFB %10110000
DEFB %11001000
DEFB %10000000
DEFB %10000000
DEFB %10000000
DEFB %00000000
; d
DEFB %00001000
DEFB %00001000
DEFB %01101000
DEFB %10011000
DEFB %10001000
DEFB %10011000
DEFB %01101000
DEFB %00000000
chars_end:
```
[Source File](../libraries/nonenglish/Assembler  _Z80 Console)

##### Assembler  _Z80, CP-M
```text
; Hello world in Z80 Assembly for CP/M

BDOS    equ     05h
WRTLINE equ     09h
;
        org     0100h
        lxi     d,sHello
        mvi     c,WRTLINE
        call    BDOS
        ret
;
sHello  db      'Hello, World!$'
```
[Source File](../libraries/nonenglish/Assembler  _Z80, CP-M)

##### Assembler  _ZX81
```text
; Hello World in Assembler for the ZX81 (Zilog Z80)

          CALL SPRINT
          DEFM HELLO WORLD.
          DEFB FF
          RET
SPRINT    POP HL
          LD A,(HL)
          INC HL
          PUSH HL
          CP FF
          RET Z
          CALL PRINT
          JR SPRINT
```
[Source File](../libraries/nonenglish/Assembler  _ZX81)

##### Binary Lambda Calculus
```text
!Hello, world
```
[Source File](../libraries/nonenglish/Binary Lambda Calculus)

##### BMC Remedy
```text
char-set: windows-1252
#
#  Hello World in BMC Remedy 7.0
#  File exported Thu May  8 09:36:46 2008
#
begin active link
   name           : Remedy_HelloWorld
   timestamp      : 1210249958
   export-version : 9
   owner          : Demo
   last-changed   : Demo
   actlink-order  : 0
   wk-conn-type   : 1
   schema-name    : _1
   actlink-mask   : 16
   enable         : 1
   permission     : 0
   action {
      message-type: 0
      message-num : 10000
      message-pane: 1
      message-text: Hello World!!
   }
   object-prop    : 2\60016\4\1\0\60017\4\1\0\
end
```
[Source File](../libraries/nonenglish/BMC Remedy)

##### C  _Amiga Anywhere
```text
/* Hello World in C for Amiga Anywhere 2 (AA2) */

#include <aa.h>

int aaMain(int argc, char **argv)
{
   aaOpenDisplay(200, 200, 16, "Hello World", FAA_DISPLAY_WINDOW);
   aaDrawString(AA_DISPLAY_PIXMAP, "Hello, world!", 20, 20, AA_DEFAULT_FONT, 0xffff00, 0, FAA_FONT_INK, -1);
   aaUpdate();
   aaWaitInput();
   return 0;
}
```
[Source File](../libraries/nonenglish/C  _Amiga Anywhere)

##### C  _ANSI
```text
/* Hello World in C, Ansi-style */

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  puts("Hello World!");
  return EXIT_SUCCESS;
}
```
[Source File](../libraries/nonenglish/C  _ANSI)

##### C  _Curses
```text
/* Hello World in C for Curses */

#include <curses.h>
main()
{
  initscr();
  addstr("Hello World!\n");
  refresh();
  endwin();
  return 0;
}
```
[Source File](../libraries/nonenglish/C  _Curses)

##### C  _GEM
```text
/* Hello World for C with GEM */

#include <aes.h>
main()
{
  appl_init();
  form_alert(1,"[0][Hello World!][Ok]");
  appl_exit();
  return 0;
}
```
[Source File](../libraries/nonenglish/C  _GEM)

##### C  _Intuition
```text
/* Hello World in C for Intution (Amiga GUI) */

#include <intuition/intuition.h>

struct IntuitionBase *IntuitionBase = NULL;

struct IntuiText hello_text = {-1,-1,JAM1,0,0,NULL,"Hello World!",NULL };
struct IntuiText ok_text    = {-1,-1,JAM1,0,0,NULL,"Ok",NULL };

void main(void)
{
   IntuitionBase = (struct IntuitionBase *)
                   OpenLibrary("intuition.library", 0);
   AutoRequest(NULL, &hello_text, NULL, &ok_text, NULL, NULL, 100, 50);
   CloseLibrary(IntuitionBase);
}
```
[Source File](../libraries/nonenglish/C  _Intuition)

##### C  _K&R
```text
/* Hello World in C, K&R-style */

main()
{
  puts("Hello World!");
  return 0;
}
```
[Source File](../libraries/nonenglish/C  _K&R)

##### C  _OpenGL
```text
/* "Hello World" in C using OGL - Open Graphics Library */

#include <GL/glut.h>
#define font GLUT_BITMAP_HELVETICA_18
#define tx "Hello World!"

void text(void)
{
 char *p, tex[] = tx;
 p = tex;
 glColor3d(1.0, 1.0, 0.0);
 glRasterPos2d(-.5, 0.);
 while(*p) glutBitmapCharacter(font, *p++);
}

void display()
{
 glClear(GL_COLOR_BUFFER_BIT);
 text();
 glFlush();
}

void reshape(int width, int height)
{
 glViewport(0, 0, width, height);
 glMatrixMode(GL_PROJECTION);
 glLoadIdentity();
 glOrtho(-1, 1, -1, 1, -1, 1);
 glMatrixMode(GL_MODELVIEW);
 display();
}

int main(int argc, char **argv)
{
 glutInit(&argc, argv);
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
 glutInitWindowPosition(50, 50);
 glutInitWindowSize(500, 500);
 glutCreateWindow("Hello World OpenGL");
 glClearColor(0,0,0,0);
 glutDisplayFunc(display);
 glutReshapeFunc(reshape);
 glutMainLoop();
 return 0;
}
```
[Source File](../libraries/nonenglish/C  _OpenGL)

##### C  _PresentationManager
```text
/* Hello World for C with PresentationManager / OS/2 2.11  */

#define INCL_WIN

#include <os2.h>

int main( void )
{
   HMQ   hmq;

   hmq = WinCreateMsgQueue( 0, 0 );

   WinMessageBox( HWND_DESKTOP, HWND_DESKTOP, (PSZ)"Hello World!",
      (PSZ)"", 0, MB_OK );

   WinDestroyMsgQueue( hmq );

   return 0;
}
```
[Source File](../libraries/nonenglish/C  _PresentationManager)

##### C  _Windows
```text
/* Hello world in C for MS-Windows */

#include <windows.h>

int PASCAL WinMain(HINSTANCE hInstance,
  HINSTANCE hPrevInstance, LPSTR CmdLine, int Show)
{
  MessageBox(GetActiveWindow(), "Hello World!", "Hello Windows World", MB_OK);
  return 0;
}
```
[Source File](../libraries/nonenglish/C  _Windows)

##### C  _X11 Athena
```text
/* Hello World in C with X11 using Athena widgets */

#include <X11/Intrinsic.h>
#include <X11/StringDefs.h>
#include <X11/Xaw/Label.h>

main(int argc,char **argv)
{
  XtAppContext app_context;
  Widget toplevel,hello;

  toplevel = XtVaAppInitialize(&app_context,"XHello",NULL,0,
    &argc,argv,NULL,NULL);
  hello = XtVaCreateManagedWidget("Hello World!",labelWidgetClass,
    toplevel,(void*)0);

  XtRealizeWidget(toplevel);

  XtAppMainLoop(app_context);
  return 0;
}
```
[Source File](../libraries/nonenglish/C  _X11 Athena)

##### C++  _
```text
// Hello World in C++/CLI for .NET

using namespace System;

void main()
{
    Console::WriteLine("Hello World");
}
```
[Source File](../libraries/nonenglish/C++  _.NET CLI)

##### C++  _Epoc
```text
// Hello World in C++, Epoc style (for Symbian OS)

#include <eikapp.h>
#include <eikdoc.h>
#include <eikappui.h>

class CHelloWorldAppUi;
class CEikApplication;
class CHelloWorldAppView;

class CHelloWorldApplication : public CEikApplication
    {
        public:
            TUid AppDllUid() const;
        protected:
            CApaDocument* CreateDocumentL();
    };

class CHelloWorldDocument : public CEikDocument
    {
        public:
            static CHelloWorldDocument* NewL(CEikApplication& aApp);
            static CHelloWorldDocument* NewLC(CEikApplication& aApp);
            ~CHelloWorldDocument(){};
        public:
            CEikAppUi* CreateAppUiL();
        private:
            void ConstructL() {};
            CHelloWorldDocument(CEikApplication& aApp){};
    };

class CHelloWorldAppUi : public CEikAppUi
    {
        public:
                void ConstructL();
                CHelloWorldAppUi(){};
                ~CHelloWorldAppUi(){};
    };

static const TUid KUidHelloWorldApp = {0x10005B91};

GLDEF_C TInt E32Dll(TDllReason )
    {
    return KErrNone;
    }

EXPORT_C CApaApplication* NewApplication() 
    {
    return (new CHelloWorldApplication);
    }

CApaDocument* CHelloWorldApplication::CreateDocumentL()
    {  
    CApaDocument* document = CHelloWorldDocument::NewL(*this);
    return document;
    }

TUid CHelloWorldApplication::AppDllUid() const
    {
    return KUidHelloWorldApp;
    }
    
CHelloWorldDocument* CHelloWorldDocument::NewL(CEikApplication& aApp)
    {
    CHelloWorldDocument* self = NewLC(aApp);
    CleanupStack::Pop(self);
    return self;
    }

CHelloWorldDocument* CHelloWorldDocument::NewLC(CEikApplication& aApp)
    {
    CHelloWorldDocument* self = new (ELeave) CHelloWorldDocument(aApp);
    CleanupStack::PushL(self);
    self->ConstructL();
    return self;
    }

CEikAppUi* CHelloWorldDocument::CreateAppUiL()
    {
    CEikAppUi* appUi = new (ELeave) CHelloWorldAppUi;
    return appUi;
    }

void CHelloWorldAppUi::ConstructL()
    {
    BaseConstructL();

    _LIT(message,"Hello!");
    CAknInformationNote* informationNote = new (ELeave) CAknInformationNote;
    informationNote->ExecuteLD(message);
    }
```
[Source File](../libraries/nonenglish/C++  _Epoc)

##### C++  _FLTK
```text
// Hello World in C++-FLTK

#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Box.H>

int main(int argc, char **argv) {
   Fl_Window *ventana = new Fl_Window(300,180);
   ventana->begin();
   Fl_Box *box = new Fl_Box(20,40,260,100,"Hello World!");
   box->labelsize(50);
   ventana->end();
   ventana->show(argc, argv);
   return Fl::run();
}
```
[Source File](../libraries/nonenglish/C++  _FLTK)

##### C++  _Gtk++
```text
// Hello World in C++ for the Gtk+ toolkit

#include <gtkmm/main.h>
#include <gtkmm/button.h>
#include <gtkmm/window.h>
#include <iostream>

void button_clicked()
{
	std::cout << "Hello, World !" << std::endl;
}

int main (int argc, char *argv[])
{
	Gtk::Main kit(argc, argv);
	Gtk::Window hello_window;
	Gtk::Button hello_button("Hello World");
	
	hello_window.set_border_width(10);
	hello_window.add(hello_button);
	hello_button.signal_clicked().connect(sigc::ptr_fun(&button_clicked));
	hello_button.show();
	
	Gtk::Main::run(hello_window);
	return 0;
}
```
[Source File](../libraries/nonenglish/C++  _Gtk++)

##### C++  _ISO
```text
// Hello World in ISO C++

#include <iostream>

int main()
{
    std::cout << "Hello World!" << std::endl;
}
```
[Source File](../libraries/nonenglish/C++  _ISO)

##### C++  _MFC
```text
// Hello World in C++ for Microsoft Foundation Classes
// (Microsoft Visual C++).

#include <afxwin.h>

class CHello : public CFrameWnd
{
public:
    CHello()
    {
        Create(NULL,_T("Hello World!"),WS_OVERLAPPEDWINDOW,rectDefault);
    }
};

class CHelloApp : public CWinApp
{
public:
    virtual BOOL InitInstance();
};

BOOL CHelloApp::InitInstance()
{
    m_pMainWnd = new CHello();
    m_pMainWnd->ShowWindow(m_nCmdShow);
    m_pMainWnd->UpdateWindow();
    return TRUE;
}

CHelloApp theApp;
```
[Source File](../libraries/nonenglish/C++  _MFC)

##### C++  _Qt
```text
// Hello World in C++ for the Qt framework

#include <qapplication.h>
#include <qlabel.h>

int main(int argc, char *argv[])
{
  QApplication a(argc, argv);
  QLabel l("Hello World!", 0);
  l.setCaption("Test");
  l.setAlignment(Qt::AlignCenter);
  l.resize(300, 200);
  a.setMainWidget(&l);
  l.show();
  return(a.exec());
}
```
[Source File](../libraries/nonenglish/C++  _Qt)

##### CA-Easytrieve Plus
```text
* Hello world in CA-Easytrieve Plus

JOB
    DISPLAY 'HELLO, WORLD!'
```
[Source File](../libraries/nonenglish/CA-Easytrieve Plus)

##### Caché Object Script
```text
HelloWorld	;Hello World in Caché Object Script
Start	;
    Write "Hello world"
    Quit
```
[Source File](../libraries/nonenglish/Caché Object Script)

##### Casio BASIC
```text
'Hello World in Casio-Basic. [new line symbol here (press EXE)]
"Hello World!"
```
[Source File](../libraries/nonenglish/Casio BASIC)

##### Common Lisp
```text
;;; Hello world in Common Lisp

(print "Hello World")
```
[Source File](../libraries/nonenglish/Common Lisp)

##### Console Postscript
```text
%% Hello World in Console PostScript

serverdict begin 0 exitserver
/Courier findfont
48 scalefont setfont
22 22 moveto
(Hello World!) show
showpage

%% End
```
[Source File](../libraries/nonenglish/Console Postscript)

##### Cω
```csharp
System.Console.WriteLine("Hello World");
```
[Source File](../libraries/nonenglish/Cω.cs)

##### C∗
```text
#include <stdio.h>

main()
{
    printf("Hello World\n");
}
```
[Source File](../libraries/nonenglish/C∗)

##### C♯
```text
//Hello World in C#
class HelloWorld
{
    static void Main()
    {
        System.Console.WriteLine("Hello, World!");
    }
}
```
[Source File](../libraries/nonenglish/C♯)

##### Déjà Vu
```text
!print "Hello world!"
```
[Source File](../libraries/nonenglish/Déjà Vu)

##### ELENA 3
```text
// Hello world in ELENA 3.0

program =
[
    console writeLine:"Hello world!".
].
```
[Source File](../libraries/nonenglish/ELENA 3.0)

##### ELENA 4
```text
// Hello world in ELENA 4.0

public program()
{
    console.writeLine("Hello world!")
}
```
[Source File](../libraries/nonenglish/ELENA 4.0)

##### EOS 2
```text
// Hello world in EOS 2

Fenster:Fenster
Text:Textfeld

Fenster.zeichne(Text)
Text.zeileHinzufügen("Hello, World!")
```
[Source File](../libraries/nonenglish/EOS 2)

##### Fjölnir
```text
;; Hello World in Fjölnir (Icelandic programming language)

"hello" < main
{
   main ->
   stef(;)
   stofn
       skrifastreng(;"Halló Veröld!"),
   stofnlok
}
*
"GRUNNUR"
;
```
[Source File](../libraries/nonenglish/Fjölnir)

##### Flaming Thunder
```text
# Write "Hello world" in Flaming Thunder.

Write "Hello world".
```
[Source File](../libraries/nonenglish/Flaming Thunder)

##### GameMonkey Script
```text
// Hello World in GameMonkey Script

print("Hello World");
```
[Source File](../libraries/nonenglish/GameMonkey Script)

##### Genero BDL
```text
-- Hello world in Genero BDL

main
   display "hello world"
end main
```
[Source File](../libraries/nonenglish/Genero BDL)

##### ICL SCL
```text
@ HELLO WORLD IN ICL SCL
BEGIN
    SEND_MESSAGE("HELLO WORLD")
END
```
[Source File](../libraries/nonenglish/ICL SCL)

##### Informix 4GL
```text
# Hello World in Informix 4GL

MAIN

  DISPLAY "Hello World"

END MAIN
```
[Source File](../libraries/nonenglish/Informix 4GL)

##### Ingres ABF
```text
/* Hello World in Ingres ABF */
procedure hello =
begin
  message 'Hello, World' with style=popup;
end
```
[Source File](../libraries/nonenglish/Ingres ABF)

##### Java  _Mobile
```text
// Hello World on a mobile Java device

package helloworld;

import javax.microedition.midlet.*;
import javax.microedition.lcdui.*;

public class HelloWorld extends MIDlet {

  public HelloWorld()
  {
    Form form = new Form("Hello World");
    form.append("Hello world!");
    Display.getDisplay(this).setCurrent(form);
  }

  protected void pauseApp() {  }
  protected void startApp() throws
    javax.microedition.midlet.MIDletStateChangeException {  }
  protected void destroyApp(boolean parm1) throws
    javax.microedition.midlet.MIDletStateChangeException {  }
}
```
[Source File](../libraries/nonenglish/Java  _Mobile)

##### Java  _Servlet
```text
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

//
// Hello World Java Servlet
//
public class HelloWorld extends HttpServlet {
public void service(HttpServletRequest request,
HttpServletResponse response)
throws IOException {

response.setContentType("text/html");
PrintWriter out = response.getWriter();

out.println("<html><body>");
out.println("Hello World!");
out.println("</body></html>");
}
}
```
[Source File](../libraries/nonenglish/Java  _Servlet)

##### Java  _Swing
```text
// Hello World in Java using Swing GUI

class HelloWorldSwing {
  static public void main(String args[]) {
    javax.swing.JOptionPane.showMessageDialog(null,"Hello world!");
  }
}
```
[Source File](../libraries/nonenglish/Java  _Swing)

##### Java Server Pages
```text
<!-- Hello World for Java Server Pages -->

<%@ page language='java' %>
<%="Hello World!" %>
```
[Source File](../libraries/nonenglish/Java Server Pages)

##### LIMS Basic
```text
'Hello World in LIMS Basic
msgbox("hello world")
```
[Source File](../libraries/nonenglish/LIMS Basic)

##### Logo  _graphical
```text
; Hello World in LOGO, graphical output.

go 20 , left 180,
go 40 , left 180,
go 20 , right 90,
go 20 , left 90 ,
go 20 , left 180,
go 40 , left 90 ,
go 20 , left 90 ,
go 20 , right 90 ,
go 20 , right 90 ,
go 10 , right 90 ,
go 20 , left 90 ,
go 10 , left 90 ,
go 30 , left 90 ,
go 40 , left 180,
go 40 , left 90 ,
go 20 , left 90 ,
go 40 , left 180,
go 40 , left 90 ,
go 40 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 60 , left 90 ,
go 40 , left 180,
go 40 , left 90 ,
go 20 , left 90 ,
go 20 , left 180,
go 20 , left 90 ,
go 20 , left 90 ,
go 40 , left 180,
go 40 , left 90 ,
go 40 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 40 , left 90 ,
go 20 , right 90,
go 20 , right 90,
go 5 , left 90  ,
go 5 , left 90  ,
go 25 , left 180,
go 40 , left 90 ,
go 40 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 20 , left 90 ,
go 40 , left 180,
go 40 ,
```
[Source File](../libraries/nonenglish/Logo  _graphical)

##### Lotus Note Formula
```text
REM "Lotus Note Formula Language";
@Prompt([ok];"Hi there";"Hello World");
```
[Source File](../libraries/nonenglish/Lotus Note Formula)

##### Lotus Script
```text
' Hello World in Lotus Script
Sub Initialize
        Msgbox "Hello world", 0, "Hi there!"
End Sub
```
[Source File](../libraries/nonenglish/Lotus Script)

##### LÖVE
```text
-- Hello world in LÖVE

function love.draw()
    love.graphics.print('Hello World!', 400, 300)
end
```
[Source File](../libraries/nonenglish/LÖVE)

##### MDM Zinc
```text
// Hello world in MDM Zinc

mdm.Dialogs.prompt("Hello World");
mdm.Application.exit();
```
[Source File](../libraries/nonenglish/MDM Zinc)

##### MPLAB IDE
```text
; Hello world in MPLAB IDE

load_HELLO_W
lfsr2,0x100
movlwd'11'
movwfPOSTINC2
movlw"H"
movwfPOSTINC2
movlw"E"
movwfPOSTINC2
movlw"L"
movwfPOSTINC2
movwfPOSTINC2
movlw"O"
movwfPOSTINC2
movlw" "
movwfPOSTINC2
movlw"W"
movwfPOSTINC2
movlw"O"
movwfPOSTINC2
movlw"R"
movwfPOSTINC2
movlw"L"
movwfPOSTINC2
movlw"D"
movwfPOSTINC2
SEND_HELLO_WORLD
lfsr1,0x100
movf    POSTINC1,w
movwfstr_length
SLmovf       POSTINC1,w
movwfTXREG
TX_wait
btfss      TXSTA,TRMT
braTX_wait
decfszstr_length,f
braSL
DONE_MESSAGE
nop
```
[Source File](../libraries/nonenglish/MPLAB IDE)

##### MS Small Basic
```text
' Hello World in Microsoft Small Basic

TextWindow.WriteLine("Hello, World")
```
[Source File](../libraries/nonenglish/MS Small Basic)

##### MySQL FUNCTION
```text
-- Hello world in MySQL FUNCTION

DELIMITER $$
CREATE FUNCTION hello_world() RETURNS TEXT COMMENT 'Hello World'
BEGIN
  RETURN 'Hello World';
END;
$$
DELIMITER ;
 
SELECT hello_world();
```
[Source File](../libraries/nonenglish/MySQL FUNCTION)

##### Pascal  _Windows
```text
{ Hello World in Borland Pascal 7 for MS-Windows}

PROGRAM HelloWorld;

USES
  WinCRT;

BEGIN
  InitWinCRT;
  WriteLn('Hello World!');
  ReadLn;
  DoneWinCRT;
END.
```
[Source File](../libraries/nonenglish/Pascal  _Windows)

##### Perl 6
```text
# Hello world in Perl 6

say 'Hello World!';
```
[Source File](../libraries/nonenglish/Perl 6)

##### Plankalkül
```text
R1.1(V0[:sig]) => R0
R1.2(V0[:m x sig]) => R0
0 => i | m + 1 => j
[W [ i  i ] ] ]
END
R1.3() => R0
'H';'e';'l';'l';'o';',';' ';'w';'o';'r';'l';'d';'!' => Z0[: m x sig] R1.2(Z0) => R0
END
```
[Source File](../libraries/nonenglish/Plankalkül)

##### Pocket Calculator
```text
Hello World for standard pocket calculators (7-segment display).
Type in and turn calculator upside down.

0.7734
```
[Source File](../libraries/nonenglish/Pocket Calculator)

##### PureBasic  _Console
```text
; Hello World in PureBasic (console program)

OpenConsole()
   ConsoleTitle ("Hello World!")
   PrintN ("Hello World!")
CloseConsole()
```
[Source File](../libraries/nonenglish/PureBasic  _Console)

##### PureBasic  _Messagebox
```text
; Hello World in PureBasic (message box)

MessageRequester("Hello World Messagebox","Hello World!")
```
[Source File](../libraries/nonenglish/PureBasic  _Messagebox)

##### PureBasic  _Window
```text
; Hello World in PureBasic (Window)

If OpenWindow(0, 216, 0, 268, 133,  #PB_Window_SystemMenu | #PB_Window_TitleBar | #PB_Window_ScreenCentered , "Hello World Window")
 If CreateGadgetList(WindowID())
   TextGadget(1, 100, 60, 60, 20, "Hello World!")
 EndIf
EndIf

Repeat    ; Message Loop
Until WaitWindowEvent() = #PB_EventCloseWindow
```
[Source File](../libraries/nonenglish/PureBasic  _Window)

##### Python 2
```text
# Hello world in Python 2

print "Hello World"
```
[Source File](../libraries/nonenglish/Python 2)

##### Python 3
```text
# Hello world in Python 3 (aka Python 3000)

print("Hello World")
```
[Source File](../libraries/nonenglish/Python 3)

##### Rational Rose
```text
' Hello World in Rational Rose scripting language
Sub Main
    RoseApp.WriteErrorLog "Hello, World!"	
End Sub
```
[Source File](../libraries/nonenglish/Rational Rose)

##### Regular Expression
```text
Hello World as a regular expression.
Replaces everything with "Hello World".
For use with vi, sed, etc.

Search String :  ^.*$
Replace String: 'Hello World'
```
[Source File](../libraries/nonenglish/Regular Expression)

##### Rexx  _simple
```text
/* Hello World in Rexx, simple version (writes to standard output) */

say 'Hello World!'
exit
```
[Source File](../libraries/nonenglish/Rexx  _simple)

##### Rexx  _window
```text
/* Hallo World in Rexx, opens window */

call RxFuncAdd 'SysLoadFuncs', 'RexxUtil', 'SysLoadFuncs'
call SysLoadFuncs
call RxMessageBox 'Hello World!', 'Hello World Window', 'OK', 'EXCLAMATION'
exit
```
[Source File](../libraries/nonenglish/Rexx  _window)

##### RPG IV v3-4
```text
H* Hello world in RPG IV versions 3 and 4

D msg             S             32    inz(*blank)
D wait            S              1

C                   eval      msg = 'Hello World'

C     msg           dsply                   wait


C                   eval      *inlr = *on
```
[Source File](../libraries/nonenglish/RPG IV v3-4)

##### RPG IV v5
```text
// Hello world in RPG IV version 5

D wait           S              1

  /Free
   dsply ( 'Hello World!') ' ' wait;

   *inlr = *on;
```
[Source File](../libraries/nonenglish/RPG IV v5)

##### RPG IV v7
```text
// Hello world in RPG IV version 7.1

dcl-s wait char(1);

dsply ( 'Hello World!') ' ' wait;

*inlr = *on;
```
[Source File](../libraries/nonenglish/RPG IV v7.1)

##### Smalltalk  _simple
```text
"Hello World in Smalltalk (simple version)"

Transcript show: 'Hello World!'.
```
[Source File](../libraries/nonenglish/Smalltalk  _simple)

##### Smalltalk  _window
```text
"Hello World in Smalltalk (in an own window)"
"(to be entered in a special browser)"

VisualComponent subclass: #HelloWorldView
	instanceVariableNames: ''
	classVariableNames: ''
	poolDictionaries: ''
	category: 'test'

displayOn: aGraphicsContext

	'Hello World!' asComposedText displayOn: aGraphicsContext.

open

	|window|
	window := ScheduledWindow new.
	window label: 'Hello World Demo:'.
	window component: self new.
	window open.
```
[Source File](../libraries/nonenglish/Smalltalk  _window)

##### Smalltalk MT
```text
"Hello World in Smalltalk MT

FrameWindow new
   title: 'Hello World';
   open
```
[Source File](../libraries/nonenglish/Smalltalk MT)

##### Splunk SPL
```text
| makeresults `comment("Hello world in Splunk SPL")` | eval mystring="Hello, World!"
```
[Source File](../libraries/nonenglish/Splunk SPL)

##### SQL  _Advantage
```text
-- Hello World in SQL for Advantage Database
 
select 'Hello World' from system.iota
```
[Source File](../libraries/nonenglish/SQL  _Advantage)

##### SQL  _DB2
```text
-- Hello World in SQL for DB2
VALUES('hello world')
```
[Source File](../libraries/nonenglish/SQL  _DB2)

##### SQL  _Oracle
```text
# Hello World in SQL for Oracle

SELECT 'Hello World' FROM dual;
```
[Source File](../libraries/nonenglish/SQL  _Oracle)

##### TI BASIC
```text
10 REM Hello World in TI BASIC
20 REM for the TI99 series computer
100 CALL CLEAR
110 PRINT "HELLO WORLD"
120 GOTO 120
```
[Source File](../libraries/nonenglish/TI BASIC)

##### TI Extended BASIC
```text
10 REM Hello World in Extended BASIC
20 REM for the TI99 series computer
100 CALL CLEAR :: DISPLAY AT(10,5):"Hello World" :: ACCEPT AT(20,4):A$
```
[Source File](../libraries/nonenglish/TI Extended BASIC)

##### TSO CLIST
```text
PROC 0
/* Hello World in TSO CLIST */
write Hello World!
```
[Source File](../libraries/nonenglish/TSO CLIST)

##### Turing Machine
```text
Hello World as a Turing machine.

State   Read   |   Write     Step    Next state
---------------|---------------------------------
1       empty  |   H         >       2
2       empty  |   e         >       3
3       empty  |   l         >       4
4       empty  |   l         >       5
5       empty  |   o         >       6
6       empty  |   blank     >       7
7       empty  |   W         >       8
8       empty  |   o         >       9
9       empty  |   r         >       10
10      empty  |   l         >       11
11      empty  |   d         >       12
12      empty  |   !         >       STOP
```
[Source File](../libraries/nonenglish/Turing Machine)

##### Unix Shell
```text
# Hello world for the Unix shells (sh, ksh, csh, zsh, bash, fish, xonsh, ...)

echo Hello World
```
[Source File](../libraries/nonenglish/Unix Shell)

##### VAX Macro
```text
Hello World in VAX Macro.

        .title  helloworld
        .ident  /hello world/
;
        .library        /sys$library:lib/
        $libdef
        $lib$routinesdef


        .psect  $data,wrt,noshr,noexe,long

hello:  .ascid  /Hello World!/

        .psect  $code,nowrt,shr,exe,long

        .entry  helloworld,^m<r9,r10,r11>

        pushaq  hello                   ; output the
message
        calls   #1,g^lib$put_output     ;

        ret                             ; GTFOH
        .end    helloworld              ;
```
[Source File](../libraries/nonenglish/VAX Macro)

##### VAX-11 Macro
```text
; Hello World in VAX-11 MACRO

        .title hello
term_name:      .ascid /SYS$INPUT/
term_chan:      .blkw 1
out_iosb:       .blkq 1
msg:    .asciz  /Hello, world!/

        .entry start,0

        ; establish a channel for terminal I/O
        $assign_s devnam=term_name,-
                chan=term_chan
        blbc r0,error

        ; queue the I/O request
        $qio_s chan=term_chan,-
                func=#io$_writevblk,-
                iosb=out_iosb,-
                p1=msg,-
                p2=#13
        blbc r0,error

        $exit_s ; normal exit

error:  halt ; error condition

        .end start
```
[Source File](../libraries/nonenglish/VAX-11 Macro)

##### VBA  _Excel
```text
' Hello world in Visual Basic for Applications, Excel version

Private Sub Workbook_Open()
    MsgBox "Hello world!"
End Sub
```
[Source File](../libraries/nonenglish/VBA  _Excel)

##### VBA  _Word
```text
' Hello world in Visual Basic for Applications, Word version

Private Sub Document_Open()
    MsgBox "Hello world!"
End Sub
```
[Source File](../libraries/nonenglish/VBA  _Word)

##### Vim script
```text
" Hello world in Vim script

:echom "Hello world!"
```
[Source File](../libraries/nonenglish/Vim script)

##### Visual Basic
```text
REM Hello World in Visual Basic for Windows

VERSION 2.00
Begin Form Form1
   Caption         =   "Form1"
   ClientHeight    =   6096
   ClientLeft      =   936
   ClientTop       =   1572
   ClientWidth     =   6468
   Height          =   6540
   Left            =   876
   LinkTopic       =   "Form1"
   ScaleHeight     =   6096
   ScaleWidth      =   6468
   Top             =   1188
   Width           =   6588
   Begin Label Label1
      Caption         =   "Hello World!"
      Height          =   372
      Left            =   2760
      TabIndex        =   0
      Top             =   2880
      Width           =   972
   End
End
Option Explicit
```
[Source File](../libraries/nonenglish/Visual Basic)

##### Visual Basic 
```text
'Hello World in Visual Basic .NET (VB.NET)

Imports System.Console

Class HelloWorld

    Public Shared Sub Main()
        WriteLine("Hello, world!")
    End Sub

End Class
```
[Source File](../libraries/nonenglish/Visual Basic .NET)

##### Visual Basic 6
```text
' Hello World in Visual Basic 6

Private Sub Form_Load()
Print "Hello World"
End Sub
```
[Source File](../libraries/nonenglish/Visual Basic 6)

##### Visual FoxPro
```text
*Hello World in Microsoft Visual FoxPro 5-9
? "Hello World!"
```
[Source File](../libraries/nonenglish/Visual FoxPro)

##### Visual Prolog
```text
/* Hello World in Visual Prolog */

goal
    console::init(),
    stdio::write("Hello World!").
```
[Source File](../libraries/nonenglish/Visual Prolog)

##### VisualWorks Smalltalk
```text
"Hello World! in VisualWorks Smalltalk"

Dialog warn: 'Hello World!'.
```
[Source File](../libraries/nonenglish/VisualWorks Smalltalk)

##### µ6
```text
,200,245,300,300,303,112,52,223,303,310,300,244,53
```
[Source File](../libraries/nonenglish/NonEnglish-1/µ6.mu6)

##### Ć
```text
public class HelloCi
{
    public static string GetMessage()
    {
        return "Hello World";
    }
}
```
[Source File](../libraries/nonenglish/Ć.ci)

##### ˸;#？!
```text
:H:e:l:l:o: :W:o:r:l:d!
```
[Source File](../libraries/nonenglish/˸;#？!)

##### μλ
```text
>  EEEEEEEΔΔΘς       v
v  ςΘΔEEEEEEEEEE     <
>  EEEEEEEEEEEδδΘς   v
v  ΘδδEEEEEEEEEEEς   <
>  ς EEEEEEEEEEEΔΘ   v
v  ΘΔΔΔΔEEEEς        <
>  ςEEEΔΔΘ           v
v  ΘδEEEEEEEEEEEEς   <
>  ςEEEEEEEEEEEΔΘ    v
v  ΘΔΔΔΔEEEEEEEEEEEς <
>  ςEEEEEEEEEEEδδΘ   v
v  ΘEEEEEEEEEEς      <
>  ςEEEΔΔΔΘ          λ
```
[Source File](../libraries/nonenglish/μλ)

##### قلب _2
```text
Hello world in قلب

‫(قول "مرحبا يا عالم!")
```
[Source File](../libraries/nonenglish/قلب _2)

##### உயிர்-Uyir
```text
முதன்மை என்பதின் வகை எண் பணி {{
         ("உலகத்தோருக்கு வணக்கம்") என்பதை திரை.இடு;

         முதன்மை = 0;
}};
```
[Source File](../libraries/nonenglish/உயிர்-Uyir)

##### ᚱᚢᚾᛅᛦ
```text
ᛋᚭᚭᚭᚭᚭᚭᚭᚭᚭᚭᚭ
ᛁ͗̿ᛁ̊ᛁ̳͗̿ᛁ̹̊ᚹᛁ̿ᛁ̊ᛁ͗ᛁ̊ᛁ̹̊ᛁ̊̿ᛧ
```
[Source File](../libraries/nonenglish/ᚱᚢᚾᛅᛦ)

##### ∗
```text
*
```
[Source File](../libraries/nonenglish/∗)

##### ∗﹥﹤﹥
```text
"Hello World"r>Ool?u!|;
```
[Source File](../libraries/nonenglish/∗﹥﹤﹥)

##### うんちく
```text
「Hello World」って書く。
```
[Source File](../libraries/nonenglish/うんちく.unchk)

##### なでしこ
```text
「Hello World」と表示
```
[Source File](../libraries/nonenglish/なでしこ.nako)

##### ひまわり
```text
「Hello World」と、表示。
```
[Source File](../libraries/nonenglish/ひまわり.hmw)

##### タイルズ
```text
N4IgLglmA2CmIC4QAlbWgewAQHUMCdoATEAGhCNgGcBjREM8COKgNVn3oBEBGAdh4AmAEaMqGAK74asZGAC20RKAAM9ADoA7dWB16wWQ0eOGAPNAhYa0AIZUqAXnUhYRMAH18GAO5ZXHmnkiAFoafFgbMFhnLCJIm2CJCCInEABVAGYiAFZsjIA2G34YqjAATzhU5wA+LRMjUyIIADdazXr6xparW3tU-3cbcJs-N3cABxtNNBq6jvmu1rn5laxFnrtHZxthdyo0WBoDAYxhACtD3RBY+OCLUtSiaABzABkIUoB5c8uYuLAEs0bNAJLBUs98MkaqYAPRNJbtVYmdbWTb9MZhCJRdwQ5KjDyTabQWaIzrwtpItbwjZ9ZwDGg2caCGqAewZAA4MsPJ600NnkYOcuKIOGSYAAFjFUbSQDt3JoJPJhBw-rcgSD+SAeNCqISsKUKurvKKoLBgtqbDIEFhND58IyANw1Hiws2aaqcloUpEo3pbFwYxnMkDVQAbWYBVBndrW5vPVgtQEGeoquNN9MrlCqV13+gOBoNSmqDpggmnGEgM5XG6rTivwEp9qVT8urMUmYCi+E0jwAVCVypVnN4RaLLdkACzjAAedqw8iLwQHbiHWFHE6n8hs47ng+HY8nWAAZhhNGBTRAAF6wS08HdTpra2xlS3W6YOgsu3W9g1GqKmyYWq02+1HWdQk3ThD1lmRMCEQWckIJg7oeT5cFISId5plrNFtl2GgMEwGtrj1PsQGEc0AGsIUkTQQhwvDLQAYiIRiX2qQAt3wjT1Oigji1i49i4K9alJV9E5xkgQ8qGhLj+M42DSRWUxhFLMBD2TetdkU1tD3cABHJJYGOMYwFtKhxQLGENOU11pJ42TjFhCw3QsVS6TGLxfHpIJQmGKJ8XcGgpHCI9lQBRJklSTIcjyfIAE5opUHt9SqINrMWbj4OaZy-Q8IYIl8wkZmSuTKVS6zisEussL2A4jl804LiOYKEnuMBHhed4vh+BrMxVHN1UgOBJNsykGnKzCsr87zYHcfrYDyqYCrSkbwKKjpvTG+kAxqQBYFUAWSV2KjJDnBmgA5aMMKlE5zmCRDZplKJxyTNdxzgTRnjFPNska4JVVzZxAH6GQAShkAa4ZgnzapAZBp0pJWsxofSxayW6IT0QCTag0AWjlAGq4-bqRu1IZtYXrzuEjFDyiI8sBlHCFQwL7mtat4PjAABJNdnmiAtRqlKmMBp4J7qTLNvt61JUHQbA8EIIhoSLEsyzKCt8dgB7ibU6blaTQiDS3LAr0EFdp1necxUvEd9d3J7NwXU3zanA8jxPc9TYN29xnvR9D1gZjTDfLXUkNY0f3NC9-28W1xmYsXMFwAhiGAqZQK5CyVORyrqeEDBgmT7QzOzxPloWOGGl43iuZJgJJum5gOYRqkkYq8aGSZGpACorHGEOjfHq4ADVVyqqwzaooaGxGMtTxu0eqQAyP3bjK8aO6uAE0++lXYB-woe+Jhuu587he4AAYVwggV55vDKd2IypjNQLNY-VISJocivAkKjQmP-BLXwZ4SIAChUUgWAAFAMASoAAlMxQATkFb3SplESYlNBZyUoeQaBdi4j2GmtC6YwMCiQgOJBKRFXbu3-M+aEZcUYTSxFNGatU8EoMKrA8eG1m5BnZLPK0e8mBwGFAuU+a9GyD2Hmg0ecD-SsJDOGUuHdDrcNkLAeMiZ+GykERvYR0FVq4y4TNAAKhrI+eFlE0RPgRe+zhH7P0otRD+9F8h2OYoAdW0YHoI9Fg8uVDIg0OrnQhBJImENxYYGaogA9tUAEdxHD55yIAEoYABFEZR68agqGcaI5h4igmAFnlcJ0jd6yJmgAMQsOMZR+w4BdRuCFemzgniM1KIUiAxTuohR+pWWmQZABWDIAdQYUnIi0Xk6uaEOaZTPgQC+01bSaBvrAIKpjErmLIhRV+1jaJX0mZMW+zE2JF1hlyChLkK7UKrnAHx+Cc61zcZQpuQTAAccoAfwYInaOrlEmwTQJASWuOPBs6YN7JO2b0+u610k1EALLygA7fw4Z83YpTfjXEiTNAAghYZ4OcKlNSZgzdqYBEXxhRULFpSVqiACvAwAq0o9P2n8wuGCFjZ2GepZBmgdJ6QMh4K+JlJJ5xSn8+yEBHKWDSR4NyJJ9D6GGktSM0NhW6AMF6GEDktCSp0PMEAABfcg4gpAyExcoEAagEAAG1QCBBIEgTEnjGBJGNekLIuQChFD4IwOqOiFbwCQIKRggpeFinoDwd1KE4wJjAN631yRBn0G-sIX+ghBA8EAVGmNWA41gJVaQQ1QR6CmqiOa5I9AIo2pinFB15wnUVnoDNRgJ1oz0AhqDctPcg3kBmovetcjPWimbTNf1iZ21PNiWapAagG3V3qeMeg1pa1wGea8qg9AB1yOxci+g47YAGIIGGn+Nh-6gK3UApNg64B6IeiuzgSBw2-x4CoQQgDz2Xt1he3dcjQ0nvXZukBr7wFLsJmqegUcJaxxIOQWWiA9zAn2AB+QzwgMgdgMqgAuqqkAdVTp8gAEJlDSNmhAqhtXmkgM0F1RlQQNudfQcYXg6DkBuvQQAhwwA0AM8MyarWRQyNkWAwgfWYelEcFoLrgPQFA+AYjSAy0UcrUgatPr4O5qirFXVoAcPccQAR2ARGS1CerowSjYngY1sk9aqKfAXnYa43hyDfHlMCdUyAN1Im+T0EAHsMgBOhkAHduDGpO2v4EZ3D+H8CEYsy6qzKENOiZAI5lzyr4N1XQ0QVDSGXWgDdRx0LiA9WMbzXakAcHyCkYwHQDjNH6P6pUJluR2rxPJdS9JgtxWM7jmUPByAfJj3AHC+Qfy+B8AAAUyNRcQCoZVQA
```
[Source File](../libraries/nonenglish/NonEnglish-1/タイルズ.tls)

##### ドリトル
```text
ラベル！（"Hello World"）作る。
```
[Source File](../libraries/nonenglish/ドリトル.dtl)

##### プロデル
```text
「Hello World」と出力する
```
[Source File](../libraries/nonenglish/プロデル.rdr)

##### 文言
```text
吾有一言。曰「「Hello World」」。書之。
```
[Source File](../libraries/nonenglish/文言.wy)

##### 易语言
```text
调试输出(“Hello World”）
```
[Source File](../libraries/nonenglish/易语言.e)

##### 火星文
```text
姠屛募潑鎹牸苻賗：【沵恏，迣鎅】。
蔠圵姟珵垿。
```
[Source File](../libraries/nonenglish/火星文.martian)

##### 秀丸マクロ
```text
message "Hello World";
```
[Source File](../libraries/nonenglish/秀丸マクロ.mac)

##### ﹥﹤﹥
```text
"Hello World"r\
          o;!?l<
```
[Source File](../libraries/nonenglish/﹥﹤﹥)

##### ？$51=
```text
$? 5 Hello World 5
```
[Source File](../libraries/nonenglish/NonEnglish-1/？$51=)

##### 🆒
```text
💬🔤👋🗺️🔤
```
[Source File](../libraries/nonenglish/🆒)

