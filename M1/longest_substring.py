"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def lengthOfLongestSubstring(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    # counter_set = set()
    counter = 0
    max_cntr = 0
    rolling_lst = []

    for _ in s:
        if _ not in rolling_lst:
            rolling_lst.append(_)
            counter +=1
            if counter > max_cntr:
                max_cntr = counter

        else:
            rolling_lst.append(_)
            lst_ind = rolling_lst.index(_)
            rolling_lst = rolling_lst[lst_ind+1:]
            counter = len(rolling_lst)
            if counter > max_cntr:
                max_cntr = counter
    
    return max_cntr


s = "abcabcbb"  

print(lengthOfLongestSubstring(s))
        


            
            
        