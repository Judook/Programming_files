class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree :
    def __init__(self, root) :
        self.root = Node(root)

    def print_tree(self, traversal_type) :
        if traversal_type == "preorder" :
            return self.preorder_print(tree.root, "")
        
        elif traversal_type == "inorder" :
            return self.inorder_print(tree.root, "")
        
        elif traversal_type == "postorder" :
            return self.postorder_print(tree.root, "")
        
        else :
            print("Traversal type", str(traversal_type), "is not supported!")
            return False

    def preorder_print(self, start, traversal) :
        # Root -> Left -> Right
        if start :
            traversal += str(start.data) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal) :
        # Left -> Root -> Right
        if start :
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.data) + "-"
            traversal = self.inorder_print(start.right, traversal) 
        return traversal
    
    def postorder_print(self, start, traversal) :
        # Left -> Right -> Root
        if start :
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.data) + "-"
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
tree.root.left.right.left = Node(10)
tree.root.left.right.right = Node(11)
tree.root.right.left.left = Node(12)
tree.root.right.left.right = Node(13)
tree.root.right.right.left = Node(14)
tree.root.right.right.right = Node(15)


# Tree :
#              1
#            /   \
#           /     \
#          /       \
#         /         \
#        2           3
#      /   \       /   \
#     4     5     6     7
#    / \   / \   / \   / \
#   8   9 10 11 12 13 14 15


print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
