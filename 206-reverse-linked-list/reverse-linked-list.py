class Solution(object):
    def reverseList(self,head):
        global h
        h=head
        def b(i,p):
            global h
            if i==None:
                return
            if i.next==None:
                i.next=p
                h=i
                return
            b(i.next,i)
            i.next=p
        b(head,None)
        return h      