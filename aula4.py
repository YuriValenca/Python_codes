# a = int(input('Digite um numero qualquer e eu lhe direi se ele e primo: '))

# count = 0
#
# for x in range (1, a + 1):
#     resto = a % x
#     if resto == 0:
#         count += 1
#
# if count == 2:
#     print('O numero {} e primo!'.format(a))
# else:
#     print('O numero {} nao e primo :/'.format(a))

a = int(input('Digite um numero e eu lhe direi quais numeros menores que ele sao primos: '))

for num in range (a + 1):

    count = 0

    for x in range (1, num + 1):
        resto = num % x
        if resto == 0:
            count += 1

    if count == 2:
        print('O numero {} e primo!'.format(num))