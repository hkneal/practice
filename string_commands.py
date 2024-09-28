"""Practice converting a string to an executable command"""

if __name__ == "__main__":

    x = int(input())
    x_set = set([int(n) for n in input().split()])
    num_of_commands = int(input())

    for _ in range(num_of_commands):
        command = input()
        if "pop" in command:
            target = ""
        else:
            command, target = command.split(" ")
        try:
            eval("x_set." + command + "(" + target + ")")
        except Exception:
            pass

    print(sum(x_set))

    """
    s.remove(5)
    print s
    set([1, 2, 3, 4, 6, 7, 8, 9])
    s.remove throws key error if not found

    s.discard does not throw key error

    in python 3 .pop() removes from the front and will throw key error on empty set/list

    """