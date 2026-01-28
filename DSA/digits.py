# RETURN THE NUMBER OF DIGITS 
 
# n = int(input("enter n "))


# count = 0
# while n > 0:
#     last_digit = n%10
#     count += 1
#     n //= 10
# print(count)

# # ------------------------------------------------------------------
# RETURN THE REVERSE OF GIVEN NUMBER 

# n = int(input("enter n"))

# reverse = 0 
# while n>0:
#     last_digit = n%10
#     reverse = (reverse*10)+last_digit
#     n//=10
# print(reverse)



# # ------------------------------------------------------------------
# CHECK IF THE GIVEN NUMBER IS A PALINDROME  

# n = int(input("enter n"))

# rev = 0 
# dup = n

# while n>0:
#     last_digit = n%10
#     rev = (rev*10)+last_digit 
#     n//=10

# print(rev)

# if dup==rev:
#     print("the given number is a palindrom")
# else:
#     print("it is not a palindrom")


    
# # ------------------------------------------------------------------
# CHECK IF THE GIVEN NUMBER IS AN AMGSTRONG NUMBER 

# n = int(input("enter n "))

# temp = n
# sum = 0 

# while n>0:
#     last_digit = n%10 
#     sum += last_digit**3
#     n//=10

# print(sum)

# if sum == temp:
#     print("it is an amstrong number")
# else:
#     print("it is not an amstrong number")

# ------------------------------------------------------------------
# PRINT ALL THE DIVSIORS OF N 

# n= int(input("enter n "))

# for i in range(n):
#     if i%2==0:
#         print(i,"is divisible by ",n)


# <OPTIMAL APPROACH>
# import math
# n = int(input("enter n "))
# divisors = []

# for i in range(1,int(math.sqrt(n))+1):
#     if n%i ==0:
#         divisors.append(i)

#         if i != n//i:
#             divisors.append(n//i)

# print(*sorted(divisors))


# ------------------------------------------------------------------
# CHECK IF THE GIVEN NUMBER IS PRIME 
import math

cnt = 0 
n = int(input("enter n"))

for i in range (1,int(math.sqrt(n))):
    if n%i==0:
        cnt+=1

        if n//i!= i:
            cnt+=i 
