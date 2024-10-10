
import numpy as np
import matplotlib.pyplot as plt

# Nombre del archivo
archivo1 = "datossenales\datos_ECG1.csv"
archivo2 = "datossenales\datos_EMG.csv"
# Leer los datos
datos1 = np.loadtxt(archivo1, delimiter=',')
datos2 = np.loadtxt(archivo2, delimiter=',')

# Frecuencia de muestreo y tiempo
frec_muestreo = 1000

tiempo1 = len(datos1) / frec_muestreo  
tiempo2 = len(datos2) / frec_muestreo


t1= np.linspace(0, tiempo1, len(datos1))  
t2 = np.linspace(0, tiempo2, len(datos2))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7))


ax1.plot(t1[0:300], datos1[0:300],color='k')
ax2.plot(t2[0:600], datos2[0:600])
ax1.set_title('ECG')
ax2.set_title('EMG')
ax1.grid(True)
ax2.grid(True)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.plot()
plt.savefig('graficasEMG_ECG.png')
plt.show()
