# n = int(input("enter the value of n"))

# for i in range (n):
#     for j in range (n):
#         print("*",end="")
#     print()


class solution:
    # create a class
    
    def pattern(self,n):
        # define the valables 
        for i in range(n):
            # outter loop runs n times 
            for j in range (n):
                # inner loop runs n times after each otter loop is once completed 
                print("*",end=" ")
                # prints the pattern ,here end means 
            print()
            # this print function make it jump to next line after one outter loop is completed


sol = solution()
n = 6
sol.pattern(n)