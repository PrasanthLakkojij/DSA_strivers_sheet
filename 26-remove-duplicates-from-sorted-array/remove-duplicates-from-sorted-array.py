class Solution(object):
    def removeDuplicates(self,a):
        l,r=0,1
        while(r<len(a)):
            if(a[l]!=a[r]):
                l=l+1
                a[l]=a[r]
            r=r+1  
        return l+1