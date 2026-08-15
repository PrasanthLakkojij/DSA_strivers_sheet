class Solution(object):
    def findMaxConsecutiveOnes(self,a):
        c=0
        d=0
        for i in range(len(a)):
            if(a[i]==0):
                c=0
            else:
                c=c+1 
            d=max(d,c)    
        return d