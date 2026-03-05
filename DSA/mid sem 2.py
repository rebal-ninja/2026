# TOH 

# def TOH(n,source,aux,des):
#     if n ==0:
#         return
#     TOH(n-1,source,des,aux)
#     print(f"move disk {n} from {source} to {des}")
#     TOH(n-1,aux,source,des)

# n =3 
# TOH(n,"a","b","c")

# PREFIC SUM 

# arr = [10,20,30,40,50]
# prefix_sum = [0]*len(arr)

# prefix_sum[0]= arr[0]
# for i in range (1,len(arr)):
#     prefix_sum[i] = prefix_sum[i-1]+arr[i]

# l = 1
# r = 3 

# if l ==0:
#     range_sum = prefix_sum[r]
# else:
#     range_sum = prefix_sum[r]-prefix_sum[l-i]

# print(range_sum)


# BUBBLE SORT


# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

# arr = [5,3,1,4,2]
# bubble_sort(arr)
# print(arr)

# RECURSION


# def func(n):
#     if n == 0:
#         return
#     print(n)
#     func(n-1)

# func(5)

# def a(n):
#     if n>0:
#         b(n-1)

# def b(n):
#     if n>0:
#         a(n-1)

# def fact(n):
#     if n ==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(5))


# LINEAR SEARCH 

# def linear_search(arr,key):
#     for i in range(len(arr)):
#         if arr[i]==key:
#             return i 
#     return -1

# arr = [10,20,30,40]
# key = 30

# pos = linear_search(arr,key)
# print("elemnt found at index",pos )


# SELECTION SORT 

# def seceltion_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_index = i 

#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index = j 

#         arr[i],arr[min_index] = arr[min_index],arr[i]

# arr = [29,10,14,37,13]
# seceltion_sort(arr)
# print(arr)

# INSERTON SORT 
# def insertion_sort(arr):
#     for i in range (1,len(arr)):
#         key = arr[i]
        

# binary search 

# def binary_search(arr,key):
#     low = 0 
#     high = len(arr)-1

#     while low <= high:
#         mid = (low +high)//2
#         if arr[mid]==key:
#             return mid
#         elif arr[mid]>key:
#             high = mid-1
#         else:
#             low = mid +1


# arr = [10,20,30,40]
# print(binary_search(arr,30))


# def linea_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i 
#     return -1
        
# arr= [10,20,30,40,50]
# res = linea_search(arr,760)

# if res==-1:
#     print("element not found")
# else:
#     print("element found at index",res)


# arr=[10,20,30,40,50]

# prefix_sum =[0]*len(arr)
# prefix_sum[0]=arr[0]
# for i in range (1,len(arr)):
#     prefix_sum[i]=prefix_sum[i-1]+arr[i]

#     print(prefix_sum)

# l= 1
# r= 3

# if l==0:
#     range_sum = prefix_sum[r]
# else:
#     range_sum = prefix_sum[r]-prefix_sum[l-1]
#     print[range_sum]


# arr=[10,20,30,40,50] 
# prefix_sum=[0]*len(arr) 
# prefix_sum[0]=arr[0] 
# for i in range(1,len(arr)): 
#     prefix_sum[i]=prefix_sum[i-1]+arr[i] 
# print("original array",arr) 
# print("prefix sum array",prefix_sum) 
# #To find the range sum 
# l=1 
# r=3 
# if l==0: 
#     range_sum=prefix_sum[r] 
# else: 
#     range_sum = prefix_sum[r]-prefix_sum[l-1] 
# print("rangesum is:",range_sum) 



# def bubble_sort(arr):
#     n= len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]> arr[j+1]:
#                 arr[j],arr[j+1]= arr[j+1],arr[j]

# arr= [5,2,4,1,3]
# bubble_sort(arr)
# print(arr)



# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n= 5    
# res= factorial(n)
# print(res)

# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1

#     mid = (low+high)//2
#     if arr[mid]==target:
#         return target
#     if arr[mid]<target:
#         high = arr[mid]-1
#     if arr[mid]>target:
#         low = arr[mid]+1 




# arr=[20,30,60,50,40]
# prefix_sum=[0]*len(arr)
# prefix_sum[0]=arr[0]
# for i in range(1,len(arr)):
#     prefix_sum[i]=prefix_sum[i-1]+arr[i]
# print("orignal array",arr)
# print("new array",prefix_sum)

# l=1
# r=3

# if l==0:
#     range_sum = prefix_sum[r]
# else:
#     range_sum = prefix_sum[r]-prefix_sum[l-1]
# print(range_sum)



# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range (0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]

# arr= [5,3,1,4,2]
# bubble_sort(arr)
# print(arr) 


# def factorial(n):
#     if n ==0:
#         return 1 
#     else:
#         return n*factorial(n-1)

# print(factorial(5))


def binary_search(arr,key):
    low = 0 
    high = len(arr)

    while low<=high:
        mid = (low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            high = mid-1
        else:
            arr[mid]>key
            low = mid +1
        return -1
arr=[10,20,30,40,50]
print(binary_search(arr,30))