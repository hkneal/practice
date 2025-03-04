"""Playing with decorators"""

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Testing this decorator")
        func(*args, **kwargs)
        print("After Execution")
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_add(x):
    print("In my_add")
    return sum(x)


print(my_add([3,4]))