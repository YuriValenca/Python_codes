# arquivo = open('teste.txt', 'a')
# arquivo.write('Minha primeira escrita\n')
# arquivo.write('Segunda linha\n')
# arquivo.close()
#Se rodar o codigo com outra string na funcao write, ela vai sobrescrever o que ja esta presente,
#caso o parametro passado na funcao open seja w. se for a, ele atualiza com o novo texto

def escrever_arq(texto):
    arquivo = open('teste.txt', 'w')
#quando o parametro w e passado, e possivel designar o diretorio que sera criado o arquivo:
#arquivo = open('C:/Documents/Portfolio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arq(nome_arq, texto):
    arquivo = open(nome_arq, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arq(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arq):
    arquivo = open(nome_arq, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def escrever_lista_media(nome_arq, texto):
    arquivo = open('medias.txt', 'a')
    arquivo.write(lista_media)
    arquivo.close()

def print_lista_media(nome_arq):
    arquivo = open(nome_arq, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    atualizar_arq('medias.txt', str(lista_media))
    print_lista_media('medias.txt')
    # escrever_arq('Primeira linha.\n')
    # atualizar_arq('Segunda linha\n')
    # ler_arq('teste.txt')
    # aluno = 'Lucas Asafe: 9, 3, 7, 8\n'
    # atualizar_arq('notas.txt', aluno)



# metodo para copiar arquivos para outro diretorio
# def copia_arq(nome_arq):
#     import shutil #essa importacao pode ser feita no comeco do arquivo, para evitar repeticao
#                   #da importacao, ja que, nesse caso, o escopo dela e local
#     shutil.copy(nome_arq, diretorio desejado/"rename se desejado")
#
# metodo para mover arquivos para outro diretorio
# def mover_arq(nome_arq):
#     shutil.move(nome_arq, diretorio desejado/"rename se desejado")
#
#
# no main:
#     copia_arq('notas.txt')
#     mover_arq('notas.txt')
