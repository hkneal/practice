from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.numsArr = nums


    def update(self, index: int, val: int) -> None:
        self.numsArr[index] = val


    def sumRange(self, left: int, right: int) -> int:
        prefixArray = [self.numsArr[0]]
        print(prefixArray, self.numsArr)
        for i in range(1, len(self.numsArr)):
            print(i)
            prefixArray.append(self.numsArr[i] + prefixArray[i-1])
        print(prefixArray)
        if left - 1 < 0 :
            return prefixArray[right]
        return prefixArray[right] - prefixArray[left-1]

nums = [1, 2, 5]
numsArray = NumArray(nums)
print(numsArray.sumRange(0,2))
