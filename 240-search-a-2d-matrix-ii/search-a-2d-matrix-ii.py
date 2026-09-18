class Solution(object):
    def searchMatrix(self,matrix,target):
        a=0
        b=len(matrix[0])-1
        c=len(matrix)
        d=len(matrix[0])
        while a<c and b>=0:
            if matrix[a][b]==target:
                return True
            elif matrix[a][b]>target:
                b-=1
            else:
                a+=1
        return False
        