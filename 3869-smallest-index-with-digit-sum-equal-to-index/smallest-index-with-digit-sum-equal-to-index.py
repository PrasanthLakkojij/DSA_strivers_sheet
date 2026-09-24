class Solution(object):
    def smallestIndex(self,a):
        k=0
        for i in range(len(a)):
            c=a[i]
            d,b=0,0
            while(c>0):
                b=c%10
                d=d+b
                c=c//10 
            if(d==i):
                return i
        return(-1) 
