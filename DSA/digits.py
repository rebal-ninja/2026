# # RETURN THE NUMBER OF DIGITS 
 
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
# import math

# cnt = 0 
# n = int(input("enter n"))

# for i in range (1,int(math.sqrt(n))):
#     if n%i==0:
#         cnt+=1

#         if n//i!= i:
#             cnt+=i 

# GCD USING ECULIDIAN 

a= int(input("enter a "))
b= int(input("enter b "))


while a>0 and b>0 :
    if a>b:
        a= a%b
    
    else:
        b = b%a

        if a ==0:
            print(b)
        else:
            print(a)


print("is gcd  ")

#<<<<<<<<<<< EVERYTHING USING CLASSES >>>>>>>>>>>>>

# RETURN THE NUMBER OF DIGITS

# class digits:
#     def count_digits(self,n):
#         count = 0
#         while n>0:
#             last_digit=n%10
#             count+=1
#             n//=10
#         print(count)
# obj = digits()
# obj.count_digits(1234)            


# RETURN THE REVERSE OF GIVEN NUMBER

# class digits:
#     def reverse_number(self,n):
#         reverse =0
#         while n>0:
#             last_digit = n%10
#             reverse= (reverse*10)+last_digit
#             n//=10
#         print(reverse)

# obj = digits()
# obj.reverse_number(12345)


# CHECK IF THE NUMBER IS A PALINDROME

# class digits:
#     def palindrome(self,n):
#         temp = n
#         reverse = 0
#         while n>0:
#             last_digit=n%10
#             reverse = (reverse*10)+last_digit
#             n//=10
#         if reverse==temp:
#             print("the given number is a palindrome")
#         else:
#             print("it is not a palindrome") 

# obj=digits()
# obj.palindrome(121)


# CHECK IF THE NUMBER IS AMGSTRONG NUMBER

# class digits:
#     def amgstrong(self,n):
#         temp = n
#         sum = 0

#         while n>0:
#             last_digit = n%10
#             sum += last_digit**3
#             n//=10
#         print(sum)

#         if temp == sum :
#             print("it is an amgstrong")
#         else:
#             print("not an amgstrong ")



# obj = digits()
# obj.amgstrong(153)