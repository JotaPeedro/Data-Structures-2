import time
import random
import sys

sys.setrecursionlimit(2000)  # Altera o limite de recursoes


################################## Bubble Sort ################################

def BubbleSort(vetor, compara):
    trocou = 1  # variavel para verificar se ocorreu a troca
    compara = compara+1
    aux = []  # vetor auxiliar
    tam = len(vetor)  # verifica o tamanho do vetor
    j = 0
    k = 0
    while trocou == 1:  # enquando houver trocas realiza as verificações
        compara = compara+1

        trocou = 0  # false para iniciar
        j = j+1

        i = 0  # variavel auxiliar para realizar as voltas
        while i != (tam-1):  # se o valor do vetor i for diferente do tamanho-1,realiza as verificações
            compara = compara+1

            k = k+1
            # print("Loop Interno",k)
            # caso o valor do vetor na posição i seja maior que na posição i+1 realiza a troca
            if vetor[i] > vetor[i+1]:
                compara = compara+1

                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux

                trocou = 1  # ocorreu uma troca então verdadeiro

            i = i+1  # somao contador para ir a proxima casa do vetor
    return compara

################################## Inserction Sort ################################


def InserctionSort(vetor, compara):
    aux = 0
    i = 1
    n = len(vetor)
    compara = compara+1
    while (i > 0) and (i <= n-1):
        compara = compara+1

        aux = vetor[i]
        j = i-1

        while (j >= 0) and vetor[j] > aux:
            compara = compara+1
            vetor[j+1] = vetor[j]
            j = j-1

        vetor[j+1] = aux
        i = i+1
    return (compara)

################################## Selection Sort ################################


def SelectionSort(vetor, compara):
    tam = len(vetor)
    for i in range(tam):
        compara = compara+1
        menor = i
        for j in range(i+1, tam):
            if vetor[menor] > vetor[j]:
                compara = compara+1
                menor = j
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    return compara


################################## Merge Sort ################################

def MergeSort(vetor, inicio=0, fim=None):

    if fim is None:
        fim = len(vetor)
    if (fim - inicio > 1):
        meio = (inicio+fim)//2
        MergeSort(vetor, inicio, meio)  # Separa
        MergeSort(vetor, meio, fim)  # Separa
        Merge(vetor, inicio, meio, fim)  # Junta
        compara = Merge(vetor, inicio, meio, fim)
        return (compara)


def Merge(vetor, inicio, meio, fim):
    esquerda = vetor[inicio:meio]
    direita = vetor[meio:fim]
    top_esq = 0
    top_dir = 0
    compara = 0
    for k in range(inicio, fim):
        compara = compara+1
        if top_esq >= len(esquerda):
            vetor[k] = direita[top_dir]
            top_dir = top_dir+1
            compara = compara+1
        elif top_dir >= len(direita):
            vetor[k] = esquerda[top_esq]
            top_esq = top_esq+1
            compara = compara+1
        elif esquerda[top_esq] < direita[top_dir]:
            vetor[k] = esquerda[top_esq]
            top_esq = top_esq+1
            compara = compara+1
        else:
            vetor[k] = direita[top_dir]
            top_dir = top_dir+1
            compara = compara+1
    return (compara)


################################## Quick Sort ################################


def Quicksort(vetor, inicio, fim, compara):
    compara = compara+1
    if (inicio < fim):

        pivo, compara = particiona(vetor, inicio, fim, compara)
        Quicksort(vetor, inicio, pivo-1, compara)
        Quicksort(vetor, pivo+1, fim, compara)
    return (compara)


def particiona(vetor, inicio, fim, compara):
    esq = inicio
    dir = fim
    pivo = vetor[inicio]
    compara = compara+1
    while (esq < dir):
        compara = compara+1
        while (vetor[esq] <= pivo and esq < fim):
            compara = compara+1
            esq = esq+1
        while (vetor[dir] > pivo and dir >= inicio):
            compara = compara+1
            dir = dir-1
        if (esq < dir):
            compara = compara+1
            vetor[esq], vetor[dir] = vetor[dir], vetor[esq]

    vetor[dir], vetor[inicio] = vetor[inicio], vetor[dir]
    return (dir, compara)

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
        max_heapfy(vetor, heapSize, maior)


def build_Max_Heap(vetor, heapSize):
    for i in range(int(len(vetor)/2), -1, -1):
        max_heapfy(vetor, heapSize, i)


def heapSort(vetor):
    heapSize = len(vetor)
    build_Max_Heap(vetor, heapSize)

    for i in range(len(vetor)-1, 0, -1):
        vetor[1], vetor[i] = vetor[i], vetor[1]
        heapSize = heapSize-1
        max_heapfy(vetor, heapSize, 1)


################ Verifica o arquivo texto ################

def verifica(texto):
    print(texto[1])
    if (texto[1] == 'c\n'):
        print("crescente")
        vetor = list(range(1, int(texto[0]) + 1))
        return vetor
    elif (texto[1] == 'd\n'):
        print("decrescente")
        vetor = list(range(int(texto[0]), 0, -1))
        return vetor
    elif (texto[1] == 'r\n'):
        print("random")
        random.seed()
        vetor = [random.randint(1, 32000) for i in range(int(texto[0]))]
        print(vetor)
        return vetor
    else:
        print("Modo de lista invalida")
        exit(1)


def main():

    entrada = open(sys.argv[1], "r")
    saida = open(sys.argv[2], "a")
    tamanho = int(entrada.readline().strip())
    ordenacao = entrada.readline().strip()

    # Gera o vetor com base no tamanho informado
    if ordenacao == 'c':
        vetor = list(range(1, tamanho+1))
    elif ordenacao == 'd':
        vetor = list(range(tamanho, 0, -1))
    else:
        import random
        vetor = [random.randint(1, tamanho) for _ in range(tamanho)]
    # Imprime o vetor desordenado
    print("Vetor desordenado:")
    print(vetor)

    # Armazena o tempo antes da ordenação com bubble sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando bubble sort
    BubbleSort(vetor, 0)
    compara = BubbleSort(vetor, 0)
    # Armazena o tempo depois da ordenação com bubble sort
    tempoFim = time.time()
    saida.write(
        f"\nBubbleSort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")

    # Armazena o tempo antes da ordenação com insertion sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando insertion sort
    InserctionSort(vetor, 0)
    # Armazena o tempo depois da ordenação com insertion sort
    tempoFim = time.time()
    compara = InserctionSort(vetor, 0)
    # Imprime o vetor ordenado com insertion sort
    saida.write(
        f"\nInsertionSort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")
    # Armazena o tempo antes da ordenação com selection sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando selection sort
    SelectionSort(vetor, 0)
    tempoFim = time.time()
    compara = SelectionSort(vetor, 0)
    # Imprime o vetor ordenado com selection sort
    saida.write(
        f"\nSelectionSort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")

    # Armazena o tempo antes da ordenação com merge sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando mergesort
    MergeSort(vetor)
    tempoFim = time.time()
    compara = MergeSort(vetor)
    # Imprime o vetor ordenado com merge sort
    saida.write(
        f"\nMergeSort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")

    # Armazena o tempo antes da ordenação com quick sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando quicksort
    tam = len(vetor)
    Quicksort(vetor, 0, (tam-1), 0)
    tempoFim = time.time()
    compara = Quicksort(vetor, 0, (tam-1), 0)
    # Imprime o vetor ordenado com Quick sort
    saida.write(
        f"\nQuicksort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")
    # Armazena o tempo antes da ordenação com heap sort
    tempoInicio = time.time()
    # Ordena o vetor utilizando heap sort
    tam = len(vetor)
    heapSort(vetor)
    tempoFim = time.time()
    # Imprime o vetor ordenado com heap sort
    saida.write(
        f"\nHeap Sort: {str(vetor)},{compara} comparacoes, {(tempoFim - tempoInicio):.10f} ms")


main()
