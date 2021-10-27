# 二叉树


class Node(object):
    def __init__(self, value, lchild=None, rchild=None) -> None:
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self, root=None):
        self.root = root

     # node in-order traversal(LDR)
    def traversal(self):
        self._traversal(self.root)

    # insert node
    def insert(self, value):
        self.root = self._insert(self.root, value)

    # delete node
    def delete(self, value):
        self.root = self._delete(self.root, value)

    # node in-order traversal(LDR)
    def _traversal(self, node):
        if not node:
            return
        self._traversal(node.lchild)
        print(node.value, end=' ')
        self._traversal(node.rchild)

    # insert node
    def _insert(self, root:Node, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.lchild = self._insert(root.lchild, value)
        elif value > root.value:
            root.rchild = self._insert(root.rchild, value)
        return root

    # delete node
    def _delete(self, root, value):
        if not root:
            return None
        if value < root.value:
            root.lchild = self._delete(root.lchild, value)
        elif value > root.value:
            root.rchild = self._delete(root.rchild, value)
        else:
            if root.lchild and root.rchild:  # degree of the node is 2
                target = root.lchild  # find the maximum node of the left subtree
                while target.rchild:
                    target = target.rchild
                root = self._delete(root, target.value)
                root.value = target.value
            else:  # degree of the node is [0|1]
                root = root.lchild if root.lchild else root.rchild
        return root


tr = Tree()

tr.insert(34)
tr.insert(23)
tr.insert(50)
tr.insert(36)
tr.insert(25)
tr.insert(54)
tr.insert(22)
tr.insert(98)
tr.traversal()
