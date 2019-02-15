from dct import dct2, idct2
import random
import time
from numpy import empty

dummies = []

def createDummy(size):
	a = empty([size, size])
	for i in range(size):
		for j in range(size):
			a[i,j] = random.randint(0,256)
	return a

for i in range(5,6):
	print("Generating", i*500, "x",i*500, "array...")
	dummies.append(createDummy(i*500))

for i in range(0, len(dummies)):
	t = time.time()
	dct2(dummies[i])
	elapsed = time.time() - t
	print("Size:",(i+5)*500,", scipyDCTtime:", elapsed, "s, myDCTtime:","","s")