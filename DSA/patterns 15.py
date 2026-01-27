n= int(input("enter the value of n"))

for i in range(n,0,-1):
    for j in range(i):
        print(chr(ord("A")+j),end="")
    print()