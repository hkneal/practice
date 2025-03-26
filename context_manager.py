from collections import Counter
import time

class TimerContext:
  def __enter__(self):
    self.start_time = time.time()
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.end_time = time.time()
    self.elapsed_time = self.end_time - self.start_time
    print(f"Total Elapsed Time: {self.elapsed_time} Seconds")


def get_odd(counter_dict) -> int: #index value
    for num, value in counter_dict.items():
        if value % 2 != 0:
            return num # This assumes only one odd value exsists
    return None


A = [9,3,9,3,9,7,9]
A_count = Counter(A)

with TimerContext():
  print("Value returned is:", get_odd(A_count))