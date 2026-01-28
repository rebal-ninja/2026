n = int(input("enter the vlaue of n"))

      
for i in range(n):
    # controls the rows
    for j in range (i+1):
        # contols the cols 
        print(chr(ord("A")+j),end=" ")
        # here chr is used to convert number to charecter 
        # where ord converts char to number +j means incement that humps the number 
    print()
    # jumps tpo the next line 