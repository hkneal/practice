from regex_engine import generator

generate = generator()

regex = generate.numerical_range(100000,999999)

print(regex)

