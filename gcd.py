def gcd(a,b):
    if a == 0:
        return b
    
    return gcd(b%a, a)

a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))

print("gcd(", a , "," , b, ") = ", gcd(a, b))