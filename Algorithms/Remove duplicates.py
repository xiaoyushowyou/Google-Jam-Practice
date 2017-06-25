#sorted array, need to return the element inside the array in place
class solution:
    def removeDump(self,A):
        index=1
        
        if len(A)==0:
            return 0    
        
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                index=index+1
                A[index-1]=A[i]
        return index
        
        #print (index)
        #print (A[0:index])

    A=[1,1,2,2,3]

    # index=removeDump(self,A)
    # print (index)
    # print (A[0:index])
    
    
#sorted array, need to return the element that appears less or equal to 2 times
class solution:
    def removeDump2(self,A):
        index=2
        newArray=[]
        
        if len(A)==0:
            return A,0
            
        for i in range(2,len(A)):
            if A[i]!=A[i-2]:
                index=index+1
                A[index-1]=A[i]
        return A,index
        
    A=[1,1,2,2,2,3]

    # A,index=removeDump2(self,A)
    # print (index)
    # print (A[0:index])  
    

#unsorted array, need to return the elements
class solution:
    def unSor(self,A):
        if (len(A)==0):
            return A,0
        
        index=1
        for i in range(1,len(A)):
            if A[i] in A[0:index]:
                continue
            else:
                index=index+1
                A[index-1]=A[i]
        return A,index
    
    #A=[1,4,2,2,2,3]

    # A,index=unSor(self,A)
    # print (index)
    # print (A[0:index])  
    
#non-negative number, represented as an arracy of digits. Plus one number and get the result
#A is [int]
class solution:
    def digitAdd(self,A):
        numb=0
        for i in range(0,len(A)):
            numb=numb+A[i]*(10**(i))
        return numb   
        
    A=[9,9,9,9]
    numb=digitAdd(self,A)+1
    
    print (numb)
        