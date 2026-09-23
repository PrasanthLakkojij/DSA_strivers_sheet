class Solution(object):
    def findPeakGrid(self,a):
        l=0
        r=len(a[0])-1
        while(l<=r):
            m=(l+r)//2
            c,k=0,0
            for i in range(len(a)):
                if a[i][m] > c:
                    c=a[i][m]
                    k=i
            lt=a[k][m-1] if m>0 else -1
            rt=a[k][m+1] if m<len(a[0])-1 else -1
            if(lt<=c>=rt):
                return([k,m])
            elif(c<rt):
                l=m+1
            else:
                r=m-1
        return-1        