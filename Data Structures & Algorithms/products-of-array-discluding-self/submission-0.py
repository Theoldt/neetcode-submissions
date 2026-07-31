class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        for i,num in enumerate(nums):
            temp = nums.copy()
            del temp[i]
            product = 1
            for x in temp:
                product *= x
            result.append(product)
        
        return result
