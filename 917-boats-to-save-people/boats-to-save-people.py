class Solution(object):
    def numRescueBoats(self,a,k):
        a.sort()
        l=0
        r=len(a)-1
        d=0
        while l<=r:
            if a[l]+a[r]<=k:
                l=l+1
            r=r-1
            d=d+1
        return d

         
        