# include<iostream>
# include<vector>
# include<queue>

using namespace std;

bool isCycleBFS(int start, vector<vector<int>> &adj, vector<int> &visited) {
    queue<pair<int, int>> q; // (node, parent)
    visited[start] = 1;
    q.push({start, -1});

    while (!q.empty()) {
        int node = q.front().first;
        int parent = q.front().second;
        q.pop();

        for (int nbr : adj[node]) {
            if (!visited[nbr]) {
                visited[nbr] = 1;
                q.push({nbr, node});
            }
            else if (nbr != parent) {
                // visited neighbor which isn't parent → cycle
                return true;
            }
        }
    }
    return false;
}

bool checkCycle(int V, vector<vector<int>> &adj) {
    vector<int> visited(V, 0);
    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            if (isCycleBFS(i, adj, visited))
                return true;
        }
    }
    return false;
}

int main() {
    int V = 5;
    vector<vector<int>> adj(V);

    // undirected graph with a cycle
    adj[0] = {1, 2};
    adj[1] = {0, 2};
    adj[2] = {0, 1, 3};
    adj[3] = {2, 4};
    adj[4] = {3};

    if (checkCycle(V, adj))
        cout << "Cycle detected (BFS)" << endl;
    else
        cout << "No cycle found" << endl;
}