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