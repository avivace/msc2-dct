from numpy import array, empty, allclose
from scipy.fftpack import fft, dct, idct

# Wrap 2D SciPy DCT (FTT)
def dct2(a):
	size1=a.shape[0]
	size2=a.shape[1]
	output = empty([size1, size2])

	# DCT2 (DCT by row and then by column)
	for i in range(0,size1):
		output[i] = dct(a[i], 2, norm = 'ortho')

	for i in range(0,size2):
		output[:, i] = dct(output[:, i], 2, norm = 'ortho')

	return output

# Wrap 2D SciPy IDCT2 (FTT)
def idct2(a):
	size1=a.shape[0]
	size2=a.shape[1]
	output = empty([size1, size2])

	for i in range(0,size2):
		output[:, i] = idct(a[:, i], 2, norm = 'ortho')

	for i in range(0,size1):
		output[i] = idct(output[i], 2, norm = 'ortho')

	return output
