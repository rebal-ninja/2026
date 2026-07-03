# while loop
# i = 3 
# while i !=0:
#     print("meow")
#     i = i-1

# for loop 
# while True: 
#     n = int(input("whats n?"))
#     if n>0:
#         break

# for i in range(n):
#     print("meow")

# taking an input from teh user 
# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n= int(input("whats n?"))
#         if n>0:
#             return n

# def meow(n):
#     for i in range (n):
#         print("meow")

# main()

# students = ["tez","aman","bhasker"]
# for student in students:
#     print(student)

# students = ["tez","divya","yashu"]
# for i in range(len(students)):
#     print(i+1,students[i])


# dictionary
# students = {
#     "harry":"griffindor",
#     "heromine": "griffindor",
#     "ron":"griffindor",
#     "draco": "slytherin"
# }

# for student in students:
#     print(student,students[student], sep=", ")


# students = [
#     {"name":"heromine", "house": "griffindor", "patronus": "otter"},
#     {"name":"harry", "house": "griffindor", "patronus": "stag"},
#     {"name":"ron", "house": "griffindor", "patronus": "jack russel terrier"},
#     {"name":"draco", "house": "slytherin", "patronus": None}
# ]
# for student in students:
#     print(student["name"],student["house"],student["patronus"] ,sep=", ")

# def main():
#      print_coloum(2)
#      print_row(3)

# def print_row(width):
#         print("?"*width)
        

# def print_coloum(height):
#     for i in range(height):
#         print("#")
# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()

main()