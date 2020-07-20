#insertion sorting
arr=[4,1,5,3]
l=len(arr)
for i in range(l):
    key=arr[i]
    j=i-1
    while(j>0):
        if key<arr[j]:
            arr.insert(j,key)
        j=j-1
            

print(arr)
            
            
