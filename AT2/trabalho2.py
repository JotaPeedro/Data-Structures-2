
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


def Ler_Arquivo(arquivo1):

    print("Lendo registros")
    # Abrindo o arquivo de jogos para leitura
    games = []

    i = 0
    vetor = [()]
    with open(arquivo1, 'r') as arq:
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

      #  print(cabecalho)

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


def Ler_Op(arquivo2, arquivo3):
    arquivo3 = open(arquivo3, "a")
    j=0
    with open(arquivo2, 'r') as arq:
        # Lendo cada linha do arquivo como um registro
        games2 = []

        for linha in arq:
            vetor = Ler_Arquivo("arquivo1.txt")
            existe = 0
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split(',')
            op = campos[0][:TAM_op].strip() if len(campos) > 0 else ""

            print(op)

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
                    print("Inserindo no arquivo")
                    arquivo3.write(f"{str(game2)}\n")
            if op == "d":
                l = 0
                campos = linha.strip().split(',')
                op = campos[0].strip()
                chavedelete = campos[1].strip()
                print(chavedelete)

                for vetor in vetor:
                    l = l+1
                    
                    if chavedelete in vetor:
                        
                        remover(l, "arquivo1.txt",j)
                        j=j+1


def remover(chave, arquivo3,j):
    
    
    m=0
    arquivo3 = open(arquivo3, "r+")
    linha=[]
    delete=[-1]
    
    while m != chave:
        frase=arquivo3.readline()
        linha.append(frase)
        m = m+1
    delete.append(m-4)
    inicio=frase[0:3]
    sub="*"+str(delete[j-1])+"|"

    print(delete)
    frasenova=frase.replace(inicio,sub,1)
    print(frasenova)
    
    frase=frasenova
    
    arquivo3.writelines(frasenova)
    
# Ler_Arquivo("arquivo1.txt")
Ler_Op("op1.txt", "saida.txt")
