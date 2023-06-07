# Cria classe para armazenar os herois
class Hero:
    # construtor do objeto Hero
    def __init__(self, chave=None, primeiroNome=None, sobrenome=None, nomeHeroi=None,
                 poder=None, fraqueza=None, cidade=None, profissao=None):
        self.chave = chave
        self.primeiroNome = primeiroNome
        self.sobrenome = sobrenome
        self.nomeHeroi = nomeHeroi
        self.poder = poder
        self.fraqueza = fraqueza
        self.cidade = cidade
        self.profissao = profissao

    def __str__(self):
        return f"{self.chave}, {self.primeiroNome}, {self.sobrenome}, {self.nomeHeroi}, {self.poder}, {self.fraqueza}, {self.cidade}, {self.profissao}"


# Define o tamanho dos parametros passado
TAM_chave = 3
TAM_primeiroNome = 15
TAM_sobrenome = 15
TAM_nomeHeroi = 15
TAM_poder = 15
TAM_fraqueza = 20
TAM_cidade = 20
TAM_profissao = 20

########## ler cabecalho #########


def lerCabecalho(input1):
    cabecalho = ""
    ler = open(input1, "r")
    cabecalho = ler.readline()
    size = cabecalho[5:8]
    top = cabecalho[13:15]
    qtde = cabecalho[21:23]
    sort = cabecalho[29]
    order = cabecalho[37:38]

    return size, top, qtde, sort, order

############ Ler os herois e gerar o vetor de chaves para ordenacao ############


def Ler_Arquivo(input1):
    heroes = []

    vetordechaves = []

    with open(input1, 'r') as arq:
        w = 0
        # Lendo cada linha do arquivo como um registro

        for linha in arq:
            # Extraindo os campos do registro com base nas posições das barras
            campos = linha.strip().split('|')
            chave = campos[0][:TAM_chave].strip() if len(campos) > 0 else ""
            primeiroNome = campos[1][:TAM_primeiroNome].strip() if len(
                campos) > 1 else ""
            sobrenome = campos[2][:TAM_sobrenome].strip() if len(
                campos) > 2 else ""
            nomeHeroi = campos[3][:TAM_nomeHeroi].strip() if len(
                campos) > 3 else ""
            poder = campos[4][:TAM_poder].strip() if len(campos) > 4 else ""
            fraqueza = campos[5][:TAM_fraqueza].strip() if len(
                campos) > 5 else ""
            cidade = campos[6][:TAM_cidade].strip() if len(campos) > 6 else ""
            profissao = campos[7][:TAM_profissao].strip() if len(
                campos) > 7 else ""

            # Criando um objeto game com os campos extraídos
            if (w > 0):
                hero = Hero(chave, primeiroNome, sobrenome,
                            nomeHeroi, poder, fraqueza, cidade, profissao)
                heroes.append(hero)
            w = w+1

        for hero in heroes:
            vetordechaves.append(hero.chave)

    return vetordechaves, heroes

############### Funcoes de Ordenacao ###############


################################## Quick Sort ################################
def Quicksort(vetor, inicio, fim):

    if (inicio < fim):

        pivo = particiona(vetor, inicio, fim)
        Quicksort(vetor, inicio, pivo-1)
        Quicksort(vetor, pivo+1, fim)
    return vetor


def particiona(vetor, inicio, fim):
    esq = inicio
    dir = fim
    pivo = vetor[inicio]

    while (esq < dir):

        while (vetor[esq] <= pivo and esq < fim):

            esq = esq+1
        while (vetor[dir] > pivo and dir >= inicio):

            dir = dir-1
        if (esq < dir):

            vetor[esq], vetor[dir] = vetor[dir], vetor[esq]

    vetor[dir], vetor[inicio] = vetor[inicio], vetor[dir]
    return (dir)

################################## Quick Sort ################################


def InserctionSort(vetordechaves):
    vetor = vetordechaves
    aux = 0
    i = 1
    n = len(vetor)
    while (i > 0) and (i <= n-1):
        aux = vetor[i]
        j = i-1
        while (j >= 0) and vetor[j] > aux:

            vetor[j+1] = vetor[j]
            j = j-1
        vetor[j+1] = aux
        i = i+1
    return vetor


def MergeSort(vetor, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio = (inicio+fim)//2
        MergeSort(vetor, inicio, meio)  # Separa
        MergeSort(vetor, meio, fim)  # Separa
        Merge(vetor, inicio, meio, fim)  # Junta
    return vetor


def Merge(vetor, inicio, meio, fim):
    esquerda = vetor[inicio:meio]
    direita = vetor[meio:fim]
    top_esq = 0
    top_dir = 0

    for k in range(inicio, fim):

        if top_esq >= len(esquerda):
            vetor[k] = direita[top_dir]
            top_dir = top_dir+1

        elif top_dir >= len(direita):
            vetor[k] = esquerda[top_esq]
            top_esq = top_esq+1

        elif esquerda[top_esq] < direita[top_dir]:
            vetor[k] = esquerda[top_esq]
            top_esq = top_esq+1

        else:
            vetor[k] = direita[top_dir]
            top_dir = top_dir+1

############################ Heap Sort #####################


def max_heapfy(vetor, heapSize, i):

    left = 2*i+1
    right = 2*i+2
    maior = i

    if left <= (heapSize-1) and vetor[left] > vetor[i]:
        maior = left
    if right <= (heapSize-1) and vetor[right] > vetor[maior]:
        maior = right

    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        max_heapfy(vetor, heapSize-1, maior)


def build_Max_Heap(vetor, heapSize):
    for i in range(int(len(vetor)/2), -1, -1):
        max_heapfy(vetor, heapSize, i)


def heapSort(vetor):
    heapSize = len(vetor)
    build_Max_Heap(vetor, heapSize)

    for i in range(len(vetor)-1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        heapSize = heapSize-1
        max_heapfy(vetor, heapSize, 0)
    return vetor
########################### Heap Sort ###########

################ Ordenar o vetor de herois com base na chave ordenada pelas funcoes de ordenacao ###############


def AlinhaChave(vetorordenado, herois):
    vetor = vetorordenado
    vetorfinal = []
    h = 0
    o = 0

    while h < len(vetorordenado):

        for hero in herois:

            aa = str(hero)
            bb = aa[0:2]
            if bb == vetor[h]:
                vetorfinal.append(hero)
        h = h+1

    while o < len(vetorfinal):
        print(vetorfinal[o])
        o = o+1
    return vetorfinal

##### Inverte a ordem do vetor de herois se necessário ###########


def inverteOrdem(vetor):
    vetor.reverse()
    i = 0
    while i < len(vetor):
        print(vetor[i])
        i = i+1


def main(entrada, saida):
    size, top, qtde, sort, order = lerCabecalho(entrada)
    print(size, "\n", top, "\n", qtde, "\n", sort, "\n", order)
    vetor, herois = Ler_Arquivo(entrada)

    if sort == "Q":
        print("Quick Sort")
        chaveordenada = Quicksort(vetor, 0, len(vetor)-1)

    elif sort == "M":
        print("Merge Sort")
        chaveordenada = MergeSort(vetor)

    elif sort == "H":
        print("Heap Sort")
        chaveordenada = heapSort(vetor)

    elif sort == "I":
        print("Inserction Sort")
        chaveordenada = InserctionSort(vetor)
    else:
        print("Erro,Arquivo invalido")
        return 0

    vetoralinhado = AlinhaChave(chaveordenada, herois)

    if order == "D":
        print("\nInvertendo\n")
        inverteOrdem(vetoralinhado)


main("input5.txt", "saida.txt")
