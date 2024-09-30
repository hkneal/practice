# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == "__main__":
    for _ in range(int(input().rstrip())):

        s = input()
        print(re.sub(r"(?<= )&&(?= )", "and", re.sub(r"(?<= )\|\|(?= )", "or", s)))