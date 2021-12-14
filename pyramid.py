rows = 5

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print("  ",end="")
    for j in range(0, i):
        print("*", end = " ")
    print()