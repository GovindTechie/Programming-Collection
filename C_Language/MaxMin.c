//  this is program to find maximum and minimum of arrary elements

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int main() {
    int arr[] = {33, 87, 16, 47, 14, 99, 37};
    int size = sizeof(arr)/sizeof(arr[0]);

    int max = INT_MIN;
    int min = INT_MAX;
    for (size_t i=0; i<size; i++){
        if(max < arr[i]) {
            max = arr[i];
        }
        if(min > arr[i]) {
            min = arr[i];
        }

    }
    printf("The array elements are : ");
    for(int i=0; i<size; i++) {
        printf("%d ", arr[i]);
    }


    printf("\nThe maximum elemnt from array is %d\n"
        "The minimum element from array is %d", max, min);

    return 0;
}

