n = int(input("enter the number of students"))

students= {}

for i in range(n):
    name = input("name of the student")
    m1 = int((input("marks 1 ")))
    m2 = int((input("marks 2 ")))
    m3 = int((input("marks 3 ")))

    students[name]=[m1,m2,m3]

student_query=input("enter the name of the student")

marks = students[student_query]
avg = (marks[0]+marks[1]+marks[2])/len(marks)

print(avg)