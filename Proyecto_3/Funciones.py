import numpy as np ; import matplotlib.pyplot as plt ; from scipy import signal
from random import randint ; import pandas as pd ; from scipy import signal,stats

def Str2Num_Vector(vector):
    vector_numeros = []
    for elemento in vector:
        vector_numeros.append(float(elemento))
    return vector_numeros

def Plot_Detalles(wavelet,name):
    fig, axes = plt.subplots(nrows=1, ncols=7, figsize=(22, 4))
    plt.suptitle("Detalles obtenidos por la wavelet "+name)
    axes[0].plot(wavelet[1])    ; axes[0].set_title('Detalle 1')
    axes[1].plot(wavelet[2])    ; axes[1].set_title('Detalle 2')
    axes[2].plot(wavelet[3])    ; axes[2].set_title('Detalle 3')
    axes[3].plot(wavelet[4])    ; axes[3].set_title('Detalle 4')
    axes[4].plot(wavelet[5])    ; axes[4].set_title('Detalle 5')
    axes[5].plot(wavelet[6])    ; axes[5].set_title('Detalle 6')
    axes[6].plot(wavelet[7])    ; axes[6].set_title('Detalle 7')
    plt.plot()


def diez_senales_aleatorias(signal):
    senal_aleatoria = []
    for i in range(10):
        senal_aleatoria.append(signal[randint(0,len(signal))])    
    return np.array(senal_aleatoria)

def Guardar_Senales_aleatorias( senales_afib,senales_sb):
    todas_senales = np.hstack((senales_afib.T, senales_sb.T))
    # Crear un DataFrame
    df = pd.DataFrame(todas_senales)
    # Agregar nombres de columnas
    columnas = [f"AFIB_{i+1}" for i in range(10)] + [f"SB_{i+1}" for i in range(10)]
    df.columns = columnas
    # Guardar en Excel
    df.to_excel('senales_aleatorias.xlsx', index=False)

  
def comprimir(senal):
    x_min = np.amin(senal)
    x_max = np.amax(senal)
    Datos_comprimir = (senal - x_min) / (x_max - x_min)
    return Datos_comprimir

def Detrend(senal):
  senal_detrend=signal.detrend(senal)
  return senal_detrend

def Frec_MaxPot(senal):
  Fs=500
  nperseg=1000
  noverlap = int(nperseg/2)
  f, Pxx_den = signal.welch(np.array(senal), Fs,'hann' ,nperseg, noverlap)
  indice_max = np.argmax(Pxx_den) # nos da el indice, Encontrar la frecuencia con la máxima potencia
  frecuencia_maxima = f[indice_max]
  return frecuencia_maxima

def Plot_Frec_MaxPot(senal,str):
  Fs=500
  nperseg=1000
  noverlap = int(nperseg/2)
  f, Pxx_den = signal.welch(np.array(senal), Fs,'hann' ,nperseg, noverlap)
  indice_max = np.argmax(Pxx_den) # nos da el indice, Encontrar la frecuencia con la máxima potencia
  frecuencia_maxima = f[indice_max]
  max_value = Pxx_den[indice_max]
  
  plt.scatter(frecuencia_maxima, max_value, color='red', marker='o', s=100)
  plt.text(frecuencia_maxima, max_value, f'Frec máxima potencia: {frecuencia_maxima:.2f}')
  plt.plot(f, Pxx_den)
  plt.title(str)

def plot_sencillo(senal,name):
    plt.figure(figsize=(13, 5))
    plt.plot(senal,label="Señal "+name)
    plt.title("Señal "+name)
    plt.legend()
    plt.show()

def evaluar_normalidad(vector,text):
  stat, p = stats.shapiro(vector)
  if p > 0.05:
    return f"Los datos {text} siguen  una distribución normal."
  else:
    return f"Los datos {text} NO siguen una distribución normal."
  
def graficas_normalidad(vector,name):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
    plt.suptitle("Comprobación normalidad " + name)
    axes[0].hist(vector, bins=20)           ; axes[0].set_title('Histograma')
    stats.probplot(vector, plot=axes[1])    ;   axes[1].set_title('Q-Q plot de fMP para AFIB')
    plt.show()
   


def prueba_saludar(nombre):
    print(f"Hola, {nombre}!")