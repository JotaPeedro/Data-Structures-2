import sys
import os


# Cria classe para armazenar as musicas

class Music:
    # construtor do objeto Music
    def __init__(self, ano=None, duracao=None, titulo=None, artista=None,
                 genero=None, idioma=None):
        self.ano = ano
        self.duracao = duracao
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.idioma = idioma

    def __str__(self):
        return f"{self.ano}, {self.duracao}, {self.titulo}, {self.artista}, {self.genero}, {self.idioma}"


########## ler cabecalho #########


def lerCabecalho(input1):
    cabecalho = ""
    ler = open(input1, "r")
    cabecalho = ler.readline()
    size = cabecalho[5:8]
    top = cabecalho[13:15]
    qtde = cabecalho[21:23]
    status = cabecalho[30:32]

    return size, top, qtde, status, cabecalho


def Ler_Arquivo(input1):
    musics = []
    vetor = ([], [])

    with open(input1, 'r') as arq:
        w = 0
        # Lendo cada linha do arquivo como um registro

        for linha in arq:
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split('|')
            ano = campos[0].strip() if len(campos) > 0 else ""
            duracao = campos[1].strip() if len(
                campos) > 1 else ""
            titulo = campos[2].strip() if len(
                campos) > 2 else ""
            artista = campos[3].strip() if len(
                campos) > 3 else ""
            genero = campos[4].strip() if len(campos) > 4 else ""
            idioma = campos[5].strip() if len(
                campos) > 5 else ""

            # Criando um objeto game com os campos extraídos
            if (w > 0):
                music = Music(ano, duracao,
                              titulo, artista, genero, idioma)
                musics.append(music)

            w = w+1
    i = 0
    for music in musics:
        chave = str(music.titulo+music.ano)
        chave = chave.replace(" ", "")
        chave = chave.replace(",", "")
        chave = chave.upper()
        # Armazena a chave no vetor juntamente com a posicao da linha
        vetor[0].append(chave)
        vetor[1].append(i)
        i = i+1

    return musics, vetor


def busca2(musics, vetor, input2, input1):
    retorno = []
    input2 = open(input2, "r")
    busca = ""
    tipobusca = ""
    esc = ""
    idxsec = ([], [])
    idxpri = vetor

    tipobusca = input2.readline()
    busca = input2.readline()
    remove = len(busca)
    busca = busca[0:remove-1]

    print("\n   Voce esta buscando por", busca, "em", tipobusca)

    input1 = open(input1, "r")
    esc = input1.readlines()

    if tipobusca == "ano\n":
        i = 0

        for music in musics:

            chave = str(music.ano)

            # Armazena a chave secundaria no vetor juntamente com chave primaria
            idxsec[0].append(chave)

            idxsec[1].append(idxpri[0][i])
            i = i+1
        j = 0
    # Verifica se o que está sendo buscado se encontra no idx secundario
        while j < len(idxsec[1]):

            if int(idxsec[0][j]) == int(busca):

                # Caso encontre ele irá verificar onde está no indice primario

                k = 0
                l = 0
                while k < len(idxpri[1]):
                    while l < len(idxpri[1]):
                        if idxsec[1][j] == idxpri[0][l]:
                            # Armazena em input1 o arquivo com as musicas

                            # Pega o RRN da linha e adiciona ao vetor retorno para imprimir depois
                            inser = str(esc[idxpri[1][l+1]])

                            retorno.append(inser)

                        l = l+1

                    k = k+1
            j = j+1

    if tipobusca == "titulo\n":
        i = 0

        for music in musics:

            chave = str(music.titulo)
            # Armazena a chave secundaria no vetor juntamente com chave primaria
            idxsec[0].append(chave)

            idxsec[1].append(idxpri[0][i])

            i = i+1
        j = 0

    # Verifica se o que está sendo buscado se encontra no idx secundario
        while j < len(idxsec[1]):

            if idxsec[0][j].lower() == busca.lower():

                # Caso encontre ele irá verificar onde está no indice primario

                k = 0
                l = 0
                while k < len(idxpri[1]):
                    while l < len(idxpri[1]):
                        if idxsec[1][j] == idxpri[0][l]:
                            # Armazena em input1 o arquivo com as musicas

                            # Pega o RRN da linha e adiciona ao vetor retorno para imprimir depois
                            inser = str(esc[idxpri[1][l+1]])

                            retorno.append(inser)

                        l = l+1

                    k = k+1
            j = j+1

    if tipobusca == "genero\n":
        i = 0

        for music in musics:

            chave = str(music.genero)
            # Armazena a chave secundaria no vetor juntamente com chave primaria
            idxsec[0].append(chave)

            idxsec[1].append(idxpri[0][i])

            i = i+1
        j = 0

    # Verifica se o que está sendo buscado se encontra no idx secundario

        while j < len(idxsec[1]):
            genero = str(idxsec[0][j])

            if genero[0:3].lower() in busca[0:3].lower():

                # Caso encontre ele irá verificar onde está no indice primario

                k = 0
                l = 0
                while k < len(idxpri[1]):
                    while l < len(idxpri[1]):
                        if idxsec[1][j] == idxpri[0][l]:
                            # Armazena em input1 o arquivo com as musicas

                            # Pega o RRN da linha e adiciona ao vetor retorno para imprimir depois
                            inser = str(esc[idxpri[1][l+1]])

                            retorno.append(inser)

                        l = l+1

                    k = k+1
            j = j+1

    if tipobusca == "artista\n":
        i = 0

        for music in musics:

            chave = str(music.artista)

            # Armazena a chave secundaria no vetor juntamente com chave primaria
            idxsec[0].append(chave)

            idxsec[1].append(idxpri[0][i])
            i = i+1
        j = 0
    # Verifica se o que está sendo buscado se encontra no idx secundario
        while j < len(idxsec[1]):

            if idxsec[0][j].lower() == busca.lower():

                # Caso encontre ele irá verificar onde está no indice primario

                k = 0
                l = 0
                while k < len(idxpri[1]):
                    while l < len(idxpri[1]):
                        if idxsec[1][j] == idxpri[0][l]:
                            # Armazena em input1 o arquivo com as musicas

                            # Pega o RRN da linha e adiciona ao vetor retorno para imprimir depois
                            inser = str(esc[idxpri[1][l+1]])

                            retorno.append(inser)

                        l = l+1

                    k = k+1
            j = j+1

    if tipobusca == "idioma\n":
        i = 0

        for music in musics:

            chave = str(music.idioma)

            # Armazena a chave secundaria no vetor juntamente com chave primaria
            idxsec[0].append(chave)

            idxsec[1].append(idxpri[0][i])
            i = i+1
        j = 0
    # Verifica se o que está sendo buscado se encontra no idx secundario
        while j < len(idxsec[1]):

            if idxsec[0][j].lower() == busca.lower():

                # Caso encontre ele irá verificar onde está no indice primario

                k = 0
                l = 0
                while k < len(idxpri[1]):
                    while l < len(idxpri[1]):
                        if idxsec[1][j] == idxpri[0][l]:
                            # Armazena em input1 o arquivo com as musicas

                            # Pega o RRN da linha e adiciona ao vetor retorno para imprimir depois
                            inser = str(esc[idxpri[1][l+1]])

                            retorno.append(inser)

                        l = l+1

                    k = k+1
            j = j+1

    return retorno


def imprimirarq(vetorencontrado, output):

    output = open(output, "a")
    i = 0
    if len(vetorencontrado) < 1:
        output.writelines("Nenhuma musica encontrada")
        print(" Nenhuma musica foi encontrada a partir da sua busca\n")
        print("----ENCERRANDO O PROGRAMA----")
        exit()
    else:

        while i < len(vetorencontrado):
            output.writelines(vetorencontrado[i])
            i = i+1


def verificacao(input1, input2, output):

    if os.path.isfile(input1) == False:
        print("---ARQUIVO DE MUSICAS NAO ENCONTRADAO,FINALIZANDO PROGRAMA---")
        exit()

    if os.path.isfile(input2) == False:
        print("---ARQUIVO DE BUSCA NAO ENCONTRADO,FINALIZANDO PROGRAMA----")
        exit()

    input2 = open(input2, "r")
    tipobusca = input2.readline()

    if "genero" or "idioma" or "ano" or "titulo" or "artista" in tipobusca:
        input2.close()

    else:
        output = open(output, "w")
        output.writelines("Arquivo Invalido")
        print("-----------------ERRO NO ARQUIVO DE CONSULTA,ENCERRANDO PROGRAMA--------------------")
        input2.close()
        output.close()
        exit()


def main(input1, input2, output):
    print("\n--------------Inicio do programa------------")
    print("------------Realizando verificacoes---------")
    verificacao(input1, input2, output)
    print("----------Verificacoes Finalizadas----------")
    lerCabecalho(input1)
    musicas, idxprimario = Ler_Arquivo(input1)
    vetorencontrado = busca2(musicas, idxprimario, input2, input1)
    imprimirarq(vetorencontrado, output)
    print("-------Finalizando Programa.As musicas encontradas estão no arquivo de saida-------\n")


# input1 = "input1.txt"
# input2 = "entrada02.txt"
# output = "saida2.txt"


input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

main(input1, input2, output)
