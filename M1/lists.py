my_list = [2,1,5,3,4]

def minimumBribes(q):
    # Write your code here
    """
    For every position in the list check the value against the index if it's less than two from the index reply 'Too chaotic'
    """
    too_chaotic = False
    min_brides = 0
    for index, value in enumerate(q):
        test = (value - (index+1))
        print(test)
        if test > 2:
            # print(f"Index: {index}, Value: {value}, Diff: {(value - index)}")
            too_chaotic = True

            if test > min_brides:
                min_brides = test

    if too_chaotic:
        print('Too chaotic')
    else:
        print(min_brides)

new_list = [None] * 128
new_list[ord("c")] = 1
new_list[ord("d")] = 3
new_list[ord("e")] = 4

minimumBribes(my_list)
print(ord('c'))
print(new_list)