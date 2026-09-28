class Solution(object):
    def maxDepth(self, s):
        k,c=0,0
        for i in s:
            if(i=='('):
                c=c+1
                k=max(k,c)
            elif(i==')'):
                c=c-1
        return k            
        