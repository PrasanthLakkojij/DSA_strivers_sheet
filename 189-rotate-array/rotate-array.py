class Solution(object):
    def rotate(self,a,k):
        i=k%len(a)
        a.reverse()
        a[:i]=reversed(a[:i])
        a[i:]=reversed(a[i:])
        return (a)
        
        