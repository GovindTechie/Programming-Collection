# include<iostream>
# include<vector>

using namespace std;

class Solution {
public:
    vector<int> result;
    vector<int> maxIndices;
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        for(int i=0; i<nums.size(); i++) {
            if(!maxIndices.empty() && maxIndices.front() <= i-k) {
                maxIndices.erase(maxIndices.begin());
            }

            while(!maxIndices.empty() && nums[i] >= nums[maxIndices.back()]) {
                maxIndices.pop_back();
            }

            maxIndices.push_back(i);

            if(i >= k-1) {
                result.push_back(nums[maxIndices.front()]);

            }
        }
        return result;
    }
};

int main() {
    Solution s1;
    vector<int>nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    vector<int> result;
    cout << "The original nums are : " ;
    for(int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }   
    cout << "The window size is : " << k << endl;
    result = s1.maxSlidingWindow(nums, k);
    cout << "The max from each window are : ";
    for(int i=0; i<result.size(); i++) {
        cout << result[i] << " ";
    }

    return 0;
}