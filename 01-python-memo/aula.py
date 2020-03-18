# Comentário
'''print("Olá Mundo!")

vazio = None

nome = "Ricardo"
print(nome)'''

# misc = [6, "ricardo", True]
# misc[-1] == misc[len(misc)-1]
# misc.append(.3)
# misc += [4,3,7]
# misc2 = list(misc)
# misc2.pop(1)
# del misc2[1]
# del misc2
# print(misc2)

# x, y, z, alpha = 3, 5, 2, .5
# x, y = y, x
# posicao = (x, y, z, alpha)
# print(posicao)

notas = {
    "Ze": 0,
    "Thiago": 3,
    "Maria": 10
}

nota = 10#int(input("Escreva sua última nota: "))
if not nota < 70 and nota > 40:
    print("Bombou!")
    nota += 10
elif nota < 85:
    print("Passou apertado, hein?!")
else:
    print("Passou bem!")

while True:
    print("Ta preso!")
    break

# for(int i=0; i < 10; i++)
i=0
while i<10:
    #codigo aqui
    i += 1
# NÃO FAÇA ISSO!

compras = [10,100,50,43]
for i, val in enumerate(compras):
    if i % 2 == 0:
        print(val)

soma = 0
for val in compras:
    soma += val

def fib(n):
    fib0, fib1 = 0, 1
    for _ in range(n):
        fib0, fib1 = fib1, fib0 + fib1
    
    return fib1 if n > 0 else fib0

def fib_gen(n):
    fib0, fib1 = 0, 1
    
    yield fib0
    for _ in range(n):
        print("{}, {}".format(fib0,fib1))
        fib0, fib1 = fib1, fib0 + fib1
        yield fib0

def move_char(x0,y0,xm,ym):
    ''' Função que desloca uma posição 2D (x0,y0) por módulo
    de vetor 2D (xm, ym).
    '''
    return x0 + xm, y0 + ym

def my_enumerate(seq, start=0, step=1):
    i = start
    for val in seq:
        yield i, val
        i+=step

def my_print(prefix, *args, **argsn):
    print(prefix, end='')
    for arg in args:
        print(", {}".format(arg), end='')
    print()

    for name in argsn:
        print("{}: {}, ".format(name, argsn[name]), end='')
    print()

notas_alunos = {
    "maria" : 10,
    "muriel" : 9
}

def soma2(a):
    a +=2
    def parcela(b):
        return a + b
    
    return parcela

def __ordenar__(vals, eh_menor=lambda a, b: a < b):
    for i in range(len(vals)):
        menor = i
        for j in range(i+1,len(vals)):
            if eh_menor(vals[j], vals[menor]):
                menor = j
        
        vals[i], vals[menor] = vals[menor], vals[i]
    
    return vals