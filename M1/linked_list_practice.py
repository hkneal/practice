"""
Practicing Linked List Implementations
"""

from typing import Any

class Node:

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data
    

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> Any:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []

        for node in self:
            nodes.append(node.data)
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_first(self, new_node: Node) -> None:
        new_node.next = self.head
        self.head = new_node

    
    def append_node(self, new_node: Node) -> None:
        if self.head is None:
            self.add_first(new_node)
            return
        
        for node in self:
            if node.next is None:
                node.next = new_node
                return
            
    def add_before(self, target: str, new_node: Node) -> None:
            if self.head is None:
                raise Exception("List is empty!")
            
            if self.head.data == target:
                self.add_first(new_node)
                return

            previous = self.head

            for node in self:
                if node.data == target:
                    previous.next = new_node
                    new_node.next = node
                    return
                
                previous = node

            raise Exception("Target data was not found!")
                


myList = LinkedList()
# myList.add_first(Node("One"))
myList.append_node(Node("Two"))
myList.add_before("Two", Node("One"))

print(myList)

        