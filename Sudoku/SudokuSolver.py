#!/usr/bin/env python
# coding: utf-8

# # Resolutor de Sudokus usando e algortimo de backtracking

# In[1]:

tabela_inicial =[[6,0,3,0,5,0,2,0,4],
                 [0,4,5,0,0,0,6,9,0],
                 [0,8,0,9,6,4,0,1,0],
                 [0,0,0,5,8,1,0,0,0],      
                 [0,0,9,3,0,6,7,0,0],
                 [0,0,0,7,9,2,0,0,0],
                 [0,7,0,2,1,5,0,3,0],
                 [0,5,4,0,0,0,1,2,0],
                 [2,0,8,0,3,0,5,0,6]];


# In[2]:

def imprimir_tabela(t):
    for f in range(len(t)):
        print(t[f])
    print(" ")    


# In[3]:

imprimir_tabela(tabela_inicial)


# In[4]:

def sudoku(i,j,inicial,solucao):
    if inicial[i][j] == False:
        for k in range(1,10):
            solucao[i][j] = k
            if e_factivel(i,j,solucao):
                if i == 8 and j == 8: imprimir_tabela(solucao)
                if i < 8 and j == 8: sudoku(i+1, 0, inicial, solucao)
                if i <= 8 and j < 8: sudoku(i, j+1, inicial ,solucao)
            solucao[i][j] = 0
    else:
        if i == 8 and j == 8: imprimir_tabela(solucao)
        if i < 8 and j == 8: sudoku(i+1, 0, inicial, solucao)
        if i <= 8 and j < 8: sudoku(i, j+1, inicial ,solucao)


# In[5]:

def e_factivel(i,j,solucao):
    valido = True
    k = 0
    while k <= 8 and valido:  # Verificamos a coluna
        if solucao[i][j] == solucao[k][j] and k != i:
            valido = False
        k = k + 1
    l = 0
    while l <= 8 and valido: # Verificamos a linha
        if solucao[i][j] == solucao[i][l] and l != j:
            valido = False
        l = l +1
    k = correspondencia3x3(i);
    l = correspondencia3x3(j);

    # Verificamos o subgrupo 3x3
    while k < correspondencia3x3(i) + 3 and valido:
        while l < correspondencia3x3(j) + 3 and valido:
            if solucao[i][j] == solucao[k][l] and i != k and j != l:
                valido = False
            l = l + 1
        k = k + 1
        l = correspondencia3x3(j)
    return valido    


# In[6]:

def correspondencia3x3(i):
    resultado = (i//3)*3
    return resultado    


# In[7]:

tabela_solucao = [[0 for x in range(9)] for y in range(9)] 
for n in range(len(tabela_inicial)):
    for m in range(len(tabela_inicial[n])):
        tabela_solucao[n][m] = tabela_inicial[n][m]
        
sudoku(0,0,tabela_inicial,tabela_solucao)

