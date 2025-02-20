class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []
        result = [-1] * n  # Initialize the result array with -1

        # Traverse the array twice to handle circular behavior
        for i in range(2 * n - 1, -1, -1):
            current_index = i % n  # Use modulo to wrap around
            
            # Pop elements from the stack that are less than or equal to nums[current_index]
            while stack and stack[-1] <= nums[current_index]:
                stack.pop()

            # If stack is not empty, assign the top of the stack as next greater element
            if stack:
                result[current_index] = stack[-1]
            
            # Push the current element onto the stack
            stack.append(nums[current_index])

        return result