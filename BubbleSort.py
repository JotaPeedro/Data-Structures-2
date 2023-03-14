
vetor=[29,13 ,-44,20,35,-33,46,-8,15,-30,-29,-16,-35,12,-7] #vetor
trocou = 1 #variavel para verificar se ocorreu a troca

aux=[] #vetor auxiliar
print(vetor)#printa o primeiro vetor
tam=len(vetor)#verifica o tamanho do vetor
j=0
k=0
while trocou==1:#enquando houver trocas realiza as verificações
    trocou=0 #false para iniciar
    j=j+1
    print("Loop Externo",j)
    
    i=0 #variavel auxiliar para realizar as voltas
    while i != (tam-1): #se o valor do vetor i for diferente do tamanho-1,realiza as verificações
        k=k+1
        #print("Loop Interno",k)
        if vetor[i]> vetor[i+1]: #caso o valor do vetor na posição i seja maior que na posição i+1 realiza a troca
            aux=vetor[i]
            vetor[i]=vetor[i+1]
            vetor[i+1]=aux
            print(vetor)
            trocou =1 #ocorreu uma troca então verdadeiro
            
        i=i+1#somao contador para ir a proxima casa do vetor