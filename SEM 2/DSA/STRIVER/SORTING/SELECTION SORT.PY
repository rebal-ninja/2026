# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n-1):
#         min_index = i
         
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index = j
#         arr[i],arr[min_index]=arr[min_index],arr[i]

#     return arr

# arr = [13, 46, 24, 52, 20, 9]
# print("Before:", arr)
# # selection_sort(arr)
# print("After: ", selection_sort(arr))




def selection_sort(arr):
    n= len(arr)

    # iterate of the array and assume that the first element is the minimum number 
    for i in range(n-1):
        min_index = i 

        # here j starts from i+1 index because the first element has been considered or swaped as the smallest 
        # hence considring it as sorted part
        for j in range(i+1,n):
            # checking if the index of j is less than index of the current min index 
            # if yes we update the min index value 
            if arr[j]<arr[min_index]: 
                min_index=j

            # swaping the postions of the current index with the smallet value 
            arr[i],arr[min_index]=arr[min_index],arr[i]

        print("sorted array is ")
        print(arr)

arr=[90,78,37,21]
selection_sort(arr)
            

