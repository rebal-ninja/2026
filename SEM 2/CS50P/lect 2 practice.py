# # for i in range(5):
# #     print("hello")

# # number = int(input("enter a number"))
# # while number<0:
# #     print("invalid input")
# #     number = int(input("enter again!"))

# # print(number)

# # def main():
# #     repeat(3)

# # def repeat(n):
# #     for i in range (n):
# #         print("cs50")

# # main()


# for i in range(0, 11, 2):
#     print(i)
    

def main():
   if is_even(number):
       print("even")
   else:
       print("odd")

def is_even(n):
    return n %2 ==0
number = int(input("enter a number"))
main()