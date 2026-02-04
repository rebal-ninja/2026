# # BUBBLE SORT — BRUTE FORCE → OPTIMIZED (VISUAL + LOGIC IN ONE PLACE)

# arr = [13, 46, 24, 52, 20, 9]
# n = len(arr)

# # =========================
# # BRUTE FORCE BUBBLE SORT
# # =========================
# # Idea:
# # - Compare adjacent elements
# # - Swap if left > right
# # - Do ALL passes (even if already sorted)

# # Visual pass explanation:
# # Pass 1: largest element moves to end
# # Pass 2: second largest moves to its position
# # ...
# # Total passes = n-1
# # Time = O(n^2)

# for i in range(n - 1):
#     for j in range(n - 1):
#         # Compare adjacent elements
#         if arr[j] > arr[j + 1]:
#             # Swap
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print("After Brute Force Bubble Sort:")
# print(arr)

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

for i in range(n-1,-1,-1):
    did_swap = False

    for j in range (i):
        if arr[j]>arr[j+1]:

            arr[j],arr[j+1]=arr[j+1],arr[j]
            did_swap = True

    if not did_swap:
        break

print(arr)