#include <iostream>
#include <cmath>

using namespace std;

bool ehPrimo(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 3; i <= sqrt(n); i+2) {
        if (n % i == 0) return false;
    }
    return true;
}

void fatorarOtimizado(int n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (ehPrimo(i) && n % i == 0) {
            while (n % i == 0) {
                cout << i << " ";
                n /= i;
            }
        }
    }
    if (n > 1) {
        cout << n << " ";
    }
    cout << endl;
}

int main() {
    int num;
    cout << "Digite o número a ser fatorado: ";
    cin >> num;
    cout << "Fatores primos de " << num << ": ";
    fatorarOtimizado(num);
    return 0;
}