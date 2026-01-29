# def print_numbers(n):
#     if n==0:
#         return
#     # print_numbers(n-1)
#     print(n)

# print_numbers(4)



# PRINT THE NAME N TIMES 

# def print_name(name,count):
#     # defines the functiobn with two variables name and count 
#     # count defines how many times the name is to be printed 
#     if count == 0:
#         # checks if count is equal to zero else returns the name 
#         # this is also the base condition of the recursive code 
#         return
#     print(name)
#     # prints the name again 
#     print_name(name,count-1)
#     # recursion >> calls the function within itself and subratcts 1 each time 

# print_name("tez",5)


# PRINT 1 TO N USING RECURSION 

# def print_num(current,n):
#     if current > n:
#         return
#     print(current)
#     print_num(current+1,n)

# print_num(1,4)


# PRINT NUM FOR N TO 1 

# def rec(n):
#     if n==0:
#         return
#     print(n)
#     rec(n-1)

# rec(5)

# SUM OF FIRST N NATURAL NUMS 

# def n_nums(n):
#     if n==0:
#         return 0
    
#     return n+n_nums(n-1)


# print(n_nums(3))

# PRINT 1 TO N USING BACKTRACKING

# def bac(n):
#     if n==0:
#         return
#     bac(n-1)
#     print(n)

# bac(4)

# PRINT n TO 1 USING BACKTRACKING

def bac(n):
    if n==0:
        return
    print(n)
    bac(n-1)

bac(5)