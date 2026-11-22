#include <iostream>
#include <iomanip>

int main() {
    int first, second;
    if (!(std::cin >> first >> second)) return 1;
    long long a = first;
    long long b = second;
    if (b == 0) {
        std::cout << "Деление на ноль не определено .\n";
        return 0;
    }

    long long integer = a / b;
    double quotient = static_cast<double>(a) / b;
    std::cout << "a / b = " << integer << '\n';
    std::cout << std::setprecision(16) << "static_cast<double>(a) / b = " << quotient << '\n';
    std::cout << "Результаты совпадают: " << std::boolalpha << (a % b == 0) << '\n';
}
