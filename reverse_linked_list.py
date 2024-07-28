class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        prev, curr, tmp = None, head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

if __name__ == '__main__':

    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    solution = Solution()
    reversed_head = solution.reverseList(node1)

    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next
