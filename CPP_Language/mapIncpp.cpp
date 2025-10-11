#include <bits/stdc++.h>
using namespace std;
int main() {
    map<string,int> m;
    m["apple"] = 3;
    m["banana"] = 5;
    for (auto p : m)
        cout << p.first << " -> " << p.second << '\n';
}
