from enum import Enum, auto

# class DiscountType(Enum):
#     STANDARD = auto()
#     SEASONAL = auto()
#     WEIGHT = auto()

# def get_discounted_price(cart_weight, total_price, discount_type):
#     discount = discount_type.name
#     if discount == "STANDARD":
#         return total_price * .94
#     elif discount == "SEASONAL":
#         return total_price * .82
#     elif discount == "WEIGHT":
#         if cart_weight <= 10:
#             return total_price * .94
#         else:
#             return total_price * .82
#     else:
#         return total_price

# print(get_discounted_price(12, 100, DiscountType.WEIGHT))

class TextInput:
    def __init__(self):
        self.value = ""

    def add(self, character: str):
        self.value = self.value + character

    def get_value(self):
        return self.value

class NumericInput(TextInput):
    def __init__(self):
        super().__init__()

    def add(self, character: any):
        if character.isdigit():
            super().add(character)

if __name__ == '__main__':
   input = NumericInput()
   input.add("1")
   input.add("a")
   input.add("0")
   print(input.get_value())

#    TextInput().add("HELLO3")