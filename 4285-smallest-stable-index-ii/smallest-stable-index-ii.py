class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        c=[nums[0]]
        for i in range(1, n):
            c.append(max(c[-1],nums[i]))
        d=[nums[-1]]
        for i in range(n-2,-1,-1):
            d.append(min(d[-1],nums[i]))
        d.reverse()
        for i in range(n):
            if c[i]-d[i]<= k:
                return i
        return -1
        