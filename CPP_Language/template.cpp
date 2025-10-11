template<typename T>
class Box {
public:
    T value;
    Box(T v) {
        value = v;
    }
    T get () {
        return value;
    }
};


int main() {
    Box<int> intBox(5);       // T = int
    Box<double> doubleBox(3.14); // T = double

    cout << intBox.get() << "\n";   // prints 5
    cout << doubleBox.get() << "\n"; // prints 3.14
}