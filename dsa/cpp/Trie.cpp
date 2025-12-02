#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    bool isEnd;
    TrieNode() {
        isEnd = false;
        for(int i = 0; i < 26; i++) children[i] = nullptr;
    }
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }

    void insert(string word) {
        TrieNode* node = root;
        for(char c : word) {
            int idx = c - 'a';
            if(!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        TrieNode* node = root;
        for(char c : word) {
            int idx = c - 'a';
            if(!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        TrieNode* node = root;
        for(char c : prefix) {
            int idx = c - 'a';
            if(!node->children[idx]) return false;
            node = node->children[idx];
        }
        return true;
    }
};

int main() {
    Trie trie;
    trie.insert("cat");
    trie.insert("cap");
    trie.insert("car");
    trie.insert("dog");

    cout << trie.search("cap") << endl;      // 1 (true)
    cout << trie.search("ca") << endl;       // 0 (false)
    cout << trie.startsWith("ca") << endl;   // 1 (true)
    cout << trie.startsWith("do") << endl;   // 1 (true)
}
