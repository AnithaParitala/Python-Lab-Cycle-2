def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [22,33,44,55,66,77]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))
