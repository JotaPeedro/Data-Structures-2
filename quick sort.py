import random

# Funcao quicksort


def Quicksort(vetor, inicio, fim, choice):

    if (inicio < fim):
        pivo = particiona(vetor, inicio, fim, choice)
        Quicksort(vetor, inicio, pivo-1, choice)
        Quicksort(vetor, pivo+1, fim, choice)

# Funcao auxiliar realiza a separação do vetor


def particiona(vetor, inicio, fim, choice):
    troca = 0
    esq = inicio
    dir = fim
    # Verifica a escolha do pivo
    if (choice == "first"):
        pivo = vetor[inicio]
    if (choice == "last"):
        pivo = vetor[fim]
    if (choice == "random"):
        aleatorio = random.randrange(inicio, fim)
        pivo = vetor[aleatorio]

    while (esq < dir):

        while (vetor[esq] <= pivo and esq < fim):
            esq = esq+1
        while (vetor[dir] > pivo and dir >= inicio):

            dir = dir-1
        if (esq < dir):
            vetor[esq], vetor[dir] = vetor[dir], vetor[esq]
            troca = troca = +1

    vetor[dir], vetor[inicio] = vetor[inicio], vetor[dir]
    troca = troca = +1
    return (dir)


vetor = [29, 13, -44, 20, 35, -33, 46, -8,
         15, -30, -29, -16, -35, 12, -7]  # vetor
tam = len(vetor)
Quicksort(vetor, 0, (tam-1), "first")
print(vetor)
