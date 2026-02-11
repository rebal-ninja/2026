# 3D MATRIX 
# CONTAINS ROWS,COLS,LAYERS,MATRIX

layers = int(input("enter the number of layers"))

rows = int(input("enter no of rows "))

cols = int(input("enter no of colums "))

matrix = []

for i in range(layers):
    layers= []
    for j in range(rows):
        row = []
        for k in range(cols):
            val = int(input(f"enter the value at [{i}][{j}][{k}]"))
            row.append(val)
        layers.append(row)
    matrix.append(layers)


    for i in range(layers):
        for j in range(rows):
            for k in range(cols):
                print(matrix[i][j][k],end=" ")
            print()


while True:
    ask = input("do you want to access the element (y/n) ")
    if ask == "y":
        l = int(input("enter the layer index "))
        r = int(input("enter the row index "))
        c = int(input("enter the column index "))
        if l< layers and r< rows and c< cols:
            print(f"the value of matrix at index {l} and {r} and {c} is :",matrix[l][r][c])
    else:
        break