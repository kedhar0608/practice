#merge sorting

def mergesort(array):
    if len(array)>1:

        r=len(array)//2
        L= array[:r]
        M= array[r:]

        mergesort(L)
        mergesort(M)

        i=j=k=0

        while i<len(L) and j < len(M):
            if L[i] < M [j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j +=1
            k +=1

        while  i <len(L):
            array[k]= L[i]
            i +=1
            k +=1
        while j< len(M):
            array[k]=M[j]
            j +=1
            k+=1

array=[1,3,5,6,78,9,90,10,6,7,91,101,67]

mergesort(array)

print(array)
            
        
            
                

        

            
            
