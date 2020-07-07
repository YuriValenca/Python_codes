# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if(a > b and a > c):
#     print('O maior numero entre esses tres eh {}'.format(a))
# elif (b > a and b > c):
#     print('O maior numero entre esses tres eh {}'.format(b))
# elif (c > a and c > b):
#     print('O maior numero entre esses tres eh {}'.format(c))

# a = int(input('Primeira nota: '))
# if a > 10:
#     print('Nota invalida. \nPrimeira nota:')
# b = int(input('Segunda nota: '))
# if b > 10:
#     print('Nota invalida. \nSegunda nota:')
# c = int(input('Terceira nota: '))
# if c > 10:
#     print('Nota invalida. \nTerceira nota:')
# d = int(input('Quarta nota: '))
# if d > 10:
#     print('Nota invalida. \nQuarta nota:')

a = int(input('Primeira nota: '))
while a > 10:
    a = int(input('Voce digitou uma nota invalida. Primeira nota: '))
b = int(input('Segunda nota: '))
while b > 10:
    b = int(input('Voce digitou uma nota invalida. Segunda nota: '))
c = int(input('Terceira nota: '))
while c > 10:
    c = int(input('Voce digitou uma nota invalida. Terceira nota: '))
d = int(input('Quarta nota: '))
while d > 10:
    d = int(input('Voce digitou uma nota invalida. Quarta nota: '))

media = (a + b + c + d)/4
print('A media do aluno e: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Media do aluno: {}'.format(media))
# else:
#     print('Uma das notas digitadas foi invalida')