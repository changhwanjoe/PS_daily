//https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;

        int p_val = nums[0];
        for (int i = 1; i < n - 1; i++) {
            int c_val = nums[i];
            int l_idx = i - 1, r_idx = i + 1;
            int l_nei = 0, r_nei = 0;
            if (c_val == p_val) continue;
            p_val = c_val;
            while (l_idx >= 0) {
                if (nums[l_idx] != c_val) {
                    l_nei = nums[l_idx];
                    break;
                }
                l_idx--;
            }

            while (r_idx < n) {
                if (nums[r_idx] != c_val) {
                    r_nei = nums[r_idx];
                    break;
                }
                r_idx++;
            }
            //cout << l_nei << " " << c_val << " " << r_nei << endl;
            
            if (!l_nei || !r_nei)
                continue;

            if (c_val > l_nei && c_val > r_nei)
                ans++;
            if (c_val < l_nei && c_val < r_nei)
                ans++;
        }

        return ans;
    }
};