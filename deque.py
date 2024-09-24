"""Practice with deques"""
import collections

if __name__ == "__main__":
    n = int(input())
    d = collections.deque()

    for _ in range(n):
        command = input()
        if "pop" in command:
            target = ""
        else:
            command, target = command.split(" ")
        eval("d." + command + "(" + target + ")")

    for element in d:
        print(element, end=" ")

"""
Deque methods:  https://docs.python.org/2/library/collections.html#deque-objects

append(x) - Add x to the right side of the deque.

appendleft(x) - Add x to the left side of the deque.

clear() - Remove all elements from the deque leaving it with length 0.

count(x) - Count the number of deque elements equal to x.

New in version 2.7.

extend(iterable) - Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable) - Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

pop() - Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft() - Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

remove(value) - Remove the first occurrence of value. If not found, raises a ValueError.

New in version 2.5.

reverse() - Reverse the elements of the deque in-place and then return None.

New in version 2.7.

rotate(n=1) - Rotate the deque n steps to the right. If n is negative, rotate to the left.
When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft()).

Deque objects also provide one read-only attribute:

maxlen - Maximum size of a deque or None if unbounded.
"""