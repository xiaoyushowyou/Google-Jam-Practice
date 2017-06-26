#Longest consecutive sequence (quick array, o(nlogn))
#[100, 4, 200, 1, 3, 2] and the consecutive elements is going to be [1,2,3,4]
#In order to achieve it, need to use Hash Table
#import set

class solution:
    def longConSeq (self,myArray):
        numA=len(myArray)
        myHS=set()
        
        for ele in myArray:
            myHS.add(ele)
        
        ans=0
        for i in range(numA):
            if (myArray[i]-1) not in myHS:
                j = myArray[i]
                cuLength=1
                while ((j+1) in myHS):
                    cuLength+=1
                    j+=1
                
                if cuLength>=ans:
                    ans=cuLength
                    arrSol=list(range(j-cuLength+1,j+1))
               
        print (ans,arrSol)
        
        
        
    #myArray=[1,5,2,3,4,7,9]
    #longConSeq(self,myArray)
       
       
#twosum probelm
#Given an array of integers, find two numbers such that they add up to a specific target number.
#You may assume that each input would have exactly one solution.
#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

class solution:
    def twoSum (self,numbers,target):
        numA=len(numbers)
        myDic={}
        
        for i in range(numA):
            myDic[numbers[i]]=i
        print (myDic)
        
        if numA<=1:
            return 0,0
        
        for ele in numbers:
            mySub=target-ele
            index=myDic[ele]
            
            if mySub in myDic:
                if (index==myDic[mySub]):
                    continue
                elif (index<myDic[mySub]):
                    return index+1,myDic[mySub]+1
                else:
                    return myDic[mySub]+1,index+1
    #numbers=[1,2,3,4,5]
    #target=5  
    #print(twoSum(self,numbers,target))
        
#----------------------------------------------------------------------------#
# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5, Return

# [
     # [1],
    # [1,1],
   # [1,2,1],
  # [1,3,3,1],
 # [1,4,6,4,1]
# ]

class solution:
    def PascalTri(self,numR):
    
    sol={}
    for i range(numR):
        sol[i]=[]
    
    print (sol)
    
    PascalTri(self,5)
        