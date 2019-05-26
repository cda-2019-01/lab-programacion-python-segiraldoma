##
## Imprima la cantidad de registros por letra para la
## primera columna, ordenados alfabeticamente.
x = open('data.csv','r').readlines() #Se lee el archivo
x = [z.replace('\n', '') for z in x]
x = [z.split('\t') for z in x]
b = [(z[0]) for z in x[0:]]
e=[int(z[1]) for z in x[0:]]
c = set(b)
d = list(c)
d.sort()
lenb = len(b)
lend = len(d)
for i in range(0,lend):
    n=0
    for j in range(0,lenb):
        if b[j] == d[i]:
            n = n + e[j]
    print(d[i], end="")
    print(',', end="")
    print(n)
## A,37
## B,36
## C,27
## D,23
## E,67
##
