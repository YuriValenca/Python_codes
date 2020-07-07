class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota: '))
        print(x)
        if x > 10:
            raise InputError('Nota nao pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota nao pode ser menor que 0')
        break
    except ValueError:
        print('Valor invalido. Por favor digite um numero')
    except InputError as ex:
        print(ex)