import math
def sfera(r):
	volume=(r**3*math.pi*4/3)
	return volume

r=input ('raggio:')
r=int(r)
print(sfera(r))
