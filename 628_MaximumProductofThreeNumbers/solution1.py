"""
key point is to find three largest numbers, and two smallest numbers

so we can improve the complexity from O(nlgn) to O(n)

"""

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, secondlargest, thirdlargest = -1<<31, -1<<31, -1<<31
        smallest, secondsmallest = (1 << 31)-1, (1 << 31)-1
        for n in nums:
            if n <= smallest:
                secondsmallest = smallest
                smallest = n
            elif n <= secondsmallest:
                secondsmallest = n
            if n >= largest:
                thirdlargest = secondlargest
                secondlargest = largest
                largest = n
            elif n >= secondlargest:
                thirdlargest = secondlargest
                secondlargest = n
            elif n >= thirdlargest:
                thirdlargest = n
        return max(largest*secondlargest*thirdlargest, smallest*secondsmallest*largest)


if __name__ == "__main__":
    nums = [-1, -2, -3]
    sol = Solution()
    print(sol.maximumProduct(nums))
