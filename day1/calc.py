
import wx
import sys, os

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mult(a, b):
    c = 0
    for i in range(b):
        if c == 0:
            c = a
        else:
            c = add(c, a)
    return c

def div(a, b):
    return a/b

def pwr(a, b):
    c = 0
    for i in range(b):
        if c == 0:
            c = a
        else:
            c = mult(c, b)
    return c

def remain(a, b):
    c = div(a, b)
    d = int(c)
    e = sub(c, d)
    f = mult(e, b)
    return f

def bintodec(a):
    b = a.split('.')
    c = 0
    d = 0
    for i in range(len(b)):
        for x in range(len(b[i])):
            if i == 0:
                c += int(b[i][x])*(2**(len(b[i])-add(x, 1)))
            else:
                d += int(b[i][x])*(2**(x-len(b[i])))
    return add(c, d)

def bintoOct(a):
    b = a.split(".")
    c = ""
    d = ""
    b[1] = add(str(b[1]), str(mult("0", int(remain(len(b[1])+1, 3)))))
    b[0] = add(str(mult("0", int(remain(len(b[0])+1, 3)))), str(b[0]))
    x = len(b[0])-1
    while x >= 0:
        if b[0][x:x-2] == "000"
            c = "0" + c
        if b[0][x:x-2] == "001"
            c = "1" + c
        if b[0][x:x-2] == "010"
            c = "2" + c
        if b[0][x:x-2] == "011"
            c = "3" + c
        if b[0][x:x-2] == "100"
            c = "4" + c
        if b[0][x:x-2] == "101"
            c = "5" + c
        if b[0][x:x-2] == "110"
            c = "6" + c
        if b[0][x:x-2] == "111"
            c = "7" + c
        x = x-3
        print("c "+c)
    x = 0
    while x <= len(b[1]):
        d += str(bintodec(str(b[1][x:x+3])))
        x += 3
        print("d "+d)
    return add(c, '.'+d)

print(bintoOct("111.111"))
