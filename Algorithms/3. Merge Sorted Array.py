#Given two sorted integer arrays A and B, merge B into A as one sorted array.

class solution:
    def mergeSA(A,B):
        numA=len(A)-1
        numB=len(B)-1
        numT=len(A)+len(B)-1 
        
        for i in range (numA,numT):
            A.append(0)
            print (A)
                    
        while numT>=0:
            print (numT,numA,numB)
            if (numA>=0 and numB>=0):
                print (numA)
                if (A[numA]>B[numB]):
                    A[numT]=A[numA]
                    numA-=1
                else:
                    A[numT]=B[numB]
                    numB-=1
                numT-=1
            
            elif (numA<0):
                A[numT]=B[numB]
                numB-=1
                numT-=1
                
            else:
                A[numT]=A[numA]
                numA-=1
                numT-=1
            
        return A
                    
            
    A=[1,2,3,7]
    B=[4,5,6]
    
    print(mergeSA(A,B))
        