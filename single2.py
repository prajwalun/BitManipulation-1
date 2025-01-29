# The singleNumber method finds the two unique numbers in an array where every other number appears twice.

# Approach:
# - Compute XOR of all numbers to get `xor` of the two unique numbers.
# - Find the rightmost set bit to separate numbers into two groups.
# - XOR each group to get the two unique numbers.

# TC: O(n) - Single pass through `nums`.
# SC: O(1) - Constant space usage.


class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        rightmost_set_bit = xor & -xor
        
        num1, num2 = 0, 0
        for num in nums:
            if (num & rightmost_set_bit) == 0:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]