#include <iostream>
#include <vector>
using namespace std;

class MinHeap {
    vector<int> heap;

    void heapifyDown(int i) {
        int n = heap.size();
        int smallest = i;
        int left = 2*i + 1;
        int right = 2*i + 2;

        if (left < n && heap[left] < heap[smallest])
            smallest = left;
        if (right < n && heap[right] < heap[smallest])
            smallest = right;

        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }

    void heapifyUp(int i) {
        if (i == 0) return;
        int parent = (i - 1) / 2;
        if (heap[parent] > heap[i]) {
            swap(heap[parent], heap[i]);
            heapifyUp(parent);
        }
    }
    
public:
    void insert(int val) {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }

    void removeMin() {
        if (heap.empty()) return;
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
    }

    int getMin() {
        return heap.empty() ? -1 : heap[0];
    }

    void printHeap() {
        for (int v : heap) cout << v << " ";
        cout << endl;
    }
};

int main() {
    MinHeap h;
    h.insert(10);
    h.insert(30);
    h.insert(20);
    h.insert(5);

    cout << "Min Heap: ";
    h.printHeap();

    cout << "Min: " << h.getMin() << endl;

    h.removeMin();
    cout << "After removing min: ";
    h.printHeap();
}
