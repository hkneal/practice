"""Find which room is the Captain's based on a aset of n grouped size values
Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
Sample Output

8 Captain is in room 8 (Captain has the only room with 1 person)

"""

from collections import Counter
if __name__ == "__main__":

    group_size = int(input().rstrip())
    groups = Counter([int(x) for x in input().split(" ")])

    print(min(groups, key=groups.get))