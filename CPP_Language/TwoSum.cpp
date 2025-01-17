// we are creating a program that have given one target variable and one array and in that \
two number that addition is target value and we have to return the array of that index

#include<iostream>
#include <vector>
using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
    vector<int>ex;
    int n = nums.size();

    int i=0, j=n-1;

    while(i<j) {
        int pairSum = nums[i] + nums[j];
        if (pairSum > target) {
            j--;
        }else if(pairSum < target) {
            i++;
        }else {
            ex.push_back(i);
            ex.push_back(j);
            return ex;
        }
    }
return ex;
}

int main (){
    vector <int> nums = {2,7,11,15};
    int target = 13;
    vector <int> ans = twoSum(nums, target);
    cout << ans[0] << ", " << ans[1];
    
    return 0;
}