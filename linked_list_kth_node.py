class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None



def kth_node_from_end(number, head_node):
    # set 2 pointers to head
    p1 = head_node
    p2 = head_node

   
    # if possible move p1 forward number of nodes
    for step in xrange(number):
        # print p1.value
        if p1.next:
            p1 = p1.next
            
        else:
            raise ValueError("number is bigger than length of list")

    # move p1 and p2 at the same time until p1 falls off the list
    while p1:
        # print p1.value
        p1 = p1.next
        
        p2 = p2.next

    #return p2 nodes
    return p2.value


def kth_node_checkpoints(number, head_node):

    current = head_node
    checkpoint = None
    list_index = 1

    checkpoint1 = None
    checkpoint2 = None
    if number < 1:
        raise ValueError("cant find less than first node")

    #go through list, get length and set 2 checkpoints
    while current.next:
        #move pointer 1 node
        print current.value
        current = current.next
        # increment index
        list_index += 1

        #set checkpoint 
        if list_index % number == 0:
            #checkpoint1 not None
            if checkpoint1:
                checkpoint2 = checkpoint1
                checkpoint1 = current
            else:
                checkpoint1 = current

    if number > list_index:
        raise ValueError("number is bigger than lenght of list")
    

    print checkpoint1.value
    print checkpoint2.value
    #find index of requested node
    element_idx = (list_index - number) + 1
    print element_idx
    # find # of steps from nearest checkpoint
    steps = element_idx % number
    print steps
    if steps == 0:
        return checkpoint1.value
    
    else:
        node = checkpoint2
        for step in xrange(steps):

            node = node.next

        return node.value




a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# print kth_node_from_end(4, a)



big_num = 41
idx = 1
head = LinkedListNode(idx)
pointer = head

for i in xrange(2,big_num+1):
    n = LinkedListNode(i)
    pointer.next = n 
    pointer = n

print head.value

print kth_node_checkpoints(4, head)