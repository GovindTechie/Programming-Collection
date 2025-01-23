// Function to calculate the maximum hourglass sum in a 6x6 matrix
int hourglassSum(vector<vector<int>> arr) {
    vector<int> result;

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            int add = arr[i][j] + arr[i][j+1] + arr[i][j+2]   // Top row
                    + arr[i+1][j+1]                          // Middle element
                    + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]; // Bottom row

            result.push_back(add);
        }
    }

    auto a = max_element(result.begin(), result.end());
    return *a;
}
