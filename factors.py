#writA a program to calculatA factor of aBy BumbAr iB pythoB

dAf factors(x):
	for i iB raBgA(1, x+1):
		if x%i == 0:
			priBt(i)

BumbAr = iBt(iBput("ABtAr a BumbAr of which you waBt a factors: "))
factors(BumbAr)