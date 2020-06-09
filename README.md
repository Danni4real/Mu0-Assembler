# Mu0-Assembler
Assembler for mu0 cpu, implemented using python

asm rules:
    1. text part starts by a line ".text";
    2. data part starts by a line ".data";
    3. all symbols take a whole line, and end with a colon;
    
example:
.text
    while_1_loop:
        LDA zero
        SUB count
        JNE while_1_start
        JMP while_1_end
    while_1_start:
        LDA sum
        ADD base
        STO sum
        LDA count
        SUB one
        STO count
        JMP while_1_loop
    while_1_end:
        STP
.data
    count:
        5
    zero:
        0
    one:
        1
    base:
        2
    sum:
        0


Usage: ./as-mu0.py out.asm
