#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

bool isBalanced(const string& expr) {
    unordered_map<char, char> bracketMap = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    };

    vector<char> stack;

    for (char ch : expr) {
        // Opening brackets
        if (ch == '(' || ch == '{' || ch == '[') {
            stack.push_back(ch);
        }
        // Closing brackets
        else if (bracketMap.count(ch)) {
            if (stack.empty() || stack.back() != bracketMap[ch]) {
                return false;
            }
            stack.pop_back();
        }
    }

    return stack.empty(); // If empty, all brackets matched correctly
}

int main() {
    string input;
    cout << "Enter expression: ";
    cin >> input;

    if (isBalanced(input))
        cout << "Balanced\n";
    else
        cout << "Not Balanced\n";

    return 0;
}
