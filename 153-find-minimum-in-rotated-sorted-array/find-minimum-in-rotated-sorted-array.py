class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we cant sort it and return the first element. since soring is o(n log n)
        # we have to use binary search
        # we need to find the minimum element in a rotaed array
        # in a rotated array, either it is all sorted or there are two halfs sorted
        # if we land on the middle element and we need to find the minimum, we need to check if the number on the far end of the array (right ptr) is less than the target, if it is, this means the array has been rotated and then we need to look in the other half, so we increase left pointter to be mid + 1 and keep going until we have found a valid value. The minimum element will be at the left pointer

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]