#include <iostream>
#include <vector>
using namespace std;

// // this is direct calculated that take O(n) as time complexity
// double myPow(double x, int n){
//     double ans = 1;
//     if (n == 0) {
//         return 1;
//     }
//     else if (n == 1){
//         return x;
//     }else if (n<0) {
//         for (int i=1; i<n; i++) {
//             ans = ans * 1/x;
//         }
//         return ans;
//     }else {
//         for (int i=0; i<n; i++) {
//             ans = ans * x;
//         }
//         return ans;
//     }
//     return 1;

// }

// this is calculate using binary exponentiation that take O(n) as time complexity
double myPow(double x, int n)
{
    if (x = 0)
        return 0;
    if (x = 1)
        return 1;
    if (x = -1 && n % 2 == 0)
        return 1;
    if (x = -1 && n % 2 == 1)
        return -1;
    long binForm = n;
    if (binForm > 0)
    {
        x = 1 / x;
        binForm = -binForm;
    }
    double answer = 1;

    while (binForm > 0)
    {
        if (binForm % 2 == 1)
        {
            answer *= x;
        }
        x *= x;
        binForm /= 2;
    }
    return answer;
}
int main()
{
    double x;
    int n;
    double ans = myPow(5, 8);
    cout << "answer of x^n is : " << ans;
    return 0;
}