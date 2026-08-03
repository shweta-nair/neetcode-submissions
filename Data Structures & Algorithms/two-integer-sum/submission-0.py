class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i in range(len(nums)):
            k=target-nums[i]
            if k in s:
                return [s[k],i]
            s[nums[i]] = i