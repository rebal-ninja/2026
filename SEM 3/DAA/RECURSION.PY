# def fib(n):

#     if n == 0:
#         return 0
#     if n == 1:
#         return 1 

#     return fib(n-1)+fib(n-2)
# print(fib(6))

# def sorted(arr,n):
    
#     if n == 0 or n==1:
#         return True

#     if arr[(n-1)]<arr[(n-2)]:
#          return False
#     return sorted(arr,n-1)

# arr = [1, 2, 3, 4,5,6]
# print(sorted(arr,5))

def binary_search(arr,target,low,high):

    
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    
    if target <arr[mid]:
        return binary_search(arr,target,low,mid-1)
    
    return binary_search(arr,target,mid+1,high)

arr = [2, 5, 8, 12, 16, 23, 38, 56]

target = 23
print(binary_search(arr,target,0,len(arr)-1))