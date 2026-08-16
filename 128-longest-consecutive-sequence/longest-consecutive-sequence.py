class Solution(object):
    def longestConsecutive(self,a):
        a=set(a)
        p=0
        for i in a:
            if(i-1 not in a):
                k=i
                c=0
                while(k in a):
                    c=c+1
                    k=k+1
                p=max(p,c)
        return (p)            
        