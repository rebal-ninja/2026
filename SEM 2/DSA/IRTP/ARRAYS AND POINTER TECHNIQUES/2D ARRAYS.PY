# 2D MATRIX ROWS AND COLUMS 
# ROWS AND COLUMS ARE STORED IN A MATRIX

# STEP 1 : INITILIZE THE MATRIX
rows = int(input("enter the number of rows "))
# r= 4 
cols = int(input("enter the number of colums"))
# c= 3

# STEP 2 : INITILIZE THE MATRIX 
matrix = []

# STEP 3 : INPUT THE ELEMENTS 
for i in range(rows):
    row = []
    for j in range (cols):
        val = int(input(f"enter the value at [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)


# STEP 4 : PRINTING THE MATRIX 
for i in range (rows):
    # i = 0--->>>n 
    for j in range(cols):
        # j = 0---->n
        print(matrix[i][j],end=" ")
    print()


# STEP 5 : ACCESING THE ELEMENTS 
r = int(input("enter the row index "))
c = int(input("enter the column index "))

if r< rows and c<cols:
    print(f"the value of matrix at index{i}and {j} is :",matrix[r][c])
else:
    print("invalid!")