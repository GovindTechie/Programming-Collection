#include <iostream>
#include <vector>
#include <stack>
using namespace std;

void dfs(int node, vector<vector<int>> &adj, vector<int> &visited, stack<int> &st) {
    visited[node] = 1;
    for (int nbr : adj[node]) {
        if (!visited[nbr]) {
            dfs(nbr, adj, visited, st);
        }
    }
    st.push(node);  // after visiting all neighbors
}

vector<int> topoSort(int V, vector<vector<int>> &adj) {
    vector<int> visited(V, 0);
    stack<int> st;

    for (int i = 0; i < V; i++) {
        if (!visited[i])
            dfs(i, adj, visited, st);
    }

    vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
    }
    return result;
}

int main() {
    int V = 6;
    vector<vector<int>> adj(V);

    adj[5] = {0, 2};
    adj[4] = {0, 1};
    adj[2] = {3};
    adj[3] = {1};

    vector<int> ans = topoSort(V, adj);

    cout << "Topological Sort Order: ";
    for (int x : ans)
        cout << x << " ";
    cout << endl;
}
