#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if (root == nullptr) {
            return nullptr;
        }
        if (root->val == val) {
            return root;
        }

        if (root->val < val) {
            return searchBST(root->right, val);  // RETURN this
        } else {
            return searchBST(root->left, val);   // RETURN this
        }
    }
};


void printSubtree(TreeNode* node) {
    if (!node) return;
    cout << node->val << " ";
    printSubtree(node->left);
    printSubtree(node->right);
}

int main() {
    // Construct this tree:
    //        5
    //       / \
    //      3   7
    //     / \   \
    //    2   4   8

    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(7);
    root->left->left = new TreeNode(2);
    root->left->right = new TreeNode(4);
    root->right->right = new TreeNode(8);

    Solution solver;
    int val = 7; // Change this to test other values
    TreeNode* result = solver.searchBST(root, val);

    if (result) {
        cout << "Subtree with root " << val << ": ";
        printSubtree(result); // prints the subtree starting from that node
    } else {
        cout << "Value not found in BST.";
    }

    return 0;
}
