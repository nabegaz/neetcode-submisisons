class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Place lists in set for instant lookup 
        num_set = set(nums)
        longest = 0
        for n in nums: 
            # Check if there is a previous num liset
            # If n - 1 does not exists, then that a start of seq
            length = 0
            if n - 1 not in num_set:
                while n + length in num_set:
                    length += 1
                    longest = max(longest, length)
        return longest
