from numpy import array, empty
from scipy.fftpack import fft, dct, idct
import random
import time

def createDummy(size):
	a = empty([size, size])
	for i in range(size):
		for j in range(size):
			a[i,j] = random.randint(0,256)
	return a

a = []

for i in range(5,5):
	print("Generating", i*500, "x",i*500, "array...")
	a.append(createDummy(i*500))

for i in range(0, len(a)):
	t = time.time()
	dct(a[i], 2)
	elapsed = time.time() - t
	print("Size:",(i+5)*500,", scipyDCTtime:", elapsed, "s, myDCTtime:","","s")


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

print(dct(sample[0], 2, norm = 'ortho'))

# DCT2 (DCT by row and then by column)
for i in range(0,8):
	sample[i] = dct(sample[i], 2, norm = 'ortho')

for i in range(0,8):
	sample[:, i] = dct(sample[:, i], 2, norm = 'ortho')

print(sample)

# Inverse DCT2

for i in range(0,8):
	sample[:, i] = idct(sample[:, i], 2, norm = 'ortho')

for i in range(0,8):
	sample[i] = idct(sample[i], 2, norm = 'ortho')

print(sample)
