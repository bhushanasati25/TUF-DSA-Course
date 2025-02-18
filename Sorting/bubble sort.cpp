class Solution {
   public:
    vector<int> bubbleSort(vector<int>& nums) {
        int n = nums.size();
        for (int i = n - 1; i >= 0; i--) {
            bool didswap = false;
            for (int j = 0; j <= i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    swap(nums[j], nums[j + 1]);
                    didswap = true;
                }
            }

            if (!didswap) {
                break;
            }
        }
        return nums;
    }
};
