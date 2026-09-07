class Solution(object):
    def splitArray(self,a,k):
        l=max(a)
        r=sum(a)
        while(l<=r):
            m=(l+r)//2
            c=0
            p=1
            for i in a:
                if(c+i<=m):
                    c=c+i
                else:  
                    p=p+1
                    c=i
            if(p<=k):
                r=m-1
            else:
                l=m+1
        return (l) 
        