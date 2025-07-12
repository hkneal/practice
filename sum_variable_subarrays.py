def get_sum_of_subarrays(nums: list[int]) -> int:
    total_sum = nums[0]
    for i in range(1, len(nums)):
        start = max(0, i - nums[i])
        total_sum += sum(nums[start:i+1])
    return total_sum


nums = [2,3,1]
nums = [3,1,1,2]
print(get_sum_of_subarrays(nums))