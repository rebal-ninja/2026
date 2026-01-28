n = int(input("enter n "))

for i in range(n):
    # prints n no of rows 
    for j in range(n-i):
        # prints the cols 
        # no of rows - the row no +1 
        print(j,end="")
    print()
    # jumps when a row ittertyaion is complete  