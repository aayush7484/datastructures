def binarysearch(A,key,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if A[mid]==key:
            return True
        elif key>A[mid]:
            return binarysearch(A,key,mid+1,high)
        else:
            return binarysearch(A,key,low,mid-1)
A=[12,34,45,56,67,78]
n=int(input())
found=binarysearch(A,n,0,5)
print("The element %d is found:"%n,found)