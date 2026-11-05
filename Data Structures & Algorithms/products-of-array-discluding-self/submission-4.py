class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        
        prod = 1
        prod_without_zero = 1

        for x in nums:
            prod *= x
            if x != 0:
                prod_without_zero *= x
        
        res = []
        
        for x in nums:
            if x != 0:
                res.append(prod // x)
            else:
                res.append(prod_without_zero)
        
        return res