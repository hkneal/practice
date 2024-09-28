"""Practicing deque functions

There is a horizontal row of cubes. The length of each cube is given.
You need to create a new vertical pile of cubes.
The new pile should follow these directions: if cube[i] is on top of cube[j] then is cube[i] must be smaller than the
top cube.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example
blocks = [1,2,3,8,7]

Result: No

After choosing the rightmost element 7, choose the leftmost element, 1.
After than, the choices are 2 and 8. The larger is larger than the top block of size .

Result: Yes

"""
from collections import deque

if __name__ == "__main__":
    num_cases = int(input().rstrip())

    for _ in range(num_cases):
        count = 0
        top = None
        n = int(input().rstrip())
        a_deque = deque([int(x) for x in input().split(" ")])
        is_stackable = True

        while count < n:
            # print(f"Top: {top}")
            if a_deque[0] >= a_deque[-1]:
                if not top:
                    top = a_deque.popleft()
                    count +=1
                elif a_deque[0] <= top:
                    top = a_deque.popleft()
                    count +=1
                elif a_deque[0] > top:
                    is_stackable = False
                    break

            elif a_deque[0] < a_deque[-1]:
                if not top:
                    top = a_deque.pop()
                    count +=1
                elif a_deque[-1] <= top:
                    top = a_deque.pop()
                    count +=1
                elif a_deque[-1] > top:
                    is_stackable = False
                    break
        if is_stackable:
            print("Yes")
        else:
            print("No")