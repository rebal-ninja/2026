# import random 

# num = random.randint(1,10)

# while True:
#     guess = int(input("guess a number"))
#     if guess < num:
#         print("num is too low")
#     elif guess > num:
#         print("num is too high")
#     else:
#         print("Your guess is right!!!")
#         break


# import statistics

# count = int(input("enter a number"))

# if count ==0:
#     print("invalid")
# else:
#     num = []

#     for i in range(count):
#         n = int(input("enter a num to add in the list"))
#         num.append(n)

#     print(statistics.mean(num))



# import statistics
# while True:
#     try:
#         count = int(input("enter a number"))

#         if count ==0:
#             print("invalid")
#         else:
#             num = []

#             for i in range(count):
#                 n = int(input("enter a num to add in the list"))
#                 num.append(n)

#             print(statistics.mean(num))
#             break
#     except:
#         print("invalid input")
        

import random

while True:
    side = random.randint(1,6)
    print(side)

    user = input("continue? Y/N").upper()
    if user =="Y":
        continue
    elif user =="N":
        break
    else:
        print("invalid input")    