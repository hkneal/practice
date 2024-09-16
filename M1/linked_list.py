class Node:
    def __init__(self, data: str) -> object:
        self.data = data
        self.next = None      
        self.prev = None

    def __repr__(self):
        return self.data
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_node(self, new_node: Node) -> None:
        if self.head is None:
            self.head = new_node
            return

        for node in self:
            if node.next == None:
                node.next = new_node
                return
            
    def add_first(self, new_node: Node) -> None:
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, new_node: Node, target_data: str) -> None:
        if self.head == None:
            raise Exception("Empty List")

        for node in self:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Taget Node Not Found")
    
    def insert_before(self, new_node: Node, target_data: str) -> None:
        if self.head == None:
            raise Exception("Empty List")
        
        if self.head.data == target_data:
            return self.add_first(new_node)
        
        previous_node = self.head
        for node in self:
            if node.data == target_data:
                previous_node.next = new_node
                new_node.next = node
                return
            previous_node = node

        raise Exception("Target Node Not Found")
    
    def remove_node(self, target_data: str) -> None:
        if self.head == None:
            raise Exception("Empty List")
        
        if self.head.data == target_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Target Node Not Found")



nodeb = Node("Two")
nodec = Node("Three")
nodeb.next = nodec

my_linked_list = LinkedList()
# my_linked_list.head = nodeb
my_linked_list.add_node(Node("Four"))
my_linked_list.add_node(Node("Six"))
# my_linked_list.add_first(Node("One"))
# my_linked_list.insert_after(Node("Five"), "Four")
# my_linked_list.insert_before(Node("TwoB"), "Two")
print(my_linked_list)
# my_linked_list.remove_node("TwoB")
print(my_linked_list)



