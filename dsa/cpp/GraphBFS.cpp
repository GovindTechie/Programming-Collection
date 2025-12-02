# include<iostream>
# include<vector>
# include<queue>

using namespace std;

void bfs(int start, vector<vector<int>> &adj, int V) {
    vector<int> visited(V, 0);
    queue<int>q;

    visited[start] = 1;
    q.push(start);

    cout << "BFS Traversal: ";

    while(!q.empty()) {
        int node = q.front();
        q.pop();

        cout << node << " ";

        for(int nbr: adj[node]) {
            if(!visited[nbr]) {
                visited[nbr] = 1;
                q.push(nbr);
            }
        }
    }
}



int main() {
    int V = 5;
    vector<vector<int>> adj(V);

    adj[0] = {1, 3};
    adj[1] = {0, 2};
    adj[2] = {1, 4};
    adj[3] = {0, 4};
    adj[4] = {2, 3};

    bfs(0, adj, V);

    return 0;
}