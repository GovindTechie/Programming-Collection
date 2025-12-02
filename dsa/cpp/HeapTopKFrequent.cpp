#include <bits/stdc++.h>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int,int> freq;
    for(int n : nums) freq[n]++;

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;

    for(auto& p : freq) {
        minHeap.push({p.second, p.first});
        if(minHeap.size() > k) minHeap.pop();
    }

    vector<int> res;
    while(!minHeap.empty()) {
        res.push_back(minHeap.top().second);
        minHeap.pop();
    }
    reverse(res.begin(), res.end());
    return res;
}

int main() {
    vector<int> nums = {1,1,1,2,2,3};
    int k = 2;
    vector<int> ans = topKFrequent(nums, k);
    for(int x : ans) cout << x << " ";
}
