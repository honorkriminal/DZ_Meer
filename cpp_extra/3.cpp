#include <iostream>

int main() {
    int x, y;
    if (!(std::cin >> x >> y)) return 1;

    std::cout << std::boolalpha;
    std::cout << "x == y = " << (x == y) << '\n';
    std::cout << "x != y = " << (x != y) << '\n';
    std::cout << "x < y = " << (x < y) << '\n';
    std::cout << "x > y = " << (x > y) << '\n';
    std::cout << "x <= y = " << (x <= y) << '\n';
    std::cout << "x >= y = " << (x >= y) << '\n';
    std::cout << "(x > 0) && (y > 0) = " << ((x > 0) && (y > 0)) << '\n';
    std::cout << "(x > 0) || (y > 0) = " << ((x > 0) || (y > 0)) << '\n';
    std::cout << "!(x == y) = " << (!(x == y)) << '\n';
}
