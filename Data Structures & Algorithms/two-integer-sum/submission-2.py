class Solution:
    def twoSum(self, nums, target):
        mpp = {}

        for i in range(len(nums)):
            left = target - nums[i]
            if left in mpp:
                return [mpp[left], i]

            mpp[nums[i]] = i