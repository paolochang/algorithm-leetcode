/**
  * Iteration: Binary Search
  * Time Complexity: O(log n)
  * Space Complexity: O(log n)
  */
public class Solution {
    public int FindPeakElement(int[] nums) {
        int left = 0;
        int right = nums.Length - 1;

        while (left < right) {
            int mid = left + ((right - left) / 2);

            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}