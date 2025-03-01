class Node():

    def __init__(self, data: str):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList():

    def __init__(self, node: Node = None):
        self.head = node or None


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return (" -> ").join(nodes)

    def add_first_node(self, data: str):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        else:
            new_node.next = self.head
            self.head = new_node

    def add_node(self, data: str):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        for node in self:
            if node.next == None:
                node.next = new_node
                return



my_llist = LinkedList()
print(my_llist)
node1 = Node("One")
node2 = Node("Two")
node3 = Node("Three")

my_llist.head = node1
node1.next = node2
node2.next = node3
print(my_llist)

my_llist.add_node("Four")
print(my_llist)

my_llist.add_first_node("Begin")
print(my_llist)

# my_llist.add_last("Five")
# my_llist.add_after("Six", "Five")
# my_llist.add_before("Five A", "Five")
# print(my_llist)

a,b = [3,4]
a = a*300
print(a, b)