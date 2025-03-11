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
        _ = 0

        while m_index < len(nums1) and n_index < len(nums2) and _ < len(nums2):
            if nums1[m_index] == 0 and m_index < zero_index and nums2[n_index] >= 0:
                print("Calling #1")
                m_index +=1

            elif nums1[m_index] == 0 and m_index >= zero_index:
                print("Calling #2")
                nums1[m_index] = nums2[n_index]
                m_index += 1
                n_index += 1
                zero_index += 1
                if zero_index >= len(nums1):
                    print(f"Breaking in call 2 at indicies: M-{m_index}, N-{n_index}, and Zero-{zero_index}")
                    break

            elif n == 0:
                print("Calling #3")
                m_index += 1

            elif nums1[m_index] <= nums2[n_index]:
                print("Calling #4")
                m_index +=1

            elif nums2[n_index] < nums1[m_index]:
                print("Calling #5")
                nums1[m_index:zero_index+1] = [nums2[n_index]] + nums1[m_index:zero_index]
                m_index += 1
                n_index += 1
                zero_index += 1
                if zero_index >= len(nums1):
                    break
            print(nums1)
            print(f"Counter, {_}, MIndex: {m_index}, NIndex: {n_index}, ZeroIndex: {zero_index}")
            # break

        print(nums1)



nums1 = [-12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
m = 1
nums2 = [-49,-45,-42,-41,-40,-39,-39,-39,-38,-36,-34,-34,-33,-33,-32,-31,-29,-28,-26,-26,-24,-21,-20,-20,-18,-16,-16,-14,-11,-7,-6,-5,-4,-4,-3,-3,-2,-2,-1,0,0,0,2,2,6,7,7,8,10,10,13,13,15,15,16,17,17,19,19,20,20,20,21,21,22,22,24,24,25,26,27,29,30,30,30,35,36,36,36,37,39,40,41,42,45,46,46,46,47,48]
n = 90
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