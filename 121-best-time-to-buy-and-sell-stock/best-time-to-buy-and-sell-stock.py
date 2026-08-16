class Solution(object):
    def maxProfit(self,a):
        c,d=a[0],0
        for i in range(1,len(a)):
            c=min(c,a[i])
            d=max(d,a[i]-c)
        return d    
        