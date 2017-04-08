f=open('A-small-practice.in','r')
numCase=int(f.readline())
output_File="Output.in"
output=open(output_File,'w')
k=0
for line in f:
    smax,string=line.split()
    #print smax
    #print string
    k=k+1
    t=0
    minInv=0
    for i in range(int(smax)+1):
        minInv=max(minInv,i-t)
        t+=int(string[i])
    #print "numCase %d" %(k) "minInv %d" %(minInv)   
    output.write("Case #%d: %d \n" % (k, minInv))
	