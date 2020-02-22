def binarysearch1(A, key):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == key:
            return True
        elif A[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return False



A = [23, 34, 45, 56, 67, 78]
found = binarysearch1(A, 563)
print("The element is", found)
