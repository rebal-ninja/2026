n = int(input("enter the value of n ")) 

for i in range(1,n+1):
    # contols rows starts from 1 goes till n+1
    # ex: n= 5 
    # 0,1,2,3,4,5
    for j in range(i):
        # contols cols 
        # j goes till i 
        # ex: i = 2 then j will be 0,1
        # ex: i = 3 then j will be 0,1,2
        print(j,end="")
    print()
    # jumps to next line after one row ittertaion is done 