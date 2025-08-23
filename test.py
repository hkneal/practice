# print("1".islower())

# print("5133-3367-8912-3456".replace("-", ""))
import re
from collections import Counter
pattern2 = r"(.)\1{3}"
cc_num = "5133-2367-8912-3456"
cc_num = cc_num.replace("-", "")
matches = re.search(pattern2, cc_num)
if matches:
    print("No Matches")


s = "aaab"

print("aaa" in "aaabcd")