
import sys;


arq=open(sys.argv[1], 'r')
busca=sys.argv[2]

#Exercicio 1
def grep1(arq,busca):
    print("\nExercicio 1\n")
    #arq=open(arq, 'r')
    
    
    busca=str(busca)

    contl=0
    for linha in arq:
        linha2=linha.lower()#Deixa todos os caracteres da linha minuscula
        busca2=busca.lower()#Deixa todos os caracteres da busca minuscula
        #Verifica se a variavel busca está na linha
        if busca2 in linha2:
            print("A palavra",busca,"foi encontrada na linha",contl+1)
        
        contl=contl+1 #conta a linha 
        

#Exercicio 2

def grep2(arq,busca):
    print("\nExercicio 2\n")
    #arq=open(arq, 'r')
    arq=open(sys.argv[1], 'r')
    
    busca=str(busca)
    
    contl=0
    for linha in arq:
        
        linha2=linha.lower()#Deixa todos os caracteres da linha minuscula
        busca2=busca.lower()#Deixa todos os caracteres da busca minuscula
        #Verifica se a variavel busca está na linha
        if busca2 in linha2:
            
            print("A palavra",busca,"foi encontrada na linha",contl+1)
            print("Dados desta linha: ",linha)
        
        contl=contl+1 #conta a linha 
        

grep1(arq,busca)
grep2(arq,busca)
#grep2("data.txt","the")




