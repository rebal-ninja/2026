# MERGE SORT 
def merge_sort(arr):
    # base condition 
    # check 0 and 1 
    if len(arr)<=1:
        return arr
    # [20,10,23,2,1,89,45,4]
    mid = len(arr)//2
    # mid = 8///2--> 4 

    left = merge_sort(arr[:mid])
    # left = 0,1,2,3---> [20,10,23,2] --> [2,10,20,23]

    right = merge_sort(arr[mid:])
    # right = [1,89,45,4]--> [1,4,45,89]
    return merge(left,right)

def merge(left,right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged   

arr = list(map(int,input("entee elements ").split()))
print("sorted array is ",merge_sort(arr))

