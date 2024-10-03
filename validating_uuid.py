import re
from collections import Counter
pattern1 = r"^([\w]{10})$"
pattern2 = r"(?=(?:.*\d){3})"
pattern3 = r"(?=(?:.*[A-Z]){2})"


def used_once(c: int) -> bool:
    return c <= 1

if __name__ == "__main__":
    for _ in range(int(input())):
        emp_id = (input())

        if (
            (re.match(pattern1, emp_id))
            and (re.match(pattern2, emp_id))
            and (re.match(pattern3, emp_id))
        ):
            counts = list(map(used_once, Counter(emp_id).values()))
            # print(counts)
            if all(counts):
                print("Valid")
            else:
                print("Invalid")
        else:
            # print("Failed All")
            print("Invalid")
