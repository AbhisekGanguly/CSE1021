a = input("Enter a Number: ")
b = str(a)
l = len(b)
s = 0
B = 0
sum = 0

for i in range(l):
    s = b[i]
    B = int(s)
    sum += B**l

print(sum)
sum = int(sum)
a = int(a)

if a is sum:
    print("The Number is an Armstrong")
else:
    print("The Number is not Armstrong")

#the complexity of this algorithm is O(N) aka linear