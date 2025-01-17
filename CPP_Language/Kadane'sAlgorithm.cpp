#include<iostream>
#include<vector>
using namespace std;

int main() {
    vector<int> nums = {4, 1, 2, -1, 2};
    int maxSum = INT_MIN, currSum = 0;
    for (int start:nums) {
        currSum += start;
        maxSum = max(maxSum, currSum);
        if (currSum < 0) {
            currSum = 0;
        }
    }
    cout << "Max subarray sum = " << maxSum << endl;
    return 0;
}