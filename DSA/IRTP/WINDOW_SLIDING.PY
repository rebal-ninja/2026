#FIXED WINDOW SLIDING 
# GOAL : TO FIND MAXIMUM SUM
# N = 6 
# arr  1,2,8,9,4,5[]
# WINDOW SIZE = 3 

n = int(input("enter n"))
arr = list(map(int,input("entee the array elements").split()))
win_size = int(input("entee the window size"))
win_sum = sum(arr[:win_size])
# win_sum = sum(arr[start:end]) --> arr[:3]---> arr[1+2+8]=11
max_windowsum = win_sum
# 11 
for i in range(win_size,n):
    # 3,4,5,
    win_sum+=arr[i]-arr[i-win_size]
    # win_sum = arr[3] == 9 
    max_windowsum = max(max_windowsum,win_sum)



print(max_windowsum)

