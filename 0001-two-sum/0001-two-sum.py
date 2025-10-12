class Solution(object):
    def twoSum(self, nums, target):
        output = []
        map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in map:
                output.extend([map[difference], i])
                return output
            map[n] = i
        return