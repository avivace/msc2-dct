from dct import dct2, idct2, my_dct2
import random
import time
from numpy import empty, allclose, random
import csv

wtr = csv.writer(open ('times_scipy.csv', 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(["n","scipyTime", "myTime"])

dummies = []

def createDummy(size):
	a = random.rand(size,size)
	return a

for i in range(1,10):
	print("Generating", i*1000, "x", i*1000, "array...")
	dummies.append(createDummy(i*1000))

for i in range(0, len(dummies)):
	t = time.time()
	scipy=dct2(dummies[i])
	elapsedSciPy = time.time() - t
	#t = time.time()
	#my=my_dct2(dummies[i])
	#elapsedMy = time.time() - t
	#print(allclose (scipy, my))
	wtr.writerow([dummies[i].shape[0],elapsedSciPy])
	#print("Size:",dummies[i].shape[0],", scipyDCTtime:", elapsedSciPy, "s, myDCTtime:",elapsedMy,"s")
