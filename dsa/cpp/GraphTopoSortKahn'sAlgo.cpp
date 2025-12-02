#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> topoSortKahn(int V, vector<vector<int>> &adj) {
    vector<int> inDegree(V, 0);


    for (int i = 0; i < V; i++) {
        for (int nbr : adj[i]) {
            inDegree[nbr]++;
        }
    }

    queue<int> q;
    for (int i = 0; i < V; i++) {
        if (inDegree[i] == 0)
            q.push(i);
    }


    vector<int> topo;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        topo.push_back(node);

      
        for (int nbr : adj[node]) {
            inDegree[nbr]--;
            if (inDegree[nbr] == 0)
                q.push(nbr);
        }
    }

    return topo;
}

int main() {
    int V = 6;
    vector<vector<int>> adj(V);

    adj[5] = {0, 2};
    adj[4] = {0, 1};
    adj[2] = {3};
    adj[3] = {1};

    vector<int> ans = topoSortKahn(V, adj);

    cout << "Topological Sort (Kahn's Algorithm): ";
    for (int x : ans)
        cout << x << " ";
    cout << endl;
}
