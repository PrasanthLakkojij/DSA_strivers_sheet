class Solution(object):
    def sortColors(self,a):
        l,m,r=0,0,len(a)-1
        i=0
        while(m<=r):
            if(a[m]==0):
                a[l],a[m]=a[m],a[l]
                l=l+1
                m=m+1
            elif(a[m]==1):
                m=m+1
            else:
                a[r],a[m]=a[m],a[r]
                r=r-1    
        
        