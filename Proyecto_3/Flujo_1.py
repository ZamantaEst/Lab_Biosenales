import pywt ; from scipy import signal ; import math

def Flujo1(senal):
  Fs=500
  orden= 3.6/(50/Fs)
  orden = math.floor(orden) #Orden 

  nyquist = Fs/2 # frecuencia de nyquist
  wn_hp = 0.5/nyquist #frecuencia de corte normalizada respecto nyquist para pasa altas
  wn_lp = 50/nyquist #frecuencia de corte normalizada respecto nyquist para pasa bajas

  ## PASA ALTAS
  highpass_fir = signal.firwin(orden+1,wn_hp, pass_zero = 'highpass',window=('kaiser',6)) #filtro pasa altas
  senal_filtrada_f1 = signal.filtfilt(b=highpass_fir,a=1,x=senal) # aplicación del filtro

  ## APLICACION WAVELET MODIFICADO
  senal_filtrada_f1 = pywt.wavedec( senal_filtrada_f1, 'db3', level=7 )
  senal_filtrada_f1 = pywt.waverec(senal_filtrada_f1, 'db3') #Se reconstruye la señal con los coeficientes del wavelet

  ## PASABAJAS
  lowpass_fir = signal.firwin(orden+1,wn_lp, pass_zero = 'lowpass',window=('kaiser',6)) #filtro pasabajas
  senal_filtrada_f1 = signal.filtfilt(b=lowpass_fir,a=1,x=senal_filtrada_f1) # aplicación del filtro

  return senal_filtrada_f1