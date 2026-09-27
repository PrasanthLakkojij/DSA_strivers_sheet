class Solution(object):
    def reverseParentheses(self, a):
        a=list(a)
        b=[]
        for i in range(len(a)):
            if a[i]=='(':
                b.append(i)
            elif a[i]==')':
                l=b.pop()
                a[l+1:i]=a[l+1:i][::-1]

        a="".join(a)
        a=a.replace("(","").replace(")","")
        return (a)