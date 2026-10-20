class Solution:
    def binarySearchLeft(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def binarySearchRight(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        index = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ext_left = self.binarySearchLeft(nums, target)
        # if the target never appears, no need for the second search
        if ext_left == -1:
            return [-1, -1]

        ext_right = self.binarySearchRight(nums, target)
        return [ext_left, ext_right]
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna