#!/usr/bin/env python3

import random

tempos = [40, 60, 35, 45]
media = 0
for tempo in tempos:
    media += tempo
media = media / len(tempos)

'''for _ in range(0,20):
    print(random.randint(1,27))'''

while True:
    pass
    break

notas = {'renato': 80, 'jose': 75, 'jessica': 100}
#i = 0
for i, aluno in enumerate(notas, start=1):
    print('{}- {} tirou {}.'.format(i, aluno, notas[aluno]))
    #i += 1

def transladar2d(x0=0,y0=0,x1=1,y1=1):
    '''Transforma um ponto 2D com o modulo do outro ponto 2D.
    '''

    return x0+x1, y0+y1

val_dir = True
val_esq = False
val_dir, val_esq = val_esq, val_dir

def divPorDez(val):
    return val / 10

def applyFunc(vals, f):
    '''Aplica uma função f de um argumento a todos os elementos
    da sequencia vals, e retorna uma cópia em lista.
    '''
    copia = []
    for val in vals:
        copia.append(f(val))
    
    return copia

def fib(n):
    fib0, fib1 = 0, 1
    for _ in range(n):
        fib0, fib1 = fib1, fib0+fib1
    return fib0

# Generator
def fib_gen(n):
    fib0, fib1 = 0, 1
    for _ in range(n):
        yield fib0
        fib0, fib1 = fib1, fib0+fib1

'''for n, val in enumerate(fib_gen(100)):
    print(f"{n}, {val}")'''

def rfib(n):
    return rfib(n-1) + rfib(n-2) if n > 1 else n

def memoize(f):
    memo = {}
    def apply_memo(*args):
        if args not in memo:
            novo_memo = f(*args)
            memo[args] = novo_memo
        
        return memo[args]
    
    return apply_memo

rfib = memoize(rfib)

class FibMemo():
    def __init__(self):
        self.memo = {0: 0, 1: 1}
    
    def rfib(self, n):
        if n not in self.memo:
            novo_fib = self.rfib(n-1) + self.rfib(n-2)
            self.memo[n] = novo_fib
    
        return self.memo[n]