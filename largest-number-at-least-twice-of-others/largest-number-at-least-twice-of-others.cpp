class Solution {
public:
    int dominantIndex(vector<int>& nums) {
         int maxNumber = *std::max_element(nums.begin(), nums.end());
        // cout << maxNumber << endl;
            int max_num = *std::max_element(nums.begin(), nums.end());

    int max_num_index = -1;

    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] == max_num)
        {
            max_num_index = i;
        }

        if (nums[i] * 2 > max_num && nums[i] != max_num)
        {
            return -1;
        }
    }

    return max_num_index;
    }
};