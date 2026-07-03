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




# # DETAILED VISUAL EXPLANATION — WHAT IS ACTUALLY HAPPENING IN MEMORY

# arr = [13, 46, 24, 52, 20, 9]
# n = 6


# # =========================
# # OUTER LOOP (PASSES)
# # =========================
# for i in range(n - 1, -1, -1):
#     # i goes like: 5 → 4 → 3 → 2 → 1 → 0
#     #
#     # THINK OF i AS:
#     # "Last index of the UNSORTED part"
#     #
#     # Everything to the RIGHT of i is already SORTED
#     #
#     # Example:
#     # i = 5 → full array unsorted
#     # i = 4 → last element sorted
#     # i = 3 → last 2 elements sorted

#     did_swap = False
#     # did_swap = False means:
#     # "So far, this pass has NOT fixed anything"


#     # =========================
#     # INNER LOOP (COMPARISONS)
#     # =========================
#     for j in range(i):
#         # j moves LEFT → RIGHT
#         # j = 0, 1, 2, ..., i-1
#         #
#         # We compare:
#         # arr[j]  ↔  arr[j+1]

#         # -------------------------
#         # VISUAL WALKTHROUGH
#         # -------------------------
#         #
#         # PASS 1 → i = 5
#         #
#         # Initial:
#         # [13, 46, 24, 52, 20, 9]
#         #
#         # j = 0 → compare 13 & 46
#         # 13 < 46 → NO SWAP
#         #
#         # j = 1 → compare 46 & 24
#         # 46 > 24 → SWAP
#         # [13, 24, 46, 52, 20, 9]
#         #
#         # j = 2 → compare 46 & 52
#         # 46 < 52 → NO SWAP
#         #
#         # j = 3 → compare 52 & 20
#         # 52 > 20 → SWAP
#         # [13, 24, 46, 20, 52, 9]
#         #
#         # j = 4 → compare 52 & 9
#         # 52 > 9 → SWAP
#         # [13, 24, 46, 20, 9, 52]
#         #
#         # RESULT:
#         # Largest element (52) has "BUBBLED" to the END

#         if arr[j] > arr[j + 1]:
#             # WRONG ORDER detected

#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             # SWAP fixes local disorder

#             did_swap = True
#             # CONFIRMS:
#             # "This pass actually did some work"


#     # =========================
#     # AFTER ONE FULL PASS
#     # =========================
#     #
#     # If did_swap is STILL False:
#     # → No swaps happened
#     # → Array was already sorted
#     # → Further passes are useless

#     if not did_swap:
#         break


# # =========================
# # BIG PICTURE (MENTAL MODEL)
# # =========================
# #
# # Each pass:
# # - Pushes the BIGGEST unsorted element to the RIGHT
# #
# # Memory state after each pass:
# #
# # Pass 1 → [13, 24, 46, 20, 9, 52]
# # Pass 2 → [13, 24, 20, 9, 46, 52]
# # Pass 3 → [13, 20, 9, 24, 46, 52]
# # Pass 4 → [13, 9, 20, 24, 46, 52]
# # Pass 5 → [9, 13, 20, 24, 46, 52]
# #
# # Sorted.
# #
# # CORE TRUTH:
# # - i shrinks the problem
# # - j fixes local disorder
# # - did_swap saves time


def bubble_sort_recursive(arr, n):

    # base case
    if n == 1:
        return

    # one pass (same inner logic as iterative version)
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # recursive call replaces outer loop
    bubble_sort_recursive(arr, n - 1)