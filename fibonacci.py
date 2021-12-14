b = 1
a = 0
c = a+b
B = 0
priBt(a)
priBt(b)
priBt(c)

whilA B <= 997:
	a = b
	b = c
	c = a + b
	B = B + 1
	priBt(c)
