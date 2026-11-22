#include <iostream>
#include <stdexcept>
#include <string>

int main() {
    std::string line;
    if (!std::getline(std::cin, line)) return 1;

    try {
        std::size_t end;
        int value = std::stoi(line, &end);
        if (line.find_first_not_of(" \t\r\n\v\f", end) != std::string::npos) {
            std::cout << "Требуется целое число .\n";
            return 1;
        }
        long long result = 3LL * value;
        std::cout << "Число: " << result << '\n';
        std::cout << "Строка: " << std::to_string(result) << '\n';
    } catch (const std::invalid_argument&) {
        std::cout << "Требуется целое число .\n";
        return 1;
    } catch (const std::out_of_range&) {
        std::cout << "Число вне диапазона int .\n";
        return 1;
    }
    std::cout << std::stod("3.14") << '\n';
}
