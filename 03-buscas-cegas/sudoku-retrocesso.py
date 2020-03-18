X=-1
puzzle1 = [
    4,8,X, X,1,3, X,2,X,
    X,X,7, X,X,X, X,X,X,
    5,X,1, X,X,9, 4,X,X,

    9,7,X, X,X,2, 8,X,X,
    X,5,X, X,X,X, X,4,X,
    X,X,8, 9,X,X, X,1,2,

    X,X,6, 7,X,X, 2,X,8,
    X,X,X, X,X,X, 1,X,X,
    X,2,X, 8,9,X, X,3,6,
]

puzzle2 = [
    X,7,X, X,X,X, 4,X,X,
    X,X,X, 9,X,X, X,X,1,
    X,3,1, X,4,X, X,2,X,

    X,4,9, 1,X,X, 3,6,X,
    3,X,X, 6,X,4, X,X,2,
    X,5,2, X,X,9, 8,1,X,

    X,9,X, X,1,X, 7,5,X,
    1,X,X, X,X,6, X,X,X,
    X,X,7, X,X,X, X,4,X,
]
VAZIO = X
del X

def pretty_print_sudoku(grid, dims=9):

    return "\n".join("|".join(str(i) if i != VAZIO else "O"
        for i in grid[l:l+dims])
            for l in range(0,dims*dims,dims))

def coords(i, dims=9):
    return i//dims, i % dims

def indices_vizinhos_de(i, dims=9):
    from math import sqrt, trunc

    l, c = coords(i, dims)
    indices_linhas = range(l*dims, l*dims+dims)
    indices_colunas = range(c, dims*dims, dims)
    
    dims_quadrante = trunc(sqrt(dims))
    lq, cq = l - l%dims_quadrante, c - c%dims_quadrante
    indices_quadrante = [range((lq+n)*dims+cq, (lq+n)*dims+cq+dims_quadrante)
        for n in range(0,dims_quadrante)]
    
    return set()\
        .union(indices_linhas, indices_colunas, *indices_quadrante)\
        .difference([i])

def _preencher_sudoku_rec(grid, i):
    if i >= 9*9:
        return True
    elif grid[i] != VAZIO:
        return _preencher_sudoku_rec(grid, i+1)
    
    numeros_vizinhos = set(grid[n] for n in indices_vizinhos_de(i))
    tentativas_validas = (n for n in range(1,10) if n not in numeros_vizinhos)
    for n in tentativas_validas:
        grid[i] = n
        if _preencher_sudoku_rec(grid, i+1):
            return True
    
    grid[i] = VAZIO
    return False

def preencher_sudoku(grid):
    return _preencher_sudoku_rec(grid, 0)


if __name__ == "__main__":
    print("Vamos tentar resolver o Sudoku a seguir:",
        pretty_print_sudoku(puzzle2), sep="\n")

    import timeit, statistics
    tempo = statistics.median( timeit.repeat("preencher_sudoku(p1_cpy)",
            setup="from __main__ import preencher_sudoku, puzzle1; p1_cpy = puzzle1.copy()",
            number=1, repeat=21) )
    
    p1_cpy = puzzle1.copy()
    if preencher_sudoku(p1_cpy):
        print("Resolvido com sucesso!", pretty_print_sudoku(p1_cpy), sep="\n")
    else:
        print("Não encontrou solução. Será que existe?")
    
    print(f'Tempo de processamento de {tempo} segundos.')