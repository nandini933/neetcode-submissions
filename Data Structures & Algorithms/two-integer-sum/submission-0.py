class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff not in dic:
                dic[nums[i]] = i
            else:
                return [dic[diff], i]
        