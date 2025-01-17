# include <iostream>
# include <vector>

using namespace std;

int main () {
    vector<int>vec;

    cout << "Size = " << vec.size() << endl;

    vec.push_back(25);
    vec.push_back(27);
    vec.push_back(54);
    vec.push_back(12);
    
    cout << "After push Size = " << vec.size() << endl;
    vec.pop_back();
    cout << vec.front() << endl << vec.back() << endl;

    cout << vec[2] << vec.at(1) << endl;
    return 0;
}