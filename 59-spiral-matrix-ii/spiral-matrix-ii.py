class Solution(object):
    def generateMatrix(self, n):
        a=[[0]*n for _ in range(n)]
        k=1
        i=0
        while(i<=n//2):
            for j in range(i,n-i):
                a[i][j]=k
                k=k+1
            for j in range(i+1,n-i):
                a[j][n-1-i]=k
                k=k+1
            for j in range(i+1,n-i):
                a[n-1-i][n-1-j]=k
                k=k+1
            for j in range(i+1,n-1-i):
                a[n-1-j][i]=k
                k=k+1
            i=i+1
        return a     
        