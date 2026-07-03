# QUICK SORT WITH TRACING

def quick_sort(arr, low, high):

    if low < high:

        # partition returns correct pivot position
        pi = partition(arr, low, high)

        print("Pivot placed at index:", pi)
        print("Array now:", arr)
        print("-----------------------")

        # sort left part
        quick_sort(arr, low, pi-1)

        # sort right part
        quick_sort(arr, pi+1, high)


def partition(arr, low, high):

    pivot = arr[low]      # choose first element as pivot
    i = low + 1
    j = high

    print("\nPivot =", pivot)
    print("Start array:", arr)

    while True:

        # move i right until element > pivot
        while i <= j and arr[i] <= pivot:
            i += 1

        # move j left until element <= pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # if pointers cross → stop
        if i <= j:
            print("Swap", arr[i], "and", arr[j])
            arr[i], arr[j] = arr[j], arr[i]
            print("Array:", arr)
        else:
            break

    # place pivot in correct position
    print("Swap pivot", arr[low], "with", arr[j])
    arr[low], arr[j] = arr[j], arr[low]

    print("After pivot swap:", arr)

    return j


# INPUT
arr = list(map(int, input("Enter elements: ").split()))

print("Original array:", arr)

quick_sort(arr, 0, len(arr)-1)

print("Sorted array:", arr)