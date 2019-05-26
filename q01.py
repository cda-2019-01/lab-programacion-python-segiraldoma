## Imprima la suma de la segunda columna.
x = open('data.csv','r').readlines() #Se lee el archivo
x = [z.replace('\n', '') for z in x] #Quitamos retorno de carro
x = [z.split('\t') for z in x] #Quitamos espacios 
a=sum([int(z[1]) for z in x[0:]]) #Hacemos la operacion suma de los valores que estan en la posicion 2 
print(a) #Imprimimos resultado
