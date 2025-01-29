# The divide method performs integer division without using multiplication, division, or mod operators.

# Approach:
# - Handle edge cases for overflow.
# - Use bitwise shifting to speed up repeated subtraction.
# - Keep subtracting the divisor in multiples until reaching the dividend.
# - Return the final quotient with the correct sign.

# TC: O(log n) - Logarithmic due to bitwise shifts.
# SC: O(1) - Constant space usage.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31

        negative = (dividend < 0) ^ (divisor < 0)

        absDividend, absDivisor = abs(dividend), abs(divisor)

        quotient = 0

        while absDividend >= absDivisor:
            tempDivisor, multiple = absDivisor, 1
            while absDividend >= (tempDivisor << 1):
                tempDivisor <<= 1
                multiple <<= 1
            absDividend -= tempDivisor
            quotient += multiple

        return -quotient if negative else quotient