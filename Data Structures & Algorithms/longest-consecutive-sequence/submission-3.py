class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        s_nums = sorted(list(set(nums)))
        max_len = 1
        current_len = 1

        for i in range (1, len(s_nums)):
           if s_nums[i] - s_nums[i-1] == 1:
               current_len += 1
           else:
               current_len = 1
           max_len = max(max_len, current_len)
        
        return max_len