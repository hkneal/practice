class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)

        longest_sub = 0
        head = 0
        tail = 0
        char_map = {}

        while( head < len(s) and tail < len(s)):
            current_char = s[tail]
            if current_char in char_map:
                previous_char = char_map[current_char]
                head = max(head, previous_char + 1)
            char_map[current_char] = tail
            longest_sub = max(longest_sub, tail - head +1)
            tail +=1
        return longest_sub

test = "aera"
print(Solution().lengthOfLongestSubstring(test))
