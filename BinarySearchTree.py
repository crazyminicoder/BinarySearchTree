class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, root, val):
        if val < root.data:
            if root.left is None:
                root.left = Node(val)
            else:
                self._insert(root.left, val)
        else:
            if root.right is None:
                root.right = Node(val)
            else:
                self._insert(root.right, val)

    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preOrder(self, root):
        if root:
            print(root.data, end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data, end=' ')


bt = BinarySearchTree()

bt.insert(50)
bt.insert(25)
bt.insert(10)
bt.insert(55)
bt.insert(67)
bt.insert(2)
bt.insert(36)
bt.insert(41)

print("Inorder:", end='\n')
bt.inorder(bt.root)

print("\n")
print('Preorder:', end="\n")
bt.preOrder(bt.root)

print("\n")
print('PostOrder:', end="\n")
bt.postOrder(bt.root)
