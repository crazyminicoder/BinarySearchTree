class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self, root):
        if root is None:
            return True
        else:
            return False

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

    def findMin(self, root):
        if self.isEmpty(root):
            return
        temp = root
        while temp.left is not None:
            temp = temp.left

        print('The minimum value in the tree is:', temp.data)

    def findMax(self, root):
        if root is None:
            print('Tree is empty')
            return
        temp = root
        while temp.right is not None:
            temp = temp.right

        print('The maximum value in tree is:', temp.data)

    def findHeight(self, root):
        countLeft = 0
        countRight = 0

        temp1 = root
        temp2 = root
        while temp1.left is not None:
            temp1 = temp1.left
            countLeft += 1

        while temp2.right is not None:
            temp2 = temp2.right
            countRight += 1

        print("The height of the tree is:", max(countLeft, countRight))

    def search(self, root, key):
        if self.root is None:
            print("The tree is empty")
        else:
            self._search(root, key)

    def _search(self, root, key):
        if root is None:
            print("Key not found")
            return
        if root.data == key:
            print("Key found")
            return
        elif key < root.data:
            self._search(root.left, key)
        else:
            self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.data:
            root.left = self._delete(root.left, key)

        elif key > root.data:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children:
            # Get the inorder successor (smallest in the right subtree)
            temp = self._minValuenode(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self._delete(root.right, temp.data)

        return root

    def _minValueNode(self, node):
        current = node
        # Loop to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current


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

print("\n")
bt.findMin(bt.root)
bt.findMax(bt.root)

bt.findHeight(bt.root)

bt.search(bt.root, 2)

bt.delete(67)

bt.inorder(bt.root)
