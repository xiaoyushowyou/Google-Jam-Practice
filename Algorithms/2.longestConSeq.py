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

#Threesum probelm
#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#Note: Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c) The solution set must not contain duplicate triplets.
#Improvement: whether it equals to a certain number 

class solution:
    def threeSum(myArray,target):
        numElm=len(myArray)       
        
        if numElm<3:
            return 0
        
        for i in range(numElm):
            for j in range(i+1,numElm):
                
                temp=int(target-myArray[i]-myArray[j])
                if temp in myArray:
                    return myArray[i],myArray[j],temp
                    
    myArray=[1,2,3,4,5]
    target=9
    
    print(threeSum(myArray,target))
                    
        


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

#We can use numpy package to create multiple dimention matrix
class solution:
    def PascalTri(numR):
        sol=[]
        sol.append([1])
        sol.append([1,1])
        print (sol)
        for i in range(2,numR):
            temp=[]
            temp.append(1)
            print (i,temp)
            for j in range(1,i):
                temp.append(sol[i-1][j-1]+sol[i-1][j])
                print (temp)
            temp.append(1)
            print (temp)
            sol.append(temp)
        print (sol)
        
    #PascalTri(5)

    
    
 #_________________________________________________________________
# Given an index k, return the kth row of the Pascal's triangle.
# For example, given k = 3, Return [1,3,3,1].
# Due to the limitation to space, O(n), we can only create one dimentional metrix

class solution:
    def PascalTri2(numR):
        sol=[1,1]
        if numR==1:
            return [1]
        elif numR==2:
            return [1,1]
        else:
            for i in range(3,numR+1):
                temp=[]
                temp.append(1)
                for j in range(1,i-1):                    
                    temp.append(sol[j-1]+sol[j])
                temp.append(1)
                sol=temp
            return sol
    #print(PascalTri2(5))