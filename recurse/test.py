#!/usr/bin/env python3

def f(x):
    if x == 1:
        return 1
    return x * f(x-1)

def g(x):
    a = 1
    for i in range(1, x+1):
        a *= i
    return a

def h(x):
    if x < 1:
        return 1
    return h(x-1) + h(x-2)

def i(x):
    a = 1
    b = 1
    for i in range(x):
        c = a + b
        a = b
        b = c
    return b

def j(l):
    if l == '':
        return ''
    return l[-1] + j(l[:-1])

def k(l):
    return l[::-1]

def l(x):
    if x == 0:
        return 0
    return x + l(x-1)

def m(x):
    return sum([i for i in range(x+1)])

def n(x):
    s = 0
    for i in range(x+1):
        s += i
    return s

print(l(10))
print(m(10))
print(n(10))
