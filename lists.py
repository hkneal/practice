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


minimumBribes(my_list)


new_list = ["one", "two", "three", "four", "five"]

ind = new_list.index("three")
new_list = new_list[ind:]
print(new_list)

# def logn(n: int):

#     for j in range(2,n,pow(j,2)):
#         print(j)


# logn(32)


num1 =11
num2 = num1

num1 = 22
print(num1, num2)

d1 = {"n":11}
d2 = d1

print(d2)

d1["n"]=22
print(d2)