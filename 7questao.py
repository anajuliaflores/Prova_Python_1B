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