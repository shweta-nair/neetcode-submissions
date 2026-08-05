class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        s = sorted(s)

        c = 1
        maxi = 1

        for i in range(len(s) - 1):
            if s[i + 1] == s[i] + 1:
                c += 1
            else:
                maxi = max(maxi, c)
                c = 1

        maxi = max(maxi, c)
        return maxi