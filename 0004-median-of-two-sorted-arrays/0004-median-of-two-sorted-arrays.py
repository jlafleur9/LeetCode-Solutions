class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        length = len(merged)
        if length % 2 == 0:
            mid1 = merged[length // 2 - 1]
            mid2 = merged[length // 2]
            return ((mid1 + mid2) / 2)
        else:
            mid = merged[length // 2]
            return mid