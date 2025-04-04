"""Generate a balanced binary tree from a sorted list """


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        str_left = str(self.left.value)
        str_right = str(self.right.value)
        str_value = str(self.value)
        return "Value: " + str_value + " Left: " + str_left + " Right: " + str_right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, value: int):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self

        current_node = self.root
        while current_node.value != value:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    break
                current_node = current_node.left

            else:
                if not current_node.right:
                    current_node.right = new_node
                    break
                current_node = current_node.right


    def get_node(self, value: int) -> Node:
        if not self.root:
            return None

        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node

            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    return None

            else:
                if current_node.left:
                    current_node = current_node.left
                else:
                    return None


    # def print_bst(self, root, space=0, level_space=10):
    #     if root is None:
    #         return

    #     space += level_space
    #     self.print_bst(root.right, space, level_space)
    #     print(" " * (space - level_space) + str(root.value))
    #     self.print_bst(root.left, space, level_space)


tree_input = sorted([1, 3, 5, 20, 66, 79, 32, 12, 44, 30, 7, 67, 90])
print(tree_input)

n = len(tree_input)
tree = BinaryTree()

for _ in range(n):
    tree.insert_node(tree_input[(n-1) // 2])
    tree_input.pop(tree_input.index(tree_input[(n-1) // 2]))
    n = len(tree_input)

print(tree.get_node(31))


# tree.print_bst(tree.root)
# print(tree)