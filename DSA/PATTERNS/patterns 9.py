n = int(input("enter n"))

for i in range(n):
    # space 
    for j in range(n-i-1):
        print(" ",end="")
    # print
    for j in range(2*i+1):
        print("*",end="")
    # space 
    for j in range(n-i-1):
        print(" ",end="")
    print()


for i in range(n - 1, -1, -1):
    # left spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # stars
    for j in range(2 * i + 1):
        print("*", end="")
    # right spaces (optional)
    for j in range(n - i - 1):
        print(" ", end="")
    print()
