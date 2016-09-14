class BinaryTreeNode(object):

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


def is_binary_search_tree(node):

    if node.left:

        if node.left.value < node.value:
            return True

        else:
            return is_binary_search_tree(node.left)

    
    if node.right:
        
        if node.right.value > node.value:
            return True

        else:
            return is_binary_search_tree(node.right)

    return False



tree = BinaryTreeNode(50)
tree.insert_left(25)
tree.insert_right(75)
tree.left.insert_left(12)
tree.left.insert_right(37)
tree.right.insert_left(62)
tree.right.insert_right(88)


tree2 = BinaryTreeNode(50)
tree2.insert_left(25)
tree2.insert_right(13)
tree2.left.insert_left(12)
tree2.left.insert_right(20)
tree2.right.insert_left(62)
tree2.right.insert_right(88)
print tree2.right.value

print is_binary_search_tree(tree)

print is_binary_search_tree(tree2)

