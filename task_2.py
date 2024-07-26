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

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.val


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
print("Найбільше значення у дереві:", bst.find_min())
