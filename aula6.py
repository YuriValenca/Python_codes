conjunto = {1, 2, 2, 3, 4}
conjunto2 = {2, 3, 5, 6, 7, 8}
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto.add(5)
conjunto.discard(2)
print(conjunto)

uniao = conjunto.union(conjunto2)
print('Uniao: {}'.format(uniao)) #a uniao ignora elementos repetidos

intersec = conjunto.intersection(conjunto2)
print('Interseccao: {}'.format(intersec)) #a interseccao retorna os elementos repetidos

dif1 = conjunto.difference(conjunto2)
print('Diferenca conj - conj2: {}'.format(dif1)) #a diferenca retorna um conjunto menos o outro

dif2 = conjunto2.difference(conjunto)
print('Diferenca conj2 - conj: {}'.format(dif2)) #nessa operacao, a ordem importa!!

sym_dif = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica: {}'.format(sym_dif)) #retorna elementos que nao estao nos dois conjuntos,
               # ou seja, que so aparecem uma vez

subconj = conjunto_a.issubset(conjunto_b)
print(subconj) #retorna um boolean pra dizer se um e subconjunto do outro
#a funcao oposta ao issubset() e o issuperset()
#se a e subconjunto de b, b e superconjunto de a

#se eu tenho uma lista com elementos duplos, mas n quero essa duplicidade, uma opcao e transformar
#tal lista em um conjunto, ja q o conjunto elimina elementos repetidos

lista = ['gato', 'cachorro', 'cachorro', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)