class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int indexN = n -1;
        int indexM = m-1;
        int currentIndex = m+n -1;

        while(indexN >= 0 && indexM >= 0)
        {
            if(nums1[indexM] > nums2[indexN])
            {
                nums1[currentIndex] = nums1[indexM];
                indexM--;
            }
            else
            {
                nums1[currentIndex] = nums2[indexN];
                indexN--;
            }
            currentIndex--;
        }
        while(indexN >= 0)
        {
            nums1[currentIndex] = nums2[indexN];
            indexN--;
            currentIndex--;
        }
        
    }
}