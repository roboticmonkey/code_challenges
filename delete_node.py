class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(node_to_delete):
    
    #this is so dumb. it works, but could cause many bugs
    #depending on what is pointing to where you could have a 
    #node that you cant get to or another part of the program
    #expecting a value that has been over written.
    
    next_node = node_to_delete.next
    
    if next_node:

        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next

    else:
        raise Exception("cant delete the last node with this method.")

a = LinkedListNode("A")
b = LinkedListNode("B")
c = LinkedListNode("C")

a.next = b
b.next = c

delete_node(b)