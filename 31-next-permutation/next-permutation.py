class Solution(object):
    def nextPermutation(self,a):
        c=-1
        for i in range(len(a)-2,-1,-1):
            if(a[i]<a[i+1]):
                c=i
                break
        if(c==-1):
            a.reverse()
            return (a)
            exit()
        for i in range(len(a)-1,c,-1):
            if(a[c]<a[i]):
                a[i],a[c]=a[c],a[i]
                break
        a[c+1:]=reversed(a[c+1:])
        return (a)
        
        