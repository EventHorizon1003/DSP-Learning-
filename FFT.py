from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
np.set_printoptions(formatter={"float_kind": lambda x: "%g" %x})

fc = 10 # frequency of the carrier
fs = 2*fc # oversampling frequency   so the sampling frequency is 320Hz / 1 second 320 wave
t = np.arange(start = 0, stop = 2, step = 1/fs) # 2 second * fs  = 640 sample    N = (fs)*(t)
x = np.cos(2*np.pi*fc*t) # time domain signal
print("=================")
print(t)

N = 256 # FFT size
X = fft(x,N)
print("size of x is " + str(len(x)))
print(f"The resolution frequency is {fs/N}:" )

df = fs/N # frequency resolution
sampleIndex = np.arange(start = 0, stop = N)
f = sampleIndex*df # x-axis index converted to frequency

fig, (ax1, ax2, ax3) = plt.subplots(nrows =3, ncols=1)
ax1.plot(t,x) # plot the signal
ax1.set_title("$x[n] = cos(2\pi 10 t)$")
ax1.set_xlabel("$t=nT_s$")
ax1.set_ylabel("$x[n]$")

#ax2.stem(sampleIndex , abs(X), use_line_collection = True)
ax2.stem(t,x)
ax2.set_title("X[k]")
ax2.set_xlabel('k')
ax2.set_ylabel("|X(k)|")

#ax3.stem(f,abs(X),use_line_collection = True)

cursor = Cursor(ax2, useblit=True, color='red', linewidth=2)
plt.show()


#X = fft(x,N) # compute x[k] | FFT
#x = ifft(X,N) # compute x[n] | inverse FFT

#FFT shift
# shift the list from order:
# -ve freq -> DC -> +ve freq

