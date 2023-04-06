def Quicksort(vetor,inicio,fim):
    
    if(inicio<fim):
        pivo=particiona(vetor,inicio,fim)
        Quicksort(vetor,inicio,pivo-1)
        Quicksort(vetor,pivo+1,fim)
        
def particiona(vetor,inicio,fim):
    esq=inicio
    dir=fim
    pivo=vetor[inicio]
    
    while(esq<dir):
        
        while(vetor[esq]<=pivo and esq<fim):
      
            esq=esq+1
        while(vetor[dir]>pivo and dir>=inicio):
           
            dir=dir-1
        if (esq<dir):
            vetor[esq],vetor[dir] = vetor[dir],vetor[esq]
    
    vetor[dir],vetor[inicio] = vetor[inicio],vetor[dir]
    return(dir)




vetor=[29,13,-44,20,35,-33,46,-8,15,-30,-29,-16,-35,12,-7] #vetor
#vetor=[7,9,3,1]

Quicksort(vetor,0,14)
print(vetor)

