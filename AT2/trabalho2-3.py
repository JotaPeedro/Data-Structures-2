
# Ler o arquivo de entrada
# Verificar cabeçalho
# Criar chave para cada jogo e armazenar
#
# Ler o arquivo de operações
# Ler a primeira letra de cada linha para verificar se é insercao ou remocao
# Gerar chave do jogo e verificar se já existe na pilha
# Se o jogo já existir não inserir
# Se o jogo não exisitir e não tiver espaço inserir jogo no final
# Se o jogo não existir e tiver algum jogo já removido verificar no cabeçalho qual a posição para sobrescrever


from ast import Delete
from dataclasses import replace
import string
from traceback import print_tb


class Game:
    # construtor do objeto Game
    def __init__(self, nome=None, produtora=None, genero=None, plataforma=None,
                 ano=None, classificacao=None, preco=None, midia=None,
                 tamanho=None):
        self.nome = nome
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome}, {self.produtora}, {self.genero}, {self.plataforma}, {self.ano}, {self.classificacao}, {self.preco}, {self.midia}, {self.tamanho}"


# --------------------------------
# --------------------------------
TAM_op = 1
TAM_nome = 50
TAM_PRODUTORA = 40
TAM_GENERO = 25
TAM_PLATAFORMA = 15
TAM_ANO = 4
TAM_CLASSIFICACAO = 12
TAM_PRECO = 7
TAM_MIDIA = 8
TAM_TAMANHO = 7

# Ler o arquivo e adiciona cada jogo em um objeto


def Ler_Arquivo(input1):

    # Abrindo o arquivo de jogos para leitura
    games = []

    i = 0
    vetor = [()]
    with open(input1, 'r') as arq:
        # Lendo cada linha do arquivo como um registro

        cabecalho = arq.readline()

        for linha in arq:
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split('|')
            nome = campos[0][:TAM_nome].strip() if len(campos) > 0 else ""
            produtora = campos[1][:TAM_PRODUTORA].strip() if len(
                campos) > 1 else ""
            genero = campos[2][:TAM_GENERO].strip() if len(campos) > 2 else ""
            plataforma = campos[3][:TAM_PLATAFORMA].strip() if len(
                campos) > 3 else ""
            ano = campos[4][:TAM_ANO].strip() if len(campos) > 4 else ""
            classificacao = campos[5][:TAM_CLASSIFICACAO].strip() if len(
                campos) > 5 else ""
            preco = campos[6][:TAM_PRECO].strip() if len(campos) > 6 else ""
            midia = campos[7][:TAM_MIDIA].strip() if len(campos) > 7 else ""
            tamanho = campos[8][:TAM_TAMANHO].strip() if len(
                campos) > 8 else ""

            # Criando um objeto game com os campos extraídos
            game = Game(nome, produtora, genero, plataforma, ano,
                        classificacao, preco, midia, tamanho)
            games.append(game)

            # print(cabecalho[6:8])

        # Cria a chave para cada jogo
        for game in games:
            i = 2
            chave = str(game.nome+game.ano)
            chave = chave.replace(" ", "")
            chave = chave.upper()
            vetor.append(chave)  # Armazena a chave no vetor

            # print(chave)
            # print(game)
            i = i+1

     #   print(vetor[4])#Pega a chave do vetor na posicao 4
      #  print(games[3])#Pega o jogo na posicao da chave -1,por conta do cabecalho

    # Ler arquivo de operacaos
    return vetor


cabecalho = ""
ler = open("input2.txt", "r")
cabecalho = ler.readline()
reg = cabecalho[13:15]
print(cabecalho)
print(cabecalho[13:15])


def Ler_Op(op1, temp):
    temp = open(temp, "a")
    j = 0
    vetor3 = []

    saida = open("input2.txt", "r+")
    t = ""
    var = 0

    for linha in saida:

        vetor3.append(linha)

    with open(op1, 'r') as arq:
        # Lendo cada linha do arquivo como um registro
        games2 = []

        for linha in arq:
            vetor = Ler_Arquivo("input2.txt")
            existe = 0
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split(',')
            op = campos[0][:TAM_op].strip() if len(campos) > 0 else ""

            print(op)
            if op == "d":
                l = 0
                campos = linha.strip().split(',')
                op = campos[0].strip()
                chavedelete = campos[1].strip()
                print(chavedelete)

                for vetor in vetor:
                    l = l+1

                    if chavedelete in vetor:

                        t, var, cab = remover(l, "input2.txt", j, vetor3)
                        temp = open("temp.txt", "w")
                        temp.writelines(cab)
                        j = j+1
                        vetor3[0] = cab
                        vetor3[var-1] = t

            if op == "i":
                nome = campos[1][:TAM_nome].strip() if len(campos) > 1 else ""
                produtora = campos[2][:TAM_PRODUTORA].strip() if len(
                    campos) > 2 else ""
                genero = campos[3][:TAM_GENERO].strip() if len(
                    campos) > 3 else ""
                plataforma = campos[4][:TAM_PLATAFORMA].strip() if len(
                    campos) > 4 else ""
                ano = campos[5][:TAM_ANO].strip() if len(campos) > 5 else ""
                classificacao = campos[6][:TAM_CLASSIFICACAO].strip() if len(
                    campos) > 6 else ""
                preco = campos[7][:TAM_PRECO].strip() if len(
                    campos) > 7 else ""
                midia = campos[8][:TAM_MIDIA].strip() if len(
                    campos) > 8 else ""
                tamanho = campos[9][:TAM_TAMANHO].strip() if len(
                    campos) > 9 else ""
              # Criando um objeto game com os campos extraídos
                game2 = Game(nome, produtora, genero, plataforma, ano,
                             classificacao, preco, midia, tamanho)
                games2.append(game2)

                chaveinserir = str(game2.nome+game2.ano)
                chaveinserir = chaveinserir.replace(" ", "")
                chaveinserir = chaveinserir.upper()

                for vetor in vetor:

                    if chaveinserir in vetor:
                        existe = 1
                        print("Chave ja existe")

                if existe == 0:
                    inser = "\n"+str(game2.nome)+"|"+str(game2.produtora)+"|"+str(game2.genero)+"|"+str(game2.plataforma)+"|"+str(
                        game2.ano)+"|"+str(game2.classificacao)+"|"+str(game2.preco)+"|"+str(game2.midia)+"|"+str(game2.tamanho)
                    
                    ler = open("input2.txt", "r")
                    cabecalho = ler.readline()
                    regcabe = cabecalho[13:15]
                    print("insere reg", regcabe)
                    if "-1" in regcabe:
                        
                        vetor3.append(inser)
                    else:
                        inser2 = str(game2.nome)+"|"+str(game2.produtora)+"|"+str(game2.genero)+"|"+str(game2.plataforma)+"|"+str(
                        game2.ano)+"|"+str(game2.classificacao)+"|"+str(game2.preco)+"|"+str(game2.midia)+"|"+str(game2.tamanho)
                        indice=int(regcabe)
                        print("indice",indice)
                        vetor3[indice-1]=inser2

    print("\n Final \n:", vetor3)
    temp = open("temp.txt", "w")
    w = 0
    while w < len(vetor3):

        temp.writelines(vetor3[w])
        w = w+1

    return vetor3


def criaFinal(arqFinal):
    w = 0
    vetor1 = Ler_Op("op2.txt", "temp.txt")

    temp = open(arqFinal, "w")
    while w < len(vetor1):
        if "*" in vetor1[w]:
            del vetor1[w]

        w = w+1
    w = 0
    while w < len(vetor1):

        temp.writelines(vetor1[w])
        w = w+1


def inserir(game2, temp):
    print("Inserindo no arquivo")
    temp.write(f"{str(game2)}\n")


def remover(chave, temp, j, vetor):

    m = 0
    saida = open(temp, "r+")
    linha = []
    delete = [-1]
    vetora = []
    vetora = vetor

   # print(vetor)

    while m != chave:
        frase = saida.readline()
        linha.append(frase)
        m = m+1

    if j == 0:
        inicio = frase[0:3]
        sub = "*-1|"
        newreg = j
        frasenova = frase.replace(inicio, sub, 1)
    if "-1" in cabecalho[13:15]:
        inicio = frase[0:3]

        newreg = m
        sub = "*"+str(newreg)+"|"
        frasenova = frase.replace(inicio, sub, 1)
    else:
        delete.append(m-3)
        inicio = frase[0:3]
        sub = sub = "*"+str(newreg)+"|"
        frasenova = frase.replace(inicio, sub, 1)
        newreg = m

    cabecalhono = cabecalho.replace(reg, str(newreg))
    frase = frasenova

    att = open("input2.txt", "w")
    att.writelines(cabecalhono)
    att.writelines(vetora)

   

    return frasenova, m, cabecalhono


def verificacao(input, op):

    with open(input, 'r') as arq:
        for linha in arq:
            if "@""$""%""&""!" in linha:
                print("Arquivo input invalido")
                exit()
            else:
                with open(op, 'r') as arq2:
                    for linha in arq2:
                        if "@""$""%""&""!" in linha:
                            print("Arquivo operacoes invalido")
                            exit()
                        else:
                            print("Arquivos corretos")

    arq.close()
    arq2.close()


# verificacao("input2.txt", "op2.txt")
# Ler_Arquivo("input2.txt")


criaFinal("FINAL.txt")
