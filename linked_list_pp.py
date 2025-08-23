class Node:
    def __init__(self, data: str) -> object:
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_last_node(self) -> Node:
        if self.head is None:
            return None

        for node in self:
            if not node.next:
                return node

    def add_node(self, data: str) -> None:
        new_node = Node(data)
        node = self.get_last_node()
        if node is None:
            self.head = new_node
        else:
            node.next = new_node

    def add_after(self, target: str, data: str) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        for node in self:
            if node.data == target:
                node.next = new_node
                return

        raise Exception("Node with target data not found")



    def search(self, target: str) -> Node:
        if self.head is None:
            raise Exception("LinkedList is Empty")

        for node in self:
            if node.data == target:
                return node
        raise Exception("Target Data Not Found")


my_llist = LinkedList()
node1 = Node("One")
node2 = Node("Two")
node3 = Node("Three")

my_llist.head = node1
node1.next = node2
node2.next = node3

my_llist.add_node("Four")
# my_llist.add_last("Five")
# my_llist.add_after("Six", "Five")
# my_llist.add_before("Five A", "Five")
print(my_llist)

my_llist2 = LinkedList()
my_llist2.add_node("One")
print(my_llist2)


