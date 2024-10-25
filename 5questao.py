#Solução 1

import time
import random
start = time.time()

def tem_duplicados1(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista [j]:
                return True
    return False


def tem_duplicados2(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False


def tem_duplicados3(lista):
    elementos_vistos = set()
    for elemento in lista:
      if elemento in elementos_vistos:
        return True
    elementos_vistos.add(elemento)
    return False

lista = random.sample(range(0,1000000), 20000)
start = time.time()
tem_duplicados1(lista)
end = time.time()
duration = end - start 

print('Tempo de execução: %f' % duration)

#_______________________________________________#

start = time.time()
tem_duplicados2(lista)
end = time.time()
duration = end - start 
print('Tempo de execução: %f' % duration)

#_______________________________________________#

start = time.time()
tem_duplicados3(lista)
end = time.time()
duration = end - start 
print('Tempo de execução: %f' % duration)

"""
A resposta certa seria em que o 3° código é mais eficienteem tempo, mas consome mais espaço.
Quando eu tentei identficar os códigos não consegui entender muito bem os dois últimos, então por isso achei que o 1° código seria a respota mais viável.
"""