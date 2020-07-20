#quick sorting
arr=[4,1,5,3,2,6,8,7,9,10,13,17,21,34,-1,-5,0,-34]
l=len(arr)
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
         if pivot>=array[j]:
             i=i+1
             (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array, low, high):
    if low<high:

        pi=partition(array,low,high)

        quicksort(array,low,pi-1)

        quicksort(array,pi+1,high)

quicksort(arr,0,l-1)

print(arr)


            
            
