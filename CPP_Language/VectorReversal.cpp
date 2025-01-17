// below is code for vector element traversal

# include<iostream>
# include<vector>
using namespace std;

void VectorReversal (vector <int> &vec) {
    int start = 0, end = vec.size()-1;

    while(start < end) {
        swap(vec[start], vec[end]);
        start ++;
        end --;
    }
}


int main() {
    vector <int> vec = {2, 53, 23, 53, 43, 64, 12, 7};
    VectorReversal(vec);

    cout << endl;
    for (int i=0; i<vec.size(); i++) {   
        cout << vec[i] << " ";
    }
    return 0;
}