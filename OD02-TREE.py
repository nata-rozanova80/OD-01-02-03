class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        return self.right

# # Пример использования:
# root = TreeNode(10)
# left_child = root.insert_left(5)
# right_child = root.insert_right(15)
#
# # Вставка поддеревьев
# left_child.insert_left(3)
# left_child.insert_right(7)

def find_value(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    return find_value(node.left, target) or find_value(node.right, target)

# Пример использования:
root = TreeNode(10)
root.insert_left(5).insert_right(7)
root.insert_right(15).insert_left(12)

print(find_value(root, 7))   # True
print(find_value(root, 20))  # False
