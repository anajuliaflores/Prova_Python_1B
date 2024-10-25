#código A
lista = [x for x in range(5)]
print(lista)

#código B
lista = list(range(5))
print(lista)

#código C
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista)

'''
A resposta seria a, b e c dão o retorno do mesmo resultado. Eu coloquei que o código a e b dariam o mesmo resultado apenas, pois não tinha entendido completamente o código c, e como ele estava muito diferente achei que daria um resultado maior.
'''