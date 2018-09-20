# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        from collections import deque
        stack = deque()
        stepsize = k - 1
        temphead = ListNode(0)
        temphead.next = head
        curnode = temphead.next
        prevnode = temphead
        firstime = True
        stepsize = k-1
        while curnode:
            if not stack:
                if not firstime:
                    for i in range((k+1)//2):
                        if not curnode:
                            return temphead.next
                        prevnode = prevnode.next
                        curnode = curnode.next
                nextnode = curnode
                for i in range((k+1)//2):
                    if not nextnode:
                        return temphead.next
                    nextnode = nextnode.next
                for i in range(k//2):
                    if not nextnode:
                        return temphead.next
                    stack.append(nextnode)
                    nextnode = nextnode.next
                firstime = False
                stepsize = k-1
            if not stack:
                return temphead.next
            nextnode = stack.pop()
            prevnode.next = nextnode
            tmpnextnode = nextnode.next
            nextnode.next = curnode.next
            curnode.next = tmpnextnode
            stepsize -= 2
            if stack:
                stack[-1].next = curnode
            else:
                if stepsize != 0:
                    nextnode.next = curnode
                else:
                    nextnode.next.next = curnode
            prevnode = prevnode.next
            curnode = prevnode.next
        return temphead.next


def buildList(array):
    tmpnode = ListNode(0)
    curnode = tmpnode
    for val in array:
        curnode.next = ListNode(val)
        curnode = curnode.next
    return tmpnode.next

def listToArray(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    k = 4
    head = buildList(array)
    reshead = Solution().reverseKGroup(head, k)
    print(listToArray(reshead))
