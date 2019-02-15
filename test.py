from dct import dct2, idct2
from numpy import array, empty, allclose
from scipy.fftpack import fft, dct, idct

sample = empty([8,8])

sample = array([[231, 32, 233, 161, 24, 71, 140, 245],
				[247, 40, 248, 245, 124, 204, 36, 107],
				[234 ,202, 245, 167, 9, 217, 239, 173],
				[193, 190, 100, 167, 43, 180, 8, 70],
				[11, 24, 210, 177, 81, 243, 8, 112],
				[97, 195, 203, 47, 125, 114, 165, 181],
				[193, 70, 174, 167, 41, 30, 127, 245],
				[87, 149, 57, 192, 65, 129, 178, 228]])

print(sample)

print(dct(sample[0], 2, norm= 'ortho'))
print(dct2(sample))
print(allclose (sample, idct2(dct2(sample))))
