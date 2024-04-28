class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        if nums2[0] >= nums1[m - 1]:
            nums1[m : m + n] = nums2
            return
        pointer = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums2[n] >= nums1[m]:
                nums1[pointer] = nums2[n]
                n -= 1
            else:
                nums1[pointer] = nums1[m]
                m -= 1
            pointer -= 1
        while n >= 0:
            nums1[pointer] = nums2[n]
            n -= 1
            pointer -= 1
