arr=[10,12,15,19,21,56,100]
arr.sort()
x=100
temp=-1
print(arr)
l=0
r=len(arr)-1
mid=0
while(mid>=0 and mid<len(arr)-1):
        if r>=0:
                mid=(l+r)//2
                if arr[mid]==x:
                        print(mid)
                        temp=0
                        break
                elif x<arr[mid]:
                        r=mid-1
                elif x>arr[mid]:
                        l=mid+1
if temp==-1:
        print("element is not in the array")
        
               
        
        
                        
                        
        
                        
                        
                
                
                
                        
        


