#vetor=[29,13 ,-44,20,35,-33,46,-8,15,-30,-29,-16,-35,12,-7]

vetor=[23,4,67,-8,90,54,21]
aux=0
i=1
n=len(vetor)


while (i>0) and (i<=n-1):
    print(iteração externa)
    aux=vetor[i]
    j=i-1
   
    while(j>=0) and vetor[j]>aux:
        print("itera interna")
        vetor[j+1]=vetor[j]
        j=j-1
        print(vetor)
    vetor[j+1]=aux
    i=i+1
print(vetor)
