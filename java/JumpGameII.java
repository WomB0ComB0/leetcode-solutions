// You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

// Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:\

// 0 <= j <= nums[i] and
// i + j < n

// Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
class Solution {
    public int jump(int[] nums) {
        int len = nums.length - 1, curr = -1, next = 0, ans = 0;
        for (int i = 0 ; next <  len; i++){ // i is the current index
            if (i > curr) { // if we have reached the current index
                ans++;
                curr = next;
            }
            next = Math.max(next, nums[i] + i); // next is the max of the current next and the next index we can reach
        }
        return ans; // return the number of jumps, once the last index is reached       
    }
}