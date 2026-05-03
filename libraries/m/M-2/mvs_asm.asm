HELLO    CSECT
         USING HELLO,15
         LA    1,MSGAREA
         SVC   35
         BR    14
MSGAREA  EQU   *
         DC    AL2(19)
         DC    XL2'00'
         DC    C'Hello world!'
         END
