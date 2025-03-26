rows = 10

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
print("\n")



l = [1,2,3,4,5]
test = lambda x , y: x+y
print(test(3,4))

numbers = [1, 2, 3, 4]
squared = [x*x for x in numbers]
print(squared)



# for i in range(rows):
#     print(" " * (rows - i - 1) + "^" * (2 * i + 1))