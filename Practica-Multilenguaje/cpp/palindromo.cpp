#include <iostream>
#include <algorithm>
#include <cctype>

bool esPalindromo(std::string texto) {
    std::string limpio = "";
    for (char c : texto) {
        if (isalnum(c)) limpio += tolower(c);
    }
    std::string reverso = limpio;
    std::reverse(reverso.begin(), reverso.end());
    return limpio == reverso;
}

int main() {
    std::string cadena = "Anita lava la tina";
    if (esPalindromo(cadena)) {
        std::cout << "Es un palíndromo" << std::endl;
    } else {
        std::cout << "No es un palíndromo" << std::endl;
    }
    return 0;
}