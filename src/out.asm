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
