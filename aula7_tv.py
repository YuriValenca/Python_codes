class TV:
    def __init__(self):
        self.on = False
        self.canal = 10

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def aumenta_canal(self):
        if self.on:
            self.canal += 1

    def diminui_canal(self):
        if self.on:
            self.canal -= 1


if __name__ == '__main__': #chamar isso no main vai implicar que, se eu quiser chamar a classe tv
    #em outro modulo (arquivo), o console nao va printar tudo que tem nesse modulo atual.
    #se eu printar o name via python console, vai ser o nome do modulo, se a chamada do name vier
    #pelo mesmo arquivo, o retorno sera main
    televisao = TV()
    print(televisao.on)
    televisao.power()
    print(televisao.on)
    televisao.power()
    print(televisao.on)
    televisao.power()
    print(televisao.on)
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))