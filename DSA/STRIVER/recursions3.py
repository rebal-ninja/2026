# # # REVERSE AN ARRAY 

# # arr = [1,2,3,4,5]

# # def reverse_array(arr,left,right):

# #     if left>=right:
# #         return
    

# #     arr[left],arr[right] = arr[right],arr[left]

# #     reverse_array(arr,left+1,right-1)

# # reverse_array(arr,0,len(arr)-1)


# # print(arr)



# # CHECK IF THE GIVEN STRING IS A PALINDORME 

# s = "madam"

# # indexes:  0   1   2   3   4
# # letters:  m   a   d   a   m
# # length = 5, middle = len(s)//2 = 2

# def palindrome(i,s):
#     if i >= len(s)//2:
#         return True
#     # BASE CONDITION : IF REACH TILL MIDDLE ALL CONDITIONS ARE MATCHED

#     if s[i]!= s[len(s)-i -1]:
#         return False
#     # THIS SHOWS THAT ITS NOT A PALINDROME 

#     return(palindrome(i+1,s))

# # ---------------- VISUAL FLOW ----------------
# # Call 1: i=0 → compare s[0] & s[4] → m == m ✅ → call i=1
# # Call 2: i=1 → compare s[1] & s[3] → a == a ✅ → call i=2
# # Call 3: i=2 → i>=middle → return True
# # recursion unwinds → final result = True

# print(palindrome(0,s))  # True

# # ---------------- KEY POINTS ----------------
# # i = left pointer moving inward
# # len(s)-i-1 = mirror index from right
# # True = palindrome confirmed
# # False = mismatch found, stop
# # recursion checks one pair at a time and stops automatically at middle




# FIBONACCI WITHOUT RECURSION (USING FOR LOOP)

# n = 7   # how many Fibonacci numbers you want

# a = 0   # first number
# b = 1   # second number

# print(a, b, end=" ")

# for i in range(2, n):
#     c = a + b      # next Fibonacci number
#     print(c, end=" ")

#     a = b          # move forward
#     b = c



# SAME FIBONACI WITH RECURSIONS

def fibonacci(n):
    if n<=1:
        return n
    
    last = fibonacci(n-1)
    second_last = fibonacci(n-2)

    return(last+second_last)

print(fibonacci(7))