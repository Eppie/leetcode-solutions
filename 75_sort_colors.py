class Solution:
    """
    The `sortColors` function sorts an array containing only 0s, 1s, and 2s in place,
    using the Dutch National Flag algorithm. The goal is to group all 0s, 1s, and 2s
    together in ascending order.

    The algorithm maintains three pointers:
    - `low` (initially 0) to track the position to place the next 0.
    - `mid` (initially 0) to iterate through the array.
    - `high` (initially len(nums) - 1) to track the position to place the next 2.

    Algorithm steps:
    1. Iterate while `mid` <= `high`.
    2. If `nums[mid]` is 0, swap `nums[low]` and `nums[mid]`, then increment both `low` and `mid`.
    3. If `nums[mid]` is 1, just increment `mid`.
    4. If `nums[mid]` is 2, swap `nums[high]` and `nums[mid]`, then decrement `high`.

    Example:
    nums = [2, 0, 2, 1]
    low = 0, mid = 0, high = 3

    Step-by-step process:
    1. nums[mid] is 2:
       Swap nums[0] and nums[3]:
       nums = [1, 0, 2, 2]
       low = 0, mid = 0, high = 2
    2. nums[mid] is 1:
       Increment mid:
       nums = [1, 0, 2, 2]
       low = 0, mid = 1, high = 2
    3. nums[mid] is 0:
       Swap nums[0] and nums[1]:
       nums = [0, 1, 2, 2]
       low = 1, mid = 2, high = 2
    4. nums[mid] is 2:
       Swap nums[2] and nums[2]:
       nums = [0, 1, 2, 2]
       low = 1, mid = 2, high = 1

    Final sorted array:
    nums = [0, 1, 2, 2]
    """

    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
