class Solution(object):
    def maxNumberOfFamilies(self, n,a):
        b={}
        k=[1,2,3,4,5,6,7,8,9,10]
        c = 0
        for i, j in a:
            if i not in b:
                b[i] = []
            b[i].append(j)
        for i in b:
            b[i] = [x for x in k if x not in b[i]]
        for i, j in b.items():
            if all(x in j for x in [2,3,4,5]) and all(x in j for x in [6,7,8,9]):
                c += 2
            elif (all(x in j for x in [2,3,4,5]) or all(x in j for x in [4,5,6,7]) or all(x in j for x in [6,7,8,9])):
                c += 1
        c+=(n-len(b))*2
        return c