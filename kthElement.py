class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class kthElement:
    def __init__(self):
        self.root = None
        self.stack = []

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
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

    def find(self, root, k):
        if root is None:
            return
        self.find(root.left, k)
        self.stack.append(root.data)
        print(root.data, end=" " if root else "")
        self.find(root.right, k)
        if k < len(self.stack):
            return self.stack[k-1]
        else:
            return None


res = kthElement()
res.add(5)
res.add(1)
res.add(7)
res.add(9)
res.add(11)
res.add(20)

k = res.find(res.root, 3)
print()
print(k)
