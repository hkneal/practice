class Node():

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class BinaryTree():
    # This BST ignores duplicate values

    def __init__(self):
        self.root = None

    def add_node_bst(self, value: int) -> str:
        # Adds a node, returns the root

        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return print(f"New Node inserted as Root, {self.root}")

        current_node = self.root

        while current_node is not None:
            if new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return print(f"New Node, {new_node} inserted as left child of {current_node}")
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    return print(f"New Node, {new_node} inserted as right child of {current_node}")


    def print_bst_inorder(self, node: Node):
        # Recusivly Print the BST DFS Inorder

        if node:
            self.print_bst_inorder(node.left)
            print(node)
            self.print_bst_inorder(node.right)

        else:
            # print(node)
            return







tree_nodes = [50,30,70,20,40,60,80]
my_tree = BinaryTree()
for value in tree_nodes:
    my_tree.add_node_bst(value)
my_tree.print_bst_inorder(my_tree.root)


x = 5
print([x for x in range(3)], end=',')
print(x)


    # Pre-Order Root -> Left -> Right
    # Post-Order Left -> Right -> Root
    # InOrder   Left -> Root -> Rightt
    # LevelOrder  Root -> Queue -> Left -> Right -> Deque -> repeat
