lista = [12, 1, 3, 5, 7]

lista_animais = ['cachorro', 'gato', 'elefante']

lista_mista = [1, 3, 'gato', 7]

print(lista_animais[1]) #sera printado o gato, pois a contagem da lista comeca no indice zer0

soma = 0

for x in lista:
    print(x)
    soma += x

print(soma)
#OU
print(sum(lista))
print(max(lista)) #printa o maior valor da lista, independente do indice
print(min(lista_animais)) #printa o menor valor da lista, como essa e de string,
# printa o de menor ordem alfabetica

nova_lista = lista_animais * 2
print(nova_lista)

if 'lobo' in lista_animais:
    print('existe um lobo na lista')
else:
    print('nao existe um lobo na lista. Sera incluido')
    lista_animais.append('lobo')
    print (lista_animais)

lista_animais.pop() #a funcao .pop retira um item da lista, se n for referido um index,
lista_animais.pop(0) #retira-se o ultimo elemento da lista
print(lista_animais)

lista.sort()
print(lista)
lista.reverse()
print(lista)

lista_animais[0] = 'papagaio'
print(lista_animais)