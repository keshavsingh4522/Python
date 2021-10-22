def mergeArray(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    arr4=[]
    i=0
    j=0
    k=0
    
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            arr4.append(arr1[i])
            i=i+1
        else:
            arr4.append(arr2[j])
            j=j+1
    while i<n1:
        arr4.append(arr1[i])
        i=i+1
        
    while j<n2:
        arr4.append(arr2[j])
        j=j+1
    return arr4
def merge(arr1,arr2,arr3):
    arr=[]
    arr=mergeArray(arr1,arr2)
    return mergeArray(arr,arr3)

arr1=[1,4,7,10]
arr2=[2,5,8]
arr3=[3,6,9]
print(merge(arr1,arr2,arr3))
