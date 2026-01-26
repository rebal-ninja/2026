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