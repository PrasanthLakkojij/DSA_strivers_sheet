class Solution(object):
    def maxSubArray(self,a):
        b=a[0]
        c=0 
        for i in a:
            if (c<0):
                c=0
            c=c+i
            if (c>b):
                b=c
        return b