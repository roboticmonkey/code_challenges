class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def second_largest(root):

    node_stack = [root]
    max_element = 0
    almost_max = 0


    while node_stack:

        #retrive node from stack
        node = node_stack.pop()

        #check if new max or almost max
        if node.value > max_element:
            almost_max = max_element
            max_element = node.value
        else:
            if node.value > almost_max:
                almost_max = node.value

        if node.left:
            node_stack.append(node.left)

        if node.right:
            node_stack.append(node.right)

    return almost_max

tree = BinaryTreeNode(50)
tree.insert_left(30)
tree.insert_right(60)
tree.left.insert_left(20)
tree.left.insert_right(32)
tree.right.insert_right(80)
tree.right.insert_left(55)

print second_largest(tree)

tree2 = BinaryTreeNode(50)
tree2.insert_left(30)
tree2.insert_right(60)
tree2.left.insert_left(20)
tree2.left.insert_right(32)

print second_largest(tree2)

tree3 = BinaryTreeNode(50)
tree3.insert_left(30)
tree3.left.insert_left(20)
tree3.left.insert_right(32)

print second_largest(tree3)

