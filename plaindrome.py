my_str = str(input("Enter a string: "))

my_str = my_str.casefold()
reverse = reversed(my_str)

if list(my_str) == list(reverse):
   print("The string is a plainrome.")
else:
   print("Thr string is not a plaindrome.")