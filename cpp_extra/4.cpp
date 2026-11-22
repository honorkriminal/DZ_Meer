#include <iostream>

int main() {
    int big = 300;
    char small = big;
    double d = 3.99;
    int i = d;

    std::cout << "big = " << big << ", " << sizeof(big) << " байт\n";
    std::cout << "small = " << static_cast<int>(small) << ", " << sizeof(small) << " байт\n";
    std::cout << "d = " << (d) << '\n';
    std::cout << "i = " << (i) << '\n';
}
