# DSP-Learning
#SignalGen.py 
 ## sine_wave(f, overSampRate, phase, nCyl)
 - Create a sinuoid with defined parameters as below
   - f : frequency of analog wave 
   - OverSample : sample rate of frequency
   - phase : Phase shift in rad 
   - nCycl : number of cycle 
 ## square_wave(f,overSampRate,nCyl,duty)
 - Create a square pulse wave with defined parameters as below
   - f: frequency of analog wave
   - OverSample: sample rate of frequency 
   - nCyl: number of cycle
   - dut: duty cycle (by default is 0.5)
     (time_on/(time_on + time_off)%)
 
## rectangular_wave(A,fs,T)
   - Generate a rectangular wave 
   - By default the rectangular width is 1s only (-0.5 to 0.5)
   - A: Amplitude of the rectangular wave
   - fs: Sampling frequency (Hz)
   - T: width of rectangular wave(s)
      - True*True = 1
      - True*False = 0
      - False*True = 0
      - False*False = 0
## gaussian_pulse(fs,sigma)
   - used in GFSK which is one type of FSK
   - The impulse response is Gaussian distribution
   - Gaussian give no overshoot with minimal rise & fall time
   - it have minimum group delay 
   - The sigma to produce gaussian distribution is 0.1
   - fs: Sampling frequency (Hz)
   - sigma: gaussian coefficient

## scipy.signal.chirp(t,f0,t1,f1,phi,method="linear")
   - t is list of time 
   - f0 is initial frequency
   - t1 is stating time for vary frequency 
   - phi is initial phase 
   - method = "linear" change the frequency of the signal linearly 
     - A signal with time-varying frequency is called
       chirp 
     - up-chirp (from low to high frequency)
     - low-chirp (from high to low frequency)