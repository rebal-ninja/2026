def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i 
    return -1

arr = [10,20,30,40,50]
x = 40
res=linear_search(arr,x)

if res!=-1:
    print("array found at index",res)
else:
    print("array is not present")