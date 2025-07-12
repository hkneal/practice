def minimumBribes(q):
    # Write your code here
    num_of_bribes = 0

    for i, value in enumerate(q):
        if value -1 > i:
            if (value -1) - i > 2:
                return f"Too chaotic"
            else:
                num_of_bribes += (value -1) - i

    return num_of_bribes

q = [1,2,3,5,4,6,7,8]
q = [4,1,2,3]
q = [2,1,5,3,4]
q = [1,2,5,3,7,8,6,4]
print(minimumBribes(q))