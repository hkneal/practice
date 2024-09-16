"""
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
"""

import itertools

def partitionString(s: str) -> int:

    # get all possible substrings from the string 

    slst = list(s)
    par_set = set()
    
    for ind, char in enumerate(slst):
        print(ind, char)




partitionString("abacaba")