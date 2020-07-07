a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
soma = a + b
subtracao = a - b
mult = a * b
div = a / b
resto = a % b
soma = str (soma)
print('soma = ' + soma)
#ou
print('soma = ' + str(soma))
#OU AINDA
print('soma = {}'.format(soma))
#E finalmente
print('soma = {sum} \nsubtracao = {sub}\nmultiplicacao = {mult}'
      '\ndivisao = {div}\nresto da divisao = {resto}'.format(sum = soma, sub = subtracao, div = div, mult = mult, resto = resto))