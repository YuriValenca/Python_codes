from aula7_tv import TV
from aula7_classe1 import Calculadora
from aula8_cont_letras import contador_palavras


if __name__ == '__main__':
    televisao = TV()
    calc = Calculadora(10, 5)
    print(televisao.on)
    print(calc.soma())
    lista = ['cachorro', 'elefante', 'arara']
    print(contador_palavras(lista))