class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def sum_values(self):
            return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        return node.val + self._sum_values(node.left) + self._sum_values(node.right)


# Створення екземпляру двійкового дерева пошуку
bst = BinarySearchTree()

# Вставка значень
bst.insert(200)
bst.insert(100)
bst.insert(130)
bst.insert(25)
bst.insert(185)
bst.insert(325)
bst.insert(35)

# Знаходження найменшого значення
print("Найбільше значення у дереві:", bst.sum_values())
