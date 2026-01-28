N = int(input("enter N"))        

spaces = 2 * (N - 1)
        
# Outer loop for the number of rows
for i in range(1, N + 1):
            
# Inner loop to print numbers in increasing order
        for j in range(1, i + 1):
                print(j, end="")
            
            # Inner loop to print spaces in the middle
        for j in range(1, spaces + 1):
                print(" ", end="")
            
            # Inner loop to print numbers in decreasing order
        for j in range(i, 0, -1):
                print(j, end="")
            
            # Move to the next line after printing the row
        print()
            
            # Decrease spaces by 2 after each row
        spaces -= 2
