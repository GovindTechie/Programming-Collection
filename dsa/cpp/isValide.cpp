# include<iostream>
# include<unordered_map>
# include<string>
# include<vector>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> bracketMap = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        
        vector <char> stack;
        for(int i=0; i<s.length(); i++) {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{') {
                stack.push_back(s[i]);
            }
            else {
                if(stack.empty() || bracketMap[s[i]] != stack.back()) {
                    return false;
                }
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};



int main() {
    string s = "()[]{}";
    Solution s1;
    cout << "Original String is : " << s << endl;
    bool isvalid = s1.isValid(s);
    if(isvalid) {
        cout << "The string matches paranthesis";
    }
    else {
        cout << "The string is not matching parenthesis";
    }

    return 0;
}