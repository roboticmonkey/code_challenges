class QueueTwoStacks(object):

    def __init__(self):

        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):

        if len(self.out_stack) == 0:
            #move items from in_stack to out_stack

            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            #if out_stack is still empty raise error
            if len(self.out_stack) == 0:
                raise IndexError("Cant dequeue from empty queue.")


        return self.out_stack.pop()


