import inspect, functools

# def print_parms(func):
#     def wrapper(*args, **kwargs):
#         args = ("Hiram",)
#         print(f"Inside wrapper: {args[0]}")
#         return func(*args, kwargs)
#     return wrapper

def print_parms(author, version):

    def wrapper(func):
        func.meta = {
            'author': author,
            'version': version
        }
        str = ("Hiram",)
        return func
    return wrapper

@print_parms("Hiram", 1.0)
def tester(*args, **kwargs):
    """Testing all of this"""
    pass


# tester()
# print(f'{tester.__annotations__}')
# print(f'{print_parms.__annotations__}')
# print(f'Inspected: {inspect.getfullargspec(tester)}')

print(tester.meta)