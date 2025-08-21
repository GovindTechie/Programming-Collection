# include<iostream>

using namespace std;

struct Node {
    int data;
    Node *left;
    Node *right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

int height(Node *root) {
    if(root == nullptr)
        return 0;

    int leftHeight = height(root -> left);
    int rightHeight = height(root -> right);

    return 1 + max(leftHeight, rightHeight);
}


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

    cout << "Height of the tree: " << height(root) << endl; 
}