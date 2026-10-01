# class Solution(object):
#     def minCostClimbingStairs(self,a):
#         if(len(a)%2!=0):
#             a=a+[0]
#         dp=[0]*(len(a)+1)
#         for i in range(len(a)-1,-1,-1):
#             x=a[i]+dp[i+1]
#             y=float('inf')
#             if(i+1<len(a)):
#                 y=a[i+1]+dp[i+2]
#             dp[i]=min(x,y)
#         return(dp[0]) 
        
class Solution(object):
    def minCostClimbingStairs(self,a):
        n=len(a)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            x=a[i]+dp[i+1]
            y=float('inf')
            if i+2<=n:
                y=a[i]+dp[i+2]
            dp[i]=min(x,y)
        return min(dp[0],dp[1])     