class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry:
            carry, digits[i]  = divmod(digits[i] + carry, 10)
            i -= 1
        if carry:
            digits.insert(0, carry)
        return digits

print(Solution().plusOne([9,9]))