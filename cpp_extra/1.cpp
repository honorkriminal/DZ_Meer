#include <iostream>

int main() {
    int age = 19;
    short semester = 2;
    long long population = 8100000000LL;
    unsigned int students = 24U;
    float temperature = 21.5f;
    double distance = 125.75;
    char group = 'A';
    bool enrolled = true;

    std::cout << std::boolalpha;
    std::cout << "int: " << age << ", " << sizeof(age) << " байт\n";
    std::cout << "short: " << semester << ", " << sizeof(semester) << " байт\n";
    std::cout << "long long: " << population << ", " << sizeof(population) << " байт\n";
    std::cout << "unsigned int: " << students << ", " << sizeof(students) << " байт\n";
    std::cout << "float: " << temperature << ", " << sizeof(temperature) << " байт\n";
    std::cout << "double: " << distance << ", " << sizeof(distance) << " байт\n";
    std::cout << "char: " << group << ", " << sizeof(group) << " байт\n";
    std::cout << "bool: " << enrolled << ", " << sizeof(enrolled) << " байт\n";
}
