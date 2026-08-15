class Solution(object):
    def majorityElement(self,a):
        c=1
        v=a[0]
        for i in range(1,len(a)):
            if(a[i]==v):
                c=c+1
            else:
                c=c-1
            if(c==0):
                v=a[i]
                c=1      
        c=0
        for j in range(len(a)):
            if(a[j]==v):
                c=c+1
        if(c>len(a)//2):
              return v
    
    
        
        