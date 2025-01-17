# include <iostream>
# include <algorithm>
# include <vector>
using namespace std;
 

////  this is solved by using brute force algorithm that take O(n^2) time complexity
// int majorityElementFinder(const vector <int> &nums) {
//     int n = nums.size();
//     for (int val:nums) {
//         int count = 0;
//         for (int el:nums) {
//             if (val == el) {
//                 count++;
//             }
//         }
//         if(count > n/2){
//             return val;
//         }
//     }
//     return 0;
// }





//// this is solved by using optimized algorithm that take O(n log n) time complexity
// int majorityElementFinder(const vector <int> &nums) {
//     vector <int> sortedNum = nums;

//     int n = sortedNum.size();
    
//     // sort 
//     sort(sortedNum.begin(), sortedNum.end());

//     // freq count
//     int freq = 1, ans = sortedNum[0];
//     for (int i=1; i<n; i++) {
//         if(sortedNum[i] == sortedNum[i-1]) {
//             freq++;
//         }else {
//             freq = 1;
//             ans = sortedNum[i];
//         }
//         if(freq > n/2) {
//             return ans;
//         }
//     }
//     return 0;
// }







// this is solved by using moore's voting algorithm that take O(n) time complexity
int majorityElementFinder(const vector <int> &nums) {
    vector <int> sortedNum = nums;

    int n = sortedNum.size();
    
    int freq = 0, ans = 0;

    for (int i=0; i<n; i++) {
        if(freq == 0) {
            ans = nums[i];
        }
        if(ans == nums[i]) {
            freq++;
        }
        else {
            freq--;
        }
    }
    return ans;
}


int main() {
    vector <int> vec = {1,1,1,1,1,2,2,3,3,3};
    int majorityElement = majorityElementFinder(vec);
    cout << "Majority Element is : " << majorityElement;
    return 0;
}