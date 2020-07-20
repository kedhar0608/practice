#bubble sorting
arr=[4,1,5,3]
l=len(arr)
for i in range(l):
    for j in range(l-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)
            
            
