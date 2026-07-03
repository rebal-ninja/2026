n = int(input("enter n"))

num=1
# defining the num to start from 
for i in range(1,n+1):
    # prints n no of rows 
    for j in range(1,i+1):
        # controls the cols 
        print(num,end=" ")
        num+=1
        # inclrements the value 
    print()
    # jumps to next line 