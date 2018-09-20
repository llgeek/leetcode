"""
very elegant solution

Use three pointers. The operation is similar to Leetcode#92 Reverse Linked List II.
The pointer n will go k steps further.
(If there are no k nodes further, it means we don't have to reverse these k nodes. ==> Stop. )
The pointer p is always at the fixed position in this for-loop.
The pointer c = p.next, which means the current node we want to move.
The pointer start means the starting node for the next loop.
Dummy -> 1 -> 2 -> 3 -> 4 -> 5
   p     c         n
         start
Dummy -> 2 -> 3 -> 1 -> 4 -> 5
   p     c    n    start
Dummy -> 3 -> 2 -> 1 -> 4 -> 5
   p     c         start
         n

https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11413/Share-my-Java-Solution-with-comments-in-line
"""

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
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while True:
            prev = start
            cur = prev.next
            tail = cur
            start = start.next
            for i in range(k-1):
                if not tail:
                    return dummy.next
                tail = tail.next
            if not tail:
                break
            for i in range(k-1):
                cur = prev.next
                prev.next = cur.next
                cur.next = tail.next
                tail.next = cur
        return dummy.next
            



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
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    head = buildList(array)
    reshead = Solution().reverseKGroup(head, k)
    print(listToArray(reshead))
