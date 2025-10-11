#include <stdio.h>

int binarySearch(int arr[], int left, int right, int key) {
    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == key)
            return mid; // Found
        else if (arr[mid] < key)
            left = mid + 1; // Search right half
        else
            right = mid - 1; // Search left half
    }
    return -1; // Not found
}

int main() {
    int arr[] = {14, 16, 33, 37, 47, 87, 99}; // Must be sorted!
    int size = sizeof(arr) / sizeof(arr[0]);
    int key = 47;

    int result = binarySearch(arr, 0, size - 1, key);
    if (result != -1)
        printf("Element %d found at index %d\n", key, result);
    else
        printf("Element %d not found\n", key);

    return 0;
}
