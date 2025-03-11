from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            nums1 = [0]
        if not nums2:
            nums2 =[0]
        m_index = 0
        n_index = 0

        if m == 0:
            zero_index = 0
        else:
            zero_index = m

        for _ in range(len(nums1)):
            while m_index < len(nums1) and n_index < len(nums2):
                if nums1[m_index] == 0 and m_index < zero_index:
                    m_index +=1

                elif nums1[m_index] == 0 and m_index >= zero_index:
                    if nums2[n_index] != 0:
                        nums1[m_index] = nums2[n_index]
                        m_index += 1
                        n_index += 1
                        zero_index += 1
                        if zero_index >= len(nums1):
                            break

                elif n == 0:
                    m_index += 1

                elif nums1[m_index] <= nums2[n_index]:
                    m_index +=1

                elif nums2[n_index] < nums1[m_index]:
                    nums1[zero_index] = nums1[m_index]
                    nums1[m_index] = nums2[n_index]
                    m_index += 1
                    n_index += 1
                    zero_index += 1
                    if zero_index >= len(nums1):
                            break
            break

        print(nums1)



nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1
Solution().merge(nums1, m, nums2, n)

# Accepted answer but not O(n)
# if not nums1:
#     nums1 = [0]
# if not nums2:
#     nums2 =[0]

# m_index = len(nums1) -1
# n_index = len(nums2) -1

# while m_index >=0 and n_index >=0:
#     if nums1[m_index] == 0:
#         nums1[m_index] = nums2[n_index]
#         m_index -=1
#         n_index -=1
# nums1.sort()
# print(nums1)