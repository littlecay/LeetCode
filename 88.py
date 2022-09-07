class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pm = 0
        pn = 0
        while len(nums2)>0:
            while nums1[pm] <= nums2[0] and pm < m+n-len(nums2):
                pm += 1
            for i in range(len(nums1)-2,pm-1,-1):
                nums1[i+1] = nums1[i]
            nums1[pm] = nums2.pop(0)
