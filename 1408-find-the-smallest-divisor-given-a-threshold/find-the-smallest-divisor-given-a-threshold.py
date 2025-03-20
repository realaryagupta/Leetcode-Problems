class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            division_sum = sum(math.ceil(num / mid) for num in nums)

            if division_sum <= threshold:
                ans = mid  # Update answer
                right = mid - 1  # Try a smaller divisor
            else:
                left = mid + 1  # Increase divisor to reduce sum

        return ans  # Return the smallest valid divisor    