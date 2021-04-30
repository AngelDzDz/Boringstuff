from random import *
    
def begin(palabra):
    size = len(palabra)
    index = randint(0,size-1)
    underscores = []
    for i in range(size):
        underscores.append('_')

    for i in range (size):
        if i == index:
            underscores[i] = palabra[index]

    for i in range(size):
        print(underscores[i], end = " ") 
   
    acabado = False
    while(acabado == False): 
        
        print("")
        print("Dema una letra para completar la palabra", end = " ")
        letra = input()

        for i in range(size):
            if(palabra[i] == letra):
                underscores[i] = palabra [i]
       
        if letra not in underscores:
            print("Esa letra no forma parte de la palabra")
        
        if '_' in underscores:
            acabado = False
        else:
            acabado = True

        for i in range(size):
            print(underscores[i], end = " ")

print("Palabra a adivinar: ")
palabra = input()
        
begin(palabra)



