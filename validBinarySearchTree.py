class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class vbst:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self._add(self.root, data)

    def _add(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._add(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._add(root.right, data)

    def validate(self, root, min_val=float('-inf'), max_val=float('inf')):
        if root is None:
            return True
        if root.data <= min_val or root.data >= max_val:
            return False

        # Recursively validate left and right subtrees with updated constraints
        return (
            self.validate(root.left, min_val, root.data) and
            self.validate(root.right, root.data, max_val)
        )

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)


res = vbst()
# Add nodes manually to enforce structure violating BST property
res.root = Node(5)
res.root.left = Node(1)
# Violates BST properties because 4 < 5 but is on the right
res.root.right = Node(4)
res.root.right.left = Node(3)  # 3 should be on the left of 5, not 4
res.root.right.right = Node(6)

# Check inorder traversal and validation output
res.inorder(res.root)  # Should print: 1 3 4 5 6
print()  # For readability
print(res.validate(res.root))  # Should output: False
