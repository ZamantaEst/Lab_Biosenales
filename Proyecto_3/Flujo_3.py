from scipy import signal ; import math
def Flujo3(senal):
  Fs=500
  orden= 3.6/(50/Fs)
  orden = math.floor(orden) #Orden

  nyquist = Fs/2 # frecuencia de nyquist
  wn_hp = 0.5/nyquist #frecuencia de corte normalizada respecto nyquist para pasa bajas
  wn_lp = 50/nyquist #frecuencia de corte normalizada respecto nyquist para pasa bajas

  ## PASA ALTAS
  highpass_fir = signal.firwin(orden+1,wn_hp, pass_zero = 'highpass',window=('kaiser',6)) #filtro pasa altas
  senal_filtrada_f3 = signal.filtfilt(b=highpass_fir,a=1,x=senal) # aplicación del filtro

  ## PASA BAJAS
  lowpass_fir = signal.firwin(orden+1,wn_lp, pass_zero = 'lowpass',window=('kaiser',6)) #filtro pasabajas
  senal_filtrada_f3 = signal.filtfilt(b=lowpass_fir,a=1,x=senal_filtrada_f3) # aplicación del filtro

  return senal_filtrada_f3  