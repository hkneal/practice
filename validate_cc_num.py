import re

pattern1 = r"([0-9]{4})(-?)([0-9]{4})(-?)([0-9]{4})(-?)([0-9]{4})"
pattern2 = r"(.)\1{3}"

if __name__ == "__main__":
    n = int(input().rstrip())
    for _ in range(n):
        cc_num = input()

        if (
            not cc_num.startswith(("4", "5", "6"))
            or (len(cc_num) < 16)
            or (len(cc_num) > 19)
            or (not re.match(pattern1, cc_num))
            or (re.search(pattern2, cc_num.replace("-", "")))
        ):
            print("Invalid")

        else:
            print("Valid")