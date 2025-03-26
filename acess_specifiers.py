class MyClass():
    def __init__(self):
        self._protected_variable = "This is protected."

class SubClass(MyClass):
    def print_protected(self):
        print(self._protected_variable)

obj = SubClass()
print(obj._protected_variable)