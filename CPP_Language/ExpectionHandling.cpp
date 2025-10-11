#include <iostream>
#include <stdexcept>

class Resource {
public:
    Resource(){ std::cout << "Resource acquired\n"; }
    ~Resource(){ std::cout << "Resource released (destructor)\n"; }
};

int divide(int a, int b) {
    if (b == 0) throw std::runtime_error("division by zero");
    return a / b;
}

int main() {
    try {
        Resource r;
        std::cout << "Result: " << divide(10, 0) << '\n';
    }
    catch (const std::exception &e) {
        std::cout << "Caught exception: " << e.what() << '\n';
    }
    std::cout << "After try-catch\n";
    return 0;
}
