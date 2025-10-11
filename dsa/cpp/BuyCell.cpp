#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector <int> arr = {7, 1, 5, 3, 6, 4};
    int maxProfit = 0, bestBuy = arr[0];
    for(int i=1; i<arr.size(); i++) {
        if(arr[i] > bestBuy) {
            maxProfit = max(maxProfit, arr[i] - bestBuy);
        }

        bestBuy = min(bestBuy, arr[i]);

    }
    cout << "Max profit in buy and cell is : " << maxProfit << endl;
    return 0;
}
