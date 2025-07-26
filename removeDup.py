#26 Remove dulpicate from sorted array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k

sol = Solution()
nums1 = [0, 1, 1]
k1 = sol.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [0, 1]

nums2 = [0, 0, 1, 1, 1, 2, 2, 2, 4, 4]
k2 = sol.removeDuplicates(nums2)
print(k2, nums2[:k2])  # Output: 4, [0, 1, 2, 4]
