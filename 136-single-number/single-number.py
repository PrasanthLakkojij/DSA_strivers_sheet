class Solution(object):
    def singleNumber(self,a):
        r=0
        for i in a:
            r=r^i
        return r    
        
        
        