from numpy import array, empty, allclose, pi, cos, zeros
from scipy.fftpack import fft, dct, idct
from math import sqrt

# My DCT implementation
def mydct2_mono(a):
    #           N-1
    # y[k] = 2* sum x[n]*cos(pi*k*(2n+1)/(2*N)), 0 <= k < N.
    #           n=0
    n = len(a)
    output = zeros(n)

    for k in range(0, n):
        for i in range(0, n):
            output[k] += a[i]*cos(pi*k*(2*i+1)/(2*n))
        output[k] *= 2
        # If norm='ortho', y[k] is multiplied by a scaling factor f:
        #  f = sqrt(1/(4*N)) if k = 0,
        #  f = sqrt(1/(2*N)) otherwise.
        if k==0:
            output[k] *= sqrt(1/(4*n))
        else:
            output[k] *= sqrt(1/(2*n))
    return output

def my_dct2(a):
    size1=a.shape[0]
    size2=a.shape[1]
    output = empty([size1, size2])

    # DCT2 (DCT by row and then by column)
    for i in range(0,size1):
        output[i] = mydct2_mono(a[i])
    
    # The [:, n] notation gives access the n-th column
    for i in range(0,size2):
        output[:, i] = mydct2_mono(output[:, i])

    return output

# Wrap 2D SciPy DCT (FTT)
def dct2(a):
    size1=a.shape[0]
    size2=a.shape[1]
    output = empty([size1, size2])

    # DCT2 (DCT by row and then by column)
    for i in range(0,size1):
        output[i] = dct(a[i], 2, norm = 'ortho')

    # The [:, n] notation gives access the n-th column
    for i in range(0,size2):
        output[:, i] = dct(output[:, i], 2, norm = 'ortho')

    return output

# Wrap 2D SciPy IDCT2 (FTT)
def idct2(a):
    size1=a.shape[0]
    size2=a.shape[1]
    output = empty([size1, size2])

    # by row and then by column
    for i in range(0,size2):
        output[:, i] = idct(a[:, i], 2, norm = 'ortho')

    for i in range(0,size1):
        output[i] = idct(output[i], 2, norm = 'ortho')

    return output