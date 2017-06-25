def numDigOne(n):
    if n<=0:
       ans=0
    newNum=n
    ans=0
    x=0
    while newNum>0:
        digit = newNum%10
        if digit==1:
            ans+=ans
            
    