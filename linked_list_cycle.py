class LinkedListNode(object):

    def __init__(self, value):

        self.value = value
        self.next = None


def contains_cycle(first_node):

    # seen_nodes = set()

    # current_node = first_node

    # while current_node.next:
    #     seen_nodes.add(current_node)
    #     current_node = current_node.next

    #     if current_node in seen_nodes:
    #         return True

    # return False
    slow_runner = first_node
    fast_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner == slow_runner:
            return True

    return False
    

a = LinkedListNode("A")
b = LinkedListNode("B")
c = LinkedListNode("C")

a.next = b
b.next = c
c.next = a

print contains_cycle(a)

a = LinkedListNode("A")
b = LinkedListNode("B")
c = LinkedListNode("C")

a.next = b
b.next = c


print contains_cycle(a)

a = LinkedListNode("A")
b = LinkedListNode("B")
c = LinkedListNode("C")
d = LinkedListNode("C")
e = LinkedListNode("C")
f = LinkedListNode("C")


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = c

print contains_cycle(a)
