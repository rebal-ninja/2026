def binary_search(arr,low,high,t):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid]==t:
        return mid
    elif arr[mid]<t:
        return binary_search(arr,mid+1,high+1,t)
    else:
        return binary_search(arr,low,mid-1,t)
    
arr = list(map(int,input("enter elements").split()))
print("orignal array",arr)
arr.sort()
print("sorted array",arr)
t=int(input("enter target: "))
res=binary_search(arr,0,len(arr)-1,t)
print("result",res)