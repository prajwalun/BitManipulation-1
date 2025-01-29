# The singleNumber method finds the element that appears only once in an array where every other element appears twice.

# Approach:
# - Use XOR operation to cancel out duplicate numbers.
# - XOR of two identical numbers is 0, leaving the unique number.

# TC: O(n) - Single pass through `nums`.
# SC: O(1) - Constant space usage.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res