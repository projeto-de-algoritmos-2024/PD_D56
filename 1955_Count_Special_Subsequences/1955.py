class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        count_0, count_1, count_2 = 0, 0, 0
        
        for num in nums:
            if num == 0:
                count_0 = (count_0 + 1) % mod
            elif num == 1:
                count_1 = (count_1 + count_0) % mod
            elif num == 2:
                count_2 = (count_2 + count_1) % mod
                
        return count_2
