// these is program for intersection of two array 

# include <iostream>
using namespace std;

void intersectionFind (int arr1[], int arr2[], int size1, int size2) {
    for (int i=0; i<size1; i++) {
        for (int j=0; j<size2; j++) {
            if(arr1[i] == arr2[j]) {
                cout << arr1[i] << " ";
                break;
            }
        }
    }
}

int main(){
    int arr1[] = {2,6,4,2,9,23,2,86,86};
    int arr2[] = {1,2,3,5,6,22};

    int size1 = 6;
    int size2 = 6;

    // removing repeated element from array1 
    for (int i=0; i<size1; i++) {
        for (int j=0; j<size1; j++) {
            if(arr1[i] == arr1[j] && i!=j) {
                // after finding element with repeat value we are shifting array element 
                // and decreasing size of element
                for(int i=j; i<size1; i++) {
                    arr1[i] = arr1[i+1];
                }
                size1--;
                j--; // after shifting element we need to decrease j to check next element
            }
        }
    }

    intersectionFind (arr1, arr2, size1, size2);


    return 0;
}