import numpy as np
import scipy.signal as ss
import scipy.fft as fft
from backend.FAA import FAA
from backend.LLA import LLA
from backend.SyH import SyH
from backend.FR import FR

def Recieve(signal_type, amplitud, frec, theta, periodo, DC, FAA_ON, SyH_ON, LLA_ON, FR_ON, n_periodos):
    largo_tiempo = 12000
    # que sea multiplo de 3 por el seno
    x_tiempo=np.linspace(0, n_periodos/frec, largo_tiempo)

    if signal_type == "Coseno":
        signal = amplitud * np.cos(2*np.pi * frec * x_tiempo + (theta*(np.pi/180)))
    elif signal_type == "Seno (T*3/2)":
        x_aux=np.linspace(0, (3/2)*(1/frec), largo_tiempo//int(n_periodos))
        sin_aux= amplitud * np.sin(2*np.pi * frec * x_aux)
        div=int(theta * (len(x_aux)/360))
        signal=np.append(sin_aux, sin_aux)
        if n_periodos > 2:
            for n in range(int(n_periodos)-2):
                signal=np.append(signal, sin_aux)
        signal=np.append(signal[div:], signal[:div])
    else:
        signal=ss.sawtooth(2*np.pi* frec * x_tiempo + (theta*(np.pi/180)))

    if FAA_ON:
        FAA_out=FAA(signal)
    else:
        FAA_out=np.copy(signal)

    if SyH_ON:
        SyH_out=SyH(FAA_out)
    else:
        SyH_out=np.copy(FAA_out)

    if LLA_ON:
        LLA_out=LLA(SyH_out)
    else:
        LLA_out=np.copy(SyH_out)

    if FR_ON:
        FR_out=FR(LLA_out)
    else:
        FR_out=np.copy(LLA_out)

    dt=x_tiempo[1] - x_tiempo[0]
    frecs_x, signal_spec = FFT(signal, dt)
    FAA_x, FAA_spec = FFT(FAA_out, dt)
    SyH_x, SyH_spec = FFT(SyH_out, dt)
    LLA_x, LLA_spec = FFT(LLA_out, dt)
    FR_x, FR_spec = FFT(FR_out, dt)

    MT=np.vstack((x_tiempo, signal, FAA_out, SyH_out, LLA_out, FR_out))
    MF_x = np.vstack((frecs_x, FAA_x, SyH_x, LLA_x, FR_x))
    MF_y = np.vstack((signal_spec, FAA_spec, SyH_spec, LLA_spec, FR_spec))

    return MT, MF_x, MF_y









def FFT(signal, dt):
    signal_fft = fft.fft(signal)
    signal_frecs = fft.fftfreq(len(signal_fft), dt)[:len(signal_fft) // 2]
    signal_spectrum = 2.0 / len(signal_fft) * np.abs(signal_fft[0:len(signal_fft) // 2])

    return signal_frecs, signal_spectrum