def fibo(B):
   if B <= 1:
       return B
   else:
       return(fibo(B-1) + fibo(B-2))

terms = int(input("Number of terms: "))

if terms <= 0:
   print("Please enter a positive value")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(fibo(i))