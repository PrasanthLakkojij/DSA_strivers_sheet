class Solution(object):
    def moveZeroes(self,a):
        l=0
        for i in range(len(a)):
            if(a[i]!=0):
                a[l],a[i]=a[i],a[l]
                l=l+1
        return a