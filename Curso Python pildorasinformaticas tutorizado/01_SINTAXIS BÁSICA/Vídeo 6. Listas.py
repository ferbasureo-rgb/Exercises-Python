"""Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

x = 3
y = 7

lista_final = []
for i in range(x): #0,1,2
    L=[]
    lista_final.append(L) #Hemos añadido 1 lista vacía.
    for j in range(y): #0,1,2,3,4 Tenemos [[0] ]
        L.append(j*i)

#List comprehension
lista_final2= [[j*i for j in range(y)] for i in range(x)]

print(lista_final)
print(lista_final2)