class Tester():

    def __init__(self, iterable=(), **kwargs) -> None:
        self.__dict__.update(iterable, **kwargs)



d = Tester({'first_name':"Hiram", 'last_name':"Neal"})
print(d.last_name)