#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        int total = 1 << n;
        vector<vector<int>> result;

        for(int mask = 0; mask < total; ++mask) {
            vector<int> subset;
            for(int i = 0; i<n; ++i) {
                if((mask >> i) & 1) {
                    subset.push_back(nums[i]);
                }
            }
            result.push_back(subset);
        }
        return result;
    }
};

// Usage example
int main() {
    Solution s;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> powerSet = s.subsets(nums);

    for (const auto& subset : powerSet) {
        cout << "[ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "]" << endl;
    }

    return 0;
}
