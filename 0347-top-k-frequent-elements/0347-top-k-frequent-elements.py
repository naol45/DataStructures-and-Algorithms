class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Declared variables for the lists
        counterHash = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []

        # for every number in the input, count the frequency of each item
        for n in nums:
            counterHash[n] = counterHash.get(n, 0) + 1
        # for the counted items in the counterHash, input the items in buckets
        for n, c in counterHash.items():
            bucket[c].append(n)
        # for every list in the bucket, starting from the end    
        for i in range(len(bucket) - 1, 0, -1):
            # for every item in that list include it in the result
            for n in bucket[i]:
                result.append(n)
            # the loop ends when the result length in equal to k
            if len(result) == k:
                return result
        