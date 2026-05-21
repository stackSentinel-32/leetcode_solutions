class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Use int() division to truncate towards zero like C++ does
        # Do NOT use // here, because -2147483648 // 10 becomes -214748365
        MAX_LIMIT = int(INT_MAX / 10)
        MIN_LIMIT = int(INT_MIN / 10)

        while x != 0:
            digit = x % 10

            # Fix Python negative modulo behavior (but ignore exact zeroes!)
            if x < 0 and digit != 0:
                digit -= 10

            # Overflow check
            if rev > MAX_LIMIT or (rev == MAX_LIMIT and digit > 7):
                return 0

            if rev < MIN_LIMIT or (rev == MIN_LIMIT and digit < -8):
                return 0

            # Build reversed number
            rev = rev * 10 + digit

            # Remove last digit (truncates towards zero)
            x = int(x / 10)

        return rev