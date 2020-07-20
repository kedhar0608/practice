#insertion sorting
arr=[4,1,5,3,2,6,8,7,9,0,-8,32,67]
l=len(arr)
for i in range(l):
    key=arr[i]
    j=i-1
    while(j>=0 and key<arr[j]):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print(arr)
            
            
