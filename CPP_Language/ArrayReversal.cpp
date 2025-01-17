// program for reversing array elements

# include <iostream>
using namespace std;


void reverseArray(int arrr[], int sz) {
    int start = 0, end = sz-1;

    while(start < end) {
        swap(arrr[start], arrr[end]);
        start++;
        end--;
    }
}

int main(){
    int arr[5] = {33, 53, 22, 6, 87};
    int size = 5;

    reverseArray(arr, size);

    for (int i=0; i<size; i++) {   
        cout << arr[i] << " ";
    }

    return 0;
}