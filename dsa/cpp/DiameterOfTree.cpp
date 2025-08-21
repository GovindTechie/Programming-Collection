#include<iostream>
using namespace std;

// Node structure for binary tree
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

class BinaryTree {
private:
    int maxDiameter;

    // Recursive helper to compute height and update diameter
    int height(Node* root) {
        if (root == nullptr) return 0;

        int leftHeight = height(root->left);
        int rightHeight = height(root->right);

        // Update max diameter at current node
        int localDiameter = leftHeight + rightHeight;
        if (localDiameter > maxDiameter)
            maxDiameter = localDiameter;

        // Return height of current node
        return 1 + max(leftHeight, rightHeight);
    }

public:
    BinaryTree() {
        maxDiameter = 0;
    }

    int getDiameter(Node* root) {
        maxDiameter = 0;
        height(root);
        return maxDiameter;
    }
};

int main() {
    /*
             1
            / \
           2   3
          / \
         4   5
    */

    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    BinaryTree tree;
    cout << "Diameter of Tree = " << tree.getDiameter(root) << endl;

    return 0;
}
