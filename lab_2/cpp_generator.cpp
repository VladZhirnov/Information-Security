#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    srand(time(nullptr));
    const int length = 128;
    for (int i = 0; i < length; ++i) {
        int random_bit = rand() % 2; 
        std::cout << random_bit;
    }
    std::cout << std::endl;
    return 0;
}