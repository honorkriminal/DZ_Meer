#include <iostream>

int main() {
    int first, second;
    if (!(std::cin >> first >> second)) return 1;
    long long a = first;
    long long b = second;

    std::cout << "a + b = " << (a + b) << '\n';
    std::cout << "a - b = " << (a - b) << '\n';
    std::cout << "a * b = " << (a * b) << '\n';

    long long copy = a;
    copy += b;
    std::cout << "a += b: " << copy << '\n';
    copy = a;
    copy -= b;
    std::cout << "a -= b: " << copy << '\n';
    copy = a;
    copy *= b;
    std::cout << "a *= b: " << copy << '\n';

    if (b == 0) {
        std::cout << "Деление и остаток от деления на ноль не определены .\n";
        return 0;
    }
    std::cout << "a / b = " << (a / b) << '\n';
    std::cout << "a % b = " << (a % b) << '\n';
    copy = a;
    copy /= b;
    std::cout << "a /= b: " << copy << '\n';
    copy = a;
    copy %= b;
    std::cout << "a %= b: " << copy << '\n';
}
