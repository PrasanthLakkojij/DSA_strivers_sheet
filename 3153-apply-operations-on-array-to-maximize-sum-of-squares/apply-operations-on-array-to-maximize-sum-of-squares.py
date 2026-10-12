class Solution(object):
    def maxSum(self, nums, k):
        a=[0]*32
        for i in nums:
            for j in range(32):
                if i>>j&1:
                    a[j]+=1
        s=0
        for i in range(k):
            b=0
            for j in range(32):
                if a[j]:
                    b|=1<<j
                    a[j]-=1
            s+=b*b
        return s%(10**9 +7)
        