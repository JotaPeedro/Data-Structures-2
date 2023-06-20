import sys

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


# Define o tamanho dos parametros passado
TAM_ano = 5
TAM_duracao = 6
TAM_titulo = 28
TAM_artista = 25
TAM_genero = 15
TAM_idioma = 10


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

    with open(input1, 'r') as arq:
        w = 0
        # Lendo cada linha do arquivo como um registro

        for linha in arq:
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split('|')
            ano = campos[0][:TAM_ano].strip() if len(campos) > 0 else ""
            duracao = campos[1][:TAM_ano].strip() if len(
                campos) > 1 else ""
            titulo = campos[2][:TAM_titulo].strip() if len(
                campos) > 2 else ""
            artista = campos[3][:TAM_artista].strip() if len(
                campos) > 3 else ""
            genero = campos[4][:TAM_genero].strip() if len(campos) > 4 else ""
            idioma = campos[5][:TAM_idioma].strip() if len(
                campos) > 5 else ""

            # Criando um objeto game com os campos extraídos
            if (w > 0):
                music = Music(ano, duracao,
                              titulo, artista, genero, idioma)
                musics.append(music)
            w = w+1

    return musics


def busca(musics, input2):
    retorno = []
    input2 = open(input2, "r")
    busca = ""
    tipobusca = ""

    tipobusca = input2.readline()
    busca = input2.readline()

    print(tipobusca)
    print(busca)

    if tipobusca == "ano\n":
        for music in musics:
            if int(music.ano) == int(busca):
                print(music)

                inser = "\n"+str(music.ano)+"|"+str(music.duracao)+"|"+str(music.titulo)+"|"+str(music.artista)+"|"+str(
                        music.genero)+"|"+str(music.idioma)
                retorno.append(inser)
    if tipobusca == "titulo\n":
        for music in musics:
            if str(music.titulo.lower()+"\n") == busca.lower():
                print(music)

                inser = "\n"+str(music.ano)+"|"+str(music.duracao)+"|"+str(music.titulo)+"|"+str(music.artista)+"|"+str(
                        music.genero)+"|"+str(music.idioma)
                retorno.append(inser)
    if tipobusca == "artista\n":
        for music in musics:
            if str(music.artista.lower()+"\n") == busca.lower():
                print(music)

                inser = "\n"+str(music.ano)+"|"+str(music.duracao)+"|"+str(music.titulo)+"|"+str(music.artista)+"|"+str(
                        music.genero)+"|"+str(music.idioma)
                retorno.append(inser)

    if tipobusca == "genero\n":
        for music in musics:
            if str(music.genero.lower()+"\n") == busca.lower():
                print(music)

                inser = "\n"+str(music.ano)+"|"+str(music.duracao)+"|"+str(music.titulo)+"|"+str(music.artista)+"|"+str(
                        music.genero)+"|"+str(music.idioma)
                retorno.append(inser)
    if tipobusca == "idioma\n":

        for music in musics:

            if (str(music.idioma).lower()+"\n") == busca.lower():
                print(music)

                inser = "\n"+str(music.ano)+"|"+str(music.duracao)+"|"+str(music.titulo)+"|"+str(music.artista)+"|"+str(
                        music.genero)+"|"+str(music.idioma)
                retorno.append(inser)

    return (retorno)


def imprimirarq(vetorencontrado, input3):
    input3 = open(input3, "a")
    i = 0

    while i < len(vetorencontrado):
        input3.writelines(vetorencontrado[i])
        i = i+1


def main(input1, input2, input3):
    lerCabecalho(input1)
    musicas = Ler_Arquivo(input1)
    vetorencontrado = busca(musicas, input2)
    imprimirarq(vetorencontrado, input3)


input1 = "input1.txt"
input2 = "entrada06.txt"
input3 = "saida6.txt"

main(input1, input2, input3)
