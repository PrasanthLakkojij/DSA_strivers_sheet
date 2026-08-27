class Solution(object):
    def findUnsortedSubarray(self,a):
        c=0
        l,h=0,0
        if len(a) <= 1:
            return 0
        for i in range(1,len(a)):
            if(a[i-1]>a[i]):
                l=i-1
                break
        if(l==0 and a[0]<=a[1]):
            return 0        
        for i in range(len(a)-1,0,-1):
            if(a[i-1]>a[i]):
                h=i
                break
        mn=min(a[l:h+1])
        mx=max(a[l:h+1])
        while l>0 and a[l-1]>mn:
            l-=1
        while h<len(a)-1 and a[h+1]<mx:
            h+=1
        return h-l+1

        
        