#!/usr/bin/python3
import sys

MODE_LINE   = 0
SYMBOL_LINE = 1
NORMAL_LINE = 2

TEXT_MODE = 0
DATA_MODE = 1

SYMBOL_DISABLE = 0
SYMBOL_ENABLE  = 1

TEXT_SIGN = ".text"
DATA_SIGN = ".data"
SYMBOL_SIGN = ":"

Mode = TEXT_MODE
State = SYMBOL_DISABLE
BinaryCode = ""
SymbolTable = {}

CMD2BIN = {'LDA': '0000',\
           'STO': '0001',\
           'ADD': '0010',\
           'SUB': '0011',\
           'JMP': '0100',\
           'JGE': '0101',\
           'JNE': '0110',\
           'STP': '0111'}

def whatLine(line):
    if line == TEXT_SIGN or line == DATA_SIGN:
        return MODE_LINE
    if SYMBOL_SIGN in line:
        return SYMBOL_LINE
    if line:
        return NORMAL_LINE

def chMode(line):
    global Mode
    if line == TEXT_SIGN:
        Mode = TEXT_MODE
    if line == DATA_SIGN:
        Mode = DATA_MODE  

def chState(line):
    l = line.replace(SYMBOL_SIGN, "")
    print(l)

def toTextBin(line):
    global BinaryCode
    array = line.split(" ")
    print(array)
    binStr = CMD2BIN[array[0]]
    if len(array) > 1:
        binStr += SymbolTable[array[1]]
    if len(array) == 1:
        binStr = binStr.ljust(16,'0')
    binStr += "\n"
    BinaryCode += binStr

def toDataBin(line):
    global BinaryCode
    binStr = bin(int(line)).replace('0b','').zfill(16)
    binStr += "\n"
    BinaryCode += binStr
    

def translate(line):
    if Mode == TEXT_MODE:
        toTextBin(line)
    if Mode == DATA_MODE:
        toDataBin(line)

def asm2bin(line):
    if whatLine(line) == MODE_LINE:
        chMode(line)
    if whatLine(line) == SYMBOL_LINE:
        chState(line)
    if whatLine(line) == NORMAL_LINE:
        translate(line)

def assemble(file_path):
    f = open(file_path, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        line = line.replace("\n", "").strip()
        asm2bin(line)
    f.close()
   




def genSymbolTable(file_path):
    f = open(file_path, 'r')
    index = 0
    while True:
        line = f.readline()
        if not line:
            break
        line = line.replace("\n", "").strip()
        print(line)
        if whatLine(line) == SYMBOL_LINE:
            SymbolTable[line.replace(SYMBOL_SIGN, "")] = bin(index).replace('0b','').zfill(12)
        if whatLine(line) == NORMAL_LINE:
            index += 1
    f.close()
        
def genBinFile():
    f= open("out.bin","w+")
    f.write(BinaryCode)
    f.close()

asm_src_file_path = sys.argv[1]
genSymbolTable(asm_src_file_path)
print(SymbolTable)
assemble(asm_src_file_path)
print(BinaryCode)
genBinFile()





        


