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
    vector<vector<int>> adj(V);
    adj[0] = {1, 2};
    adj[1] = {0};
    adj[2] = {0};
    adj[3] = {4};
    adj[4] = {3};

    vector<int> visited(V, 0);
    int count = 0;
    
    cout << "Connected Components : " << endl;
    for(int i=0; i<V; i++) {
        if(!visited[i]) {
           count++;
           cout << "Component " << count << " : ";
           dfs(i, adj, visited);
           cout << endl; 
        }
    }
    return 0;
}