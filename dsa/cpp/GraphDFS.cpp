# include <iostream>
# include <vector>

using namespace std;

void dfs(int node, vector<vector<int>> &adj, vector<int> &visited) {
    visited[node] = 1;

    cout << node << " ";

    for(int nbr: adj[node]) {
        if(!visited[nbr]) {
            dfs(nbr, adj, visited);
        }
    }
}

int main () {
    int V = 5;
    vector<vector<int>> adj(5);

    adj[0] = {1, 3};
    adj[1] = {0, 2};
    adj[2] = {1, 4};
    adj[3] = {0, 4};
    adj[4] = {2, 3};

    vector<int> visited(V,0);
    dfs(0, adj, visited);
    return 0;
}