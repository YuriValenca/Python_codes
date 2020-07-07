
lista = [1, 10]

try:
    divisao = 10/0
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Nao e possivel realizar uma divisao por zero')
except IndexError:
    print('Erro ao acessar a variavel desejada')
except Exception as ex:
    print('Nao foi possivel completar o programa. Erro: {}'.format(ex))
else:
    print('Executa quando nao ocorre excecao')
# finally:
#     print('Sempre executa')
#     print('Fechando arquivo')
#     arquivo.close()
# Isso por que, assim que ocorre um erro no try, o escopo dele ja pula as linhas apos o erro,
# com isso, o finally executa o trecho de codigo dentro dele no matter what

#seguindo a hierarquia de exceptions, e pra botar os filhos antes dos pais, se nao, o erro
#vai cair nos de maior hierarquia, sem definir o que realmente aconteceu