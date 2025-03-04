import threading

def say_my_name(name: str):
    print(name)

t1 = threading.Thread(target=say_my_name, args=("Hiram",))
t2 = threading.Thread(target=say_my_name, args=("Neal",))

t1.start()
t2.start()

print("Hello Guys")

t1.join()
t2.join()

print("End of program")