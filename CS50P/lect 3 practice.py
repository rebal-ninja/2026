# while True:
#     try:
#         a = int(input("enter a number"))
        
#     except ValueError:
#         print("input is not a number")

#     else:
#         break 
# print(a,"is the input given")


while True:
    try:
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
        print(a/b)
    
    except ZeroDivisionError:  
            print("can not divide!")

    except ValueError:
        print("enter a integer")
        
    else:
        break