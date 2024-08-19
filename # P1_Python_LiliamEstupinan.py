# P1_Python_LiliamEstupinan
import numpy as np
import matplotlib as mp

a=np.array([3.1,1,0.5,-3.2,6])
b=np.array([1,3,2.2,5.1,1])

ProdEscalar=a*b
ProdPunto=np.dot(a,b)

A=np.array([[2,-1,-3],[4,1.5,-2.5],[7.3,-0.9,0.2]])
AT=np.transpose(A)
#print(AT)

#Funcion Ones-->Devuelve un array del tamaño y tipo indicados inicializando sus valores con unos
c=np.ones(3)
d=np.ones([2,6]) # tamaño matriz 
#print(c)
#print(d)

# Funcion Round-->Toma los elementos de un arreglo que estan en decimal y los redondea al entero mas cercano o al decimal que se le diga
e=np.array([2.333, 7.159, 4.856, 9.561, 4.489])
f=np.round(e)
g=np.round(e, decimals=1)# redondea a la cantidad de decimales "1"
#print(f)
#print(g)

#Funcion ceil-->Redondea cada elemento del arreglo al numero entero mas cercano pero hacia arriba
h=np.ceil(e)
#print(h)

#Funcion floor-->Redondea cada elemento del arreglo al numero entero mas cercano pero hacia abajo
i=np.floor(e)
#print(i)