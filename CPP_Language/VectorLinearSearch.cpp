# include <iostream>
# include <vector>
using namespace std;

int LinearSearch(const vector <int> &vec,int n) {
    for(int i=0; i<vec.size(); i++) {
        if(vec[i] == n) {
            return i;
        }
    }
    return -1;
}
int main () {
    vector <int> vec = {23, 53, 12, 67, 25, 64, 34, 65, 76};
    int n;
    cout << "Enter number that you want to search in vector" << endl;
    cin >> n;
    int result = LinearSearch(vec, n);
    if(result != -1) {
        cout << "Element found at index " << result; 
    }
    else {
        cout << "Element not found";
    }
    return 0;
}