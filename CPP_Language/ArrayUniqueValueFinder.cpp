// program to print all unique value in the array

# include <iostream>
using namespace std;

void uniqueValueCalculator (int arr[], int size) {
    for (int i=0; i<size; i++) {
        for (int j=0; j<size; j++) {
            if (arr[i] == arr[j] && i!=j) {
                break;
                // this will break inner loop remaining iteration and continue the program  
            }
            // if inner loop goes to last iteration means there is no repeated element find  
            else if(j == (size-1)) {
                cout<< arr[i] << endl;
            }
        } 
        
    }
}

int main(){

    int arr[7] = {33, 54, 33, 65, 45, 45, 87};
    int size = 7;

    uniqueValueCalculator(arr, size);
    
    return 0;
}