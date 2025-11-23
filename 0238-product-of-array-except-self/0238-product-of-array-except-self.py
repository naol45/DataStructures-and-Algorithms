class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultList = [1] * len(nums)
        length = len(nums)
        prefix = 1
        for i in range(len(nums)):
            resultList[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            resultList[i] *= suffix
            suffix *= nums[i]
        return resultList