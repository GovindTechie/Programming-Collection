#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> heap;

    void heapifyDown(int i) {
        int n = heap.size();
        int largest = i;
        int left = 2*i + 1;
        int right = 2*i + 2;

        if(left < n && heap[left] > heap[largest])
            largest = left;
        if(right < n && heap[right] > heap[largest])
            largest = right;

        if(largest != i) {
            swap(heap[i], heap[largest]);
            heapifyDown(largest);
        }
    }

    void heapifyUp(int i) {
        if(i == 0) return;
        int parent = (i - 1)/2;
        if(heap[parent] < heap[i]) {
            swap(heap[parent], heap[i]);
            heapifyUp(parent);
        }
    }

public:
    void insert(int val) {
        heap.push_back(val);
        heapifyUp(heap.size() - 1);
    }

    void removeMax() {
        if(heap.empty()) return;
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
    }

    int getMax() {
        return heap.empty() ? -1 : heap[0];
    }

    void printHeap() {
        for(int v : heap) cout << v << " ";
        cout << endl;
    }
};

int main() {
    MaxHeap h;
    h.insert(10);
    h.insert(30);
    h.insert(20);
    h.insert(5);
    h.printHeap(); // shows heap structure
    cout << "Max: " << h.getMax() << endl;
    h.removeMax();
    h.printHeap();
}
