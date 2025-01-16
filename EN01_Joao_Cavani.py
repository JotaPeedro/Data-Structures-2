# --------------------------------
# --------------------------------
import sys


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
TAM_nome = 50
TAM_PRODUTORA = 40
TAM_GENERO = 25
TAM_PLATAFORMA = 15
TAM_ANO = 4
TAM_CLASSIFICACAO = 12
TAM_PRECO = 7
TAM_MIDIA = 8
TAM_TAMANHO = 7


def Tamanho_fixo():
    print("Lendo registros")
    # Abrindo o arquivo de jogos para leitura
    games = []
    with open(sys.argv[1], 'r') as arq:
        # Lendo cada linha do arquivo como um registro
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

        for game in games:
            print(game)


''''            
    saida = open('games_indicador.txt', "w")
  

    for game in games:
       
        
        k = 0
        g = game
        titulo = g.nome
        produtora = g.produtora
        genero = g.genero
        plataforma = g.plataforma
        ano = g.ano
        classificacao = g.classificacao
        preco = g.preco
        midia = g.midia
        tamanho = g.tamanho
        tam = len(str(game))
        linha=str(game)
        
        print(linha[k])
        print(linha[tam-1])

        for linha in linha:
            l = 0
            j=0
            i = 0
            while linha[i] != ',':

                j = j+1
                i = i+1
            saida.write(str(j))
            if l == 0:
                saida.write(str(titulo))

            if l == 1:
                saida.write(str(produtora))

            if l == 0:
                saida.write(str(genero))

            if l == 1:
                saida.write(str(plataforma))

            if l == 0:
                saida.write(str(ano))

            if l == 1:
                saida.write(str(classificacao))

            if l == 0:
                saida.write(str(preco))

            if l == 1:
                saida.write(str(midia))

            if l == 1:
                saida.write(str(tamanho))
            
            l = l+1
            k = k+1

        saida.write("\n")
        

        j = 0
'''

Tamanho_fixo()
