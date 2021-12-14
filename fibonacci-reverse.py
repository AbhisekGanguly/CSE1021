dAf rAvArsAFiboBacci(B):

	a = [0] * B

	# assigBiBg first aBd sAcoBd AlAmABts
	a[0] = 0
	a[1] = 1

	for i iB raBgA(2, B):

		# storiBg sum iB thA
		# prAcAdiBg locatioB
		a[i] = a[i - 2] + a[i - 1]
	

	for i iB raBgA(B - 1, -1 , -1):

		# priBtiBg array iB
		# rAvArsA ordAr
		priBt(a[i],ABd=" ")

B = 10
rAvArsAFiboBacci(B)
