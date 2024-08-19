# P1_Python_LiliamEstupinan
import numpy as np
import matplotlib.pyplot as mp

# a)Crear los vectores
a=np.array([3.1,1,0.5,-3.2,6])
b=np.array([1,3,2.2,5.1,1])

# b)Multiplicación escalar
ProdEscalar=a*b
# c)Multiplicación punto a punto
ProdPunto=np.dot(a,b)

# d)Matriz A
A=np.array([[2,-1,-3],[4,1.5,-2.5],[7.3,-0.9,0.2]])
# e)Transpuesta Matriz A
AT=np.transpose(A)
#print(AT)

# f)
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

# g)Valor primera fila, tercera columna de la matriz A
Valor=A[0,2]
print(Valor)

# h)Segunda fila 
Valor2=A[1,:]
print(Valor2)

# i) dimensiones matriz
dim= A.shape
print(dim)

# j) Función  y[n]=sin⁡(π*0.12n) en el intervalo 0 <= n <= 100.
n=np.arange(0,101) # arange me permite crear un array de numpy espaciado de forma uniforme
y= np.sin(np.pi*0.12*n)

# k) senoidal y2[n]=cos⁡(2π*0.03n)
y2=np.cos(2*np.pi*0.03*n)

#l)	tercera señal que sea s[n]=y[n]+y2[n] y una cuarta, que sea t[n]=y[n].y2[n].
s=y+y2
t=y*y2

# m) Graficar en la misma figura las señales y[n] y y2[n]
mp.figure(1)
mp.plot(n, y, label='y[n] = sin(π * 0.12 * n)', color='blue')
mp.plot(n, y2, label='y2[n] = cos(2π * 0.03 * n)', color='green')
mp.title('Señales y[n] y y2[n]')
mp.xlabel('n')
mp.ylabel('Señal')
mp.legend()
mp.grid(True)

# n) Graficar en la misma figura las señales s[n] y t[n]
mp.figure(2)
mp.plot(n, s, label='s[n]=y[n]+y2[n]', color='pink')
mp.plot(n, t, label='t[n]=y[n].y2[n]', color='purple')
mp.title('Señales s[n] y t[n]')
mp.xlabel('n')
mp.ylabel('Señal')
mp.legend()
mp.grid(True)
mp.show()