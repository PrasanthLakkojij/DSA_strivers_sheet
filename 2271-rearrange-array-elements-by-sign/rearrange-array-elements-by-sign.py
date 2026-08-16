class Solution(object):
    def rearrangeArray(self,a):
        b=[0]*len(a)
        l,r=0,1
        for i in a:
            if(i>0):
                b[l]=i
                l=l+2
            else:
                b[r]=i
                r=r+2 
        return b