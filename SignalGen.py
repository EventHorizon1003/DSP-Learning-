import numpy as np

def sine_wave(f, overSampRate, phase, nCyl):
    """
    Generate Sine wave
    Parameters:
    f: frequency of sine wave (Hertz)
    OverSamRate: oversampling rate (integer)
    phase: desired phase shift in radians
    nCyl: number of cycles of sine wave to generate
    Returns:
    (t,g): time base (t) and g(t) as tuple
    Examples:
    (t,g) = sine_wave(10,30,1/3*np.pi,5)
    """
    fs = overSampRate*f # sampling frequency
    t = np.arange(0,(nCyl*1/f),1/fs) # time base
    print("testing :" + str(nCyl*1/f-1/fs))
    g = np.sin(2*np.pi*f*t + phase)
    return (t,g)

def square_wave(f,overSampRate,nCyl,duty) :
    if duty == "":
        fs = overSampRate*f # Sampling frequency
        t  = np.arange(0,(nCyl/1/f), (1/fs))
        g = np.sign(np.sin(2*np.pi*f*t))
    else:
        from scipy import signal
        fs = overSampRate*f
        t = np.arange(0,(nCyl/1/f),(1/fs))
        g = signal.square(2*np.pi*f*t, duty)
    return (t,g)

def rectangular_wave(A,fs,T):
    # default value range is -0.5 to 0.5
    # T is duration pulse in seconds
    t = np.arange(-0.5,0.5,1/fs)
    rect = (t > -T/2) * (t < T/2) + 0.5*(t==T/2) + 0.5*(t==-T/2)
    g = A*rect
    return(t,g)
