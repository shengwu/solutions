# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        turtle = head
        rabbit = head
        while turtle is not None and rabbit is not None:
            turtle_advanced = False
            if turtle is not None:
                turtle_advanced = True
                turtle = turtle.next
            if rabbit is not None and rabbit.next is not None:
                rabbit = rabbit.next.next
            elif turtle_advanced:
                return False
            if turtle is not None and turtle == rabbit:
                return True
        return False


s = Solution()

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
assert not s.hasCycle(a)

b = ListNode(1)
b.next = b
assert s.hasCycle(b)

c = ListNode(1)
c.next = ListNode(2)
c.next.next = c
assert s.hasCycle(c)

d = ListNode(1)
d.next = ListNode(2)
d.next.next = ListNode(3)
d.next.next.next = d
assert s.hasCycle(d)

e = ListNode(1)
assert not s.hasCycle(e)

f = ListNode(1)
f.next = ListNode(10)
assert not s.hasCycle(f)

assert not s.hasCycle(None)

g = ListNode(1)
g.next = ListNode(2)
g.next.next = ListNode(3)
g.next.next.next = ListNode(4)
g.next.next.next.next = ListNode(5)
g.next.next.next.next.next = ListNode(6)
g.next.next.next.next.next.next = ListNode(7)
g.next.next.next.next.next.next.next = g
assert s.hasCycle(g)

h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
h.next.next.next.next.next = ListNode(6)
h.next.next.next.next.next.next = ListNode(7)
h.next.next.next.next.next.next.next = ListNode(8)
assert not s.hasCycle(h)
