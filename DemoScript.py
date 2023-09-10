import SignalGen
import numpy as np
import matplotlib.pyplot as plt

def demo_sin():
    f = 10 #Hz
    overSample = 20
    phase = (np.pi/180)*0
    ncyl = 2
    (t,g) = SignalGen.sine_wave(f,overSample,phase,ncyl)

    plt.plot(t,g)
    plt.title('Sine Wave with' + str(f) + "Hz")
    plt.xlabel("Amplitude")
    plt.ylabel("Time (s)")
    plt.show()

def demo_square():
    f = 10 #Hz
    Oversampfreq = 20
    nCyl = 5
    [t,g] = SignalGen.square_wave(f,Oversampfreq,nCyl,0.1)

    plt.plot(t,g)
    plt.show()

def demo_rectangular():
    T = 0.9 # Rectangular width
    # By default is -0.5 to 0.5 (1 sec range)
    A = 1
    fs = 500
    [t,g] = SignalGen.rectangular_wave(A,fs,T)

    plt.plot(t,g)
    plt.show()

demo_rectangular()
#demo()
#demo_square()
