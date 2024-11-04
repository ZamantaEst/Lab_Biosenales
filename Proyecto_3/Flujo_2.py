import pywt ; from scipy import signal; import math

def Flujo2(senal):
  Fs=500
  orden_lp= 3.6/(50/Fs)
  orden_lp = math.floor(orden_lp) #Orden pasa bajas

  nyquist = Fs/2 # frecuencia de nyquist
  wn_lp = 50/nyquist #frecuencia de corte normalizada respecto nyquist para pasa bajas

  ## DETREND
  senal_filtrada_f2=signal.detrend(senal)

  ## APLICACION WAVELET MODIFICADO
  senal_filtrada_f2 = pywt.wavedec( senal_filtrada_f2, 'db3', level=7 )
  senal_filtrada_f2 = pywt.waverec(senal_filtrada_f2, 'db3') #Se reconstruye la señal con los coeficientes del wavelet

  ## PASA BAJAS
  lowpass_fir = signal.firwin(orden_lp+1,wn_lp, pass_zero = 'lowpass',window=('kaiser',6)) #filtro pasabajas
  senal_filtrada_f2 = signal.filtfilt(b=lowpass_fir,a=1,x=senal_filtrada_f2) # aplicación del filtro

  return senal_filtrada_f2
