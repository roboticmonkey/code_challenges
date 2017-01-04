class Stack(object):

    #initialize an empty list
    def __init__(self):
        self.items = []


    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    #remove the last item
    def pop(self):

        #if the stack is empty return None
        if not self.items:
            return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None

        return self.items[-1]


class MaxStack(Stack):

    def __init__(self):

        self.stack = Stack()
        self.max_elements = Stack()

    #push a new item to the end of stack
    # if the new item is greater than or equal to the last item 
    # add to max_elements
    def push(self, item):
        self.stack.push(item)

        if self.max_elements.peek() == None or self.max_elements.peek() <= item:
            self.max_elements.push(item)

    def pop(self):
        # remove last item
        item = self.stack.pop()

        if item == self.max_elements.peek():
            self.max_elements.pop()

        return item


    #returns the max stack, does not remove the items
    def get_max(self):

        return self.max_element.peek()

