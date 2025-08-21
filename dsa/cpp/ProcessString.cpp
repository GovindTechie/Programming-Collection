# include <iostream>
# include <string>
# include <algorithm>
using namespace std;

class Solution {
public:
    string processStr(string s) {
        string result = "";
        int lenght = s.length();
        for(int i=0; i<lenght; i++) {
            if(s[i] >= 'a' && s[i] <= 'z') {
                result += s[i];
            }
            if(s[i] == '*' && !result.empty()) {
                result.pop_back();
            }
            if(s[i] == '#' && !result.empty()) {
                result += result;
            } 
            if(s[i] == '%' && result.length() > 1) {
                reverse(result.begin(), result.end());
            }
        }
        return result;
    }
};


int main () {
    Solution solver;
    string s = "a#b%*";
    cout << "Original String is : " << s << endl;
    cout << "Processed String is : " << solver.processStr(s) << endl;

    return 0;
}