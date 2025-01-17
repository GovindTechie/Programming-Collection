# include <iostream>
using namespace std;

int main () {
    int arr[5];
    int size = sizeof(arr)/sizeof(int);
    cout << "Enter array elemens with size " << size << endl;
    for (int i=0; i<size; i++) {
        cin >> arr[i];
    }
    cout << endl;
    cout << "Array elements are" << endl;
    for (int i=0; i<size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // for finding smallest number in array
    int smallest = INT_MAX;
    int largest = INT_MIN;
    int smallestIndex;
    int largestIndex;
    for (int i=0; i<size; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
            smallestIndex = i;
        }
        if (arr[i] > largest) {
            largest = arr[i];
            largestIndex = i;
        }
    }
    
    cout << "Smallest number is at index "<< smallestIndex<< " and it is : " << smallest << endl;
    cout << "Largest number is at index "<< largestIndex<< " and it is : " << largest << endl;

}