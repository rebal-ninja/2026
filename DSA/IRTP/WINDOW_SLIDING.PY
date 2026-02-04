# #FIXED WINDOW SLIDING 
# # GOAL : TO FIND MAXIMUM SUM
# # N = 6 
# # arr  1,2,8,9,4,5[]
# # WINDOW SIZE = 3 

# n = int(input("enter n"))
# arr = list(map(int,input("entee the array elements").split()))
# win_size = int(input("entee the window size"))
# win_sum = sum(arr[:win_size])
# # win_sum = sum(arr[start:end]) --> arr[:3]---> arr[1+2+8]=11
# max_windowsum = win_sum
# # 11 
# for i in range(win_size,n):
#     # 3,4,5,
#     win_sum+=arr[i]-arr[i-win_size]
#     # win_sum = arr[3] == 9 
#     max_windowsum = max(max_windowsum,win_sum) cvfvb  



# print(max_windowsum)



# <<<<<<<<<<<<<<-------DYNAMIC WINDOW SLIDING-------->>>>>>>>>>>>>>>>>>>>>

# GOAL:TO FIND THE MINIMUM LENGHT OF TARGET
# N= 6 
# ARR = [1,2,3,4,5,6]
# TARGET = 6 

n = int(input("enter n"))
arr = list(map(int,input("enter the elements of array").split()))
target = int(input("enter the target"))
min_len = n+1
# min_len = 6+1=7 
current_sum = 0 
left = 0 
right = 0 
for i in range(n):
    current_sum+=arr[right]
    while current_sum >= target:
        min_len = min(min_len, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_len == n + 1:
    print(0)
else:
    print(min_len)
    