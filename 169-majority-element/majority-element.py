class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = nums[0]
        counter = 0

        for i in range(len(nums)):
            if nums[i] == majority_element:
                counter = counter + 1
            else:
                counter = counter - 1
                if counter == 0 :
                    majority_element = nums[i]
                    counter = counter + 1
        
        return majority_element