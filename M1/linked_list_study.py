"""Linked List Study """

from typing import Any


class Node:
    
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data
    
class LinkedList:

    def _is_empty(self, data: str) -> bool:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return True

        return False

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> Any:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.data)
        nodes.append("End")
        return " => ".join(nodes)
    
    
    def add_to_end(self, data: str) -> None:
        new_node = Node(data)

        if not self._is_empty(data):
            node = self.tail
            node.next = new_node
            self.tail = new_node

    def add_to_beginning(self, data: str) -> None:
        new_node = Node(data)

        if not self._is_empty(data):
            node = self.head
            new_node.next = node
            self.head = new_node

    def insert_after(self, target: str, data: str) -> None:
        # If target not found, insert at end
        new_node = Node(data)

        if not self._is_empty(data):

            node = self.head
            while node is not None:
                if node.data == target:
                    new_node.next = node.next
                    node.next = new_node
                    if new_node.next is None:
                        self.tail = new_node
                    return
                node = node.next

            # Target not found
            self.add_to_end(data)

    def insert_before(self, target: str, data: str) -> None:
        # If target not found, insert at end
        new_node = Node(data)

        if not self._is_empty(data):

            node = self.head
            previous = self.head
            while node is not None:
                if node.data == target:
                    new_node.next = node

                    # Re-adjust head
                    if previous is self.head:
                        self.head = new_node

                    else:
                        previous.next = new_node

                    return
                previous = node
                node = node.next

            # Target not found
            self.add_to_end(data)



            
my_list = LinkedList()
my_list.add_to_beginning("One")
my_list.add_to_beginning("Start")
my_list.add_to_end("Two")
my_list.add_to_end("Four")
my_list.insert_after("Two", "Three")
my_list.insert_after("Four", "Five")
my_list.add_to_end("Eight")
my_list.insert_before("Eight", "Seven")
my_list.insert_before("Start", "Beg")
my_list.insert_before("Seven", "Six")
print(my_list)