class Node:
    def __init__(self, data) -> object:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return (" -> ").join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get_last_node(self) -> Node:
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def add_node(self, data: str) -> None:
        new_node = Node(data)
        last_node = self.get_last_node()
        last_node.next = new_node

    def remove_node(self, data: str) -> None:
        node = self.head
        while node.next is not None:
            if node.next.data == data:
                node.next = node.next.next

    def add_first(self, node) -> None:
        node.next = self.head
        self.head = node

    def add_last(self, data: str) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_before(self, data: str, target_data: str) -> None:
        if self.head is None:
            raise Exception("List is Empty")

        new_node = Node(data)

        if self.head.data == target_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Target data not found")

    def add_after(self, data: str, target_data: str) -> None:
        if self.head is None:
            raise Exception("List is Empty")

        new_node = Node(data)

        for node in self:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Target data not found")

    def remove_node(self, target_data: str) -> None:
        if self.head is None:
            raise Exception("List is Empty")

        if self.head.data == target_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Target data not found")




my_llist = LinkedList()
node1 = Node("One")
node2 = Node("Two")
node3 = Node("Three")

my_llist.head = node1
node1.next = node2
node2.next = node3

my_llist.add_node("Four")
my_llist.add_last("Five")
my_llist.add_after("Six", "Five")
my_llist.add_before("Five A", "Five")
print(my_llist)

