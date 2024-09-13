import time

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

def arr_find():
    my_list = ['ab', 'sd', 'ef', 'de']
    # for i in range(0,int(len(my_list)/2)+1,2):
    #     j = i +1
    #     print("I: {}, J: {}".format(i, j))
    #     if my_list[i] == 'ef' or my_list[j] == 'ef':
    #         print("Found")

    for i in range(0,len(my_list)):
        if my_list[i] == 'ef':
            print("Found")

    # Does not improve performance
    # The though was it would run in O(n/2) and be quicker,
    # The added complexity added cycles.

t1 = time.perf_counter(), time.process_time()
arr_find()
t2 = time.perf_counter(), time.process_time()

print(f"Real time: {t2[0] - t1[0]}")
print(f"CPU time: {t2[1] - t1[1]}")
