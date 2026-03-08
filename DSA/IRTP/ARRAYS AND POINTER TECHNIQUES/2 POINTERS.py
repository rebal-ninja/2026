# # TWO POINTERS 

# # N = 8 
# # arr = [7,6,5,4,3,,1,8]

# def prefix_sum(arr):
#     n = len(arr)
#     # lenght of array required to make a duplicate array of the same lenght 
#     prefix = [0]*n
#     # ths creates the array of the same lenght 
#     prefix[0]=arr[0]
#     # this stores the index from arr at 0 to perfix at the zeroth index 
#     for i in range(1,n):
#         # loop starts from 1 to n-1
#         prefix[i] = prefix[i-1] + arr[i]
#         # this adds the previous index value of perfix to the current index value of arr and
#         # stores it in the current index of perfix
#     return prefix
# print(prefix_sum([7,6,5,4,3,2,1,8]))



# n = 8 
# arr = [1,2,3,4,5,6,7,8,9]
# prefix = [1,3,6,10,15,21,28,36,45]
n = int(input("enter the size of array "))
arr =list(map(int,input("enter elements").split()))
prefix = [0]*n
prefix[0]= arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
print("the prefix sum is ",prefix)
l = int(input("enter the staring index "))
r = int(input("enter the ending  index "))
if l==0:
    res = prefix[r]
else:
    res = prefix[r]-prefix[l-1]
print(f"the sum from staring index {l} and ending index {r} is {res}")
# <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# LEETCODE 283 
# GOAL:
# Move all zeros to the end of the array
# Keep the order of non-zero elements the SAME
# Do it IN-PLACE (no extra array)

nums = [0, 1, 0, 3, 12]

# two pointers
left = 0        # position where the next NON-ZERO should go

# right pointer scans the array
for right in range(len(nums)):

    # STEP-BY-STEP DRY RUN 👇

    # INITIAL STATE
    # nums  = [0, 1, 0, 3, 12]
    # left  = 0
    # right = starts from 0

    # right = 0 → nums[0] = 0
    # nums[right] == 0 → condition FAILS
    # nothing happens
    # nums = [0, 1, 0, 3, 12]
    # left = 0

    # right = 1 → nums[1] = 1
    if nums[right] != 0:
        # swap nums[right] and nums[left]
        nums[right], nums[left] = nums[left], nums[right]
        # swap nums[1] and nums[0]
        # nums becomes [1, 0, 0, 3, 12]

        left += 1
        # left = 1

    # right = 2 → nums[2] = 0
    # nums[right] == 0 → condition FAILS
    # nothing happens
    # nums = [1, 0, 0, 3, 12]
    # left = 1

    # right = 3 → nums[3] = 3
    if nums[right] != 0:
        # swap nums[3] and nums[1]
        # nums becomes [1, 3, 0, 0, 12]
        nums[right], nums[left] = nums[left], nums[right]

        left += 1
        # left = 2

    # right = 4 → nums[4] = 12
    if nums[right] != 0:
        # swap nums[4] and nums[2]
        # nums becomes [1, 3, 12, 0, 0]
        nums[right], nums[left] = nums[left], nums[right]

        left += 1
        # left = 3

# LOOP ENDS

# FINAL ARRAY
# nums = [1, 3, 12, 0, 0]
print(nums)