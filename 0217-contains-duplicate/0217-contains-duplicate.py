class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                return True
            else:
                map[n] = i
        return False
                