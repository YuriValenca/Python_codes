class Calculadora:
#esse jeito de fazer a classe da mais flexibilidade nas operacoes
#contudo, da mais trabalho tambem, em ter que passar os parametros a cada chamada de funcao
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return (a * b)

    def divisao(self, a, b):
        return (a / b)

calc = Calculadora()
print(calc.soma(10, 2))
print(calc.subtracao(5, 3))
print(calc.multiplicacao(10, 4))
print(calc.divisao(15, 3))