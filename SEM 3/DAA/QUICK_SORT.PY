# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr 
    
#     pivot = arr[0]

#     left = []
#     right = []

#     for i in range(1,len(arr)):
#         if arr[i]<=pivot:
#             left.append(arr[i])

#         else:
#             right.append(arr[i])
#     return quick_sort(left)+[pivot]+quick_sort(right)

# arr = [10,8,2,5,3,2]
# print("before sorting",arr)
# print("after",quick_sort(arr))


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


numbers = [10, 78, 278, 28]
sorted_nums = quicksort(numbers)

print(sorted_nums)