#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void shortestPathBFS(int V, vector<vector<int>> &adj, int src) {
    vector<int> dist(V, -1); // -1 = unvisited
    queue<int> q;

    dist[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int nbr : adj[node]) {
            if (dist[nbr] == -1) { // not visited
                dist[nbr] = dist[node] + 1;
                q.push(nbr);
            }
        }
    }

    cout << "Shortest distances from node " << src << ":\n";
    for (int i = 0; i < V; i++) {
        cout << "Node " << i << " → " << dist[i] << endl;
    }
}

int main() {
    int V = 6;
    vector<vector<int>> adj(V);

    adj[0] = {1, 3};
    adj[1] = {0, 2, 4};
    adj[2] = {1};
    adj[3] = {0, 4};
    adj[4] = {1, 3, 5};
    adj[5] = {4};

    shortestPathBFS(V, adj, 0);
}
