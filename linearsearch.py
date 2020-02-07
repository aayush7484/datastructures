def linearsearch(A,key):
    position=0
    flag=False
    while position<len(A) and not flag:
        if A[position]==key:
            flag=True
        else:
            position+=1
    return flag

A=[45,67,78,34,57,89]
n=int(input())
found=linearsearch(A,n)
print("Element %d is present:" %n,found)