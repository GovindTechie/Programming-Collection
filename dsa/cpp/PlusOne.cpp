# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        for (int i= size-1; i >= 0; i --){
            if(digits[i] < 9) {
                digits[i] += 1;
                return digits;
            }
            else {
                digits[i] = 0;
            }
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main(){
    vector<int> digits {9};
    Solution solver;
    vector<int> result = solver.plusOne(digits);

    for(int d : result) {
        cout << d << ' ';
    }
    cout << '\n';
    return 0;
}