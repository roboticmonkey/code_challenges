class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head_node):

    current_node = head_node
    
    past_node = None
    future_node = None
    

    while current_node:
        
        #move future_node to next node
        future_node = current_node.next
        #reverse current_node.next 
        current_node.next = past_node
        #move past_node to current_node
        past_node = current_node
        #move current_node to next node
        current_node = future_node



    return past_node

def reverse_out_place(head_node):

    current = head_node

    new_head = None

    while current:
        print current, current.value
        #copy the current node
        copy_node = LinkedListNode(current.value)
        print copy_node, copy_node.value
        #point the copy_node.next to new_head
        copy_node.next = new_head
        # point new_head to the newly made node
        new_head = copy_node
        # move current to next node
        current = current.next

    # print head_node, head_node.value
    # print new_head, new_head.value
    
    return new_head.value


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)
e = LinkedListNode(5)
f = LinkedListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# print reverse_list(a)
print reverse_out_place(a)

one = LinkedListNode(2)

print reverse_list(one)