class Enemy:
    def __init__(self, type: str, size: int = 10):
        self.__type_of_enemy = type # Creates private protected attribute
        self.__size = size

    def get_type(self) -> str:
        return self.__type_of_enemy

    def set_type(self, type: str):
        self.__type_of_enemy = type

    def get_size(self):
        return self.__size

    def set_size(self, size: int):
        self.__size = size


    def __repr__(self):
        return self.__type_of_enemy + f" Size {self.__size} "



zombie = Enemy("Zombie")
zombie.__type_of_enemy = "Orc"
print(zombie.get_type())
zombie.set_type("Orc")

print(zombie)

zombie.__size = 5
print(zombie)