#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Binary tree node definition
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};

// Function that returns level order traversal as vector of vectors
vector<vector<int>> levelOrderTraversal(Node* root) {
    vector<vector<int>> result;

    if (root == nullptr) return result;

    queue<Node*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size();
        vector<int> currentLevel;

        for (int i = 0; i < levelSize; ++i) {
            Node* curr = q.front();
            q.pop();

            currentLevel.push_back(curr->data);

            if (curr->left != nullptr)
                q.push(curr->left);
            if (curr->right != nullptr)
                q.push(curr->right);
        }

        result.push_back(currentLevel);
    }

    return result;
}

int main() {
    // Creating a sample binary tree:
    //
    //        1
    //       / \
    //      2   3
    //     / \   \
    //    4   5   6

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(6);

    vector<vector<int>> traversalResult = levelOrderTraversal(root);

    // Printing the result
    cout << "Level Order Traversal:\n";
    for (const auto& level : traversalResult) {
        for (int val : level) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
