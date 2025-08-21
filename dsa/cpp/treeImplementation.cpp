# include<iostream>
# include<vector>

using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

void inorder(Node* root) {
    if(root == nullptr) return;
    inorder(root -> left);
    cout << root -> data << " ";
    inorder(root -> right);
}

void preorder(Node* root) {
    if(root == nullptr) return;
    cout << root -> data << " ";
    preorder(root -> left);
    preorder(root -> right);
}

void postorder(Node* root) {
    if(root == nullptr) return;
    postorder(root -> left);
    postorder(root -> right);
    cout << root -> data << " ";
}


int main() {
    // Manually building tree:
    /*
            1
           / \
          2   3
         / \
        4   5
    */

    Node* root = new Node(1);
    root -> left = new Node(2);
    root -> right = new Node(3);
    root -> left -> left = new Node(4);
    root -> left -> right = new Node(5);
    
    cout << "Inorder traversal : " << endl;
    inorder(root);
    cout << endl << "Preorder traversal : " << endl;
    preorder(root);
    cout << endl << "Postorder traversal : " << endl;
    postorder(root);

    return 0;
}