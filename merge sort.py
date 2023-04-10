
def MergeSort(vetor, inicio, fim):
    if (inicio < fim):
        meio = ((inicio+fim)/2)
        MergeSort(vetor, inicio, meio)
        MergeSort(vetor, meio+1, fim)
        Merge(vetor, inicio, meio, fim)


def Merge(vetor, inicio, meio, fim):
    i = 0
    aux = []
    p1 = inicio
    p2 = meio+1

    while (p1 <= meio and p2 <= fim):
        if (vetor[p1] > vetor[p2]):
            aux[i] = vetor[p2]
        else:
            aux[i] = vetor[p1]
    if (p1 == meio):
