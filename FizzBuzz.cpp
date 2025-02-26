#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'fizzBuzz' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

void fizzBuzz(int n) {
    if(n % 3 == 0 && n % 5 == 0)
        cout << "FizzBuzz" << endl;
    else if(n % 3 == 0 && n % 5 != 0)
        cout << "Fizz" << endl;
    else if(n % 3 != 0 && n % 5 == 0)
        cout << "Buzz" << endl;
    else
        cout << n << endl;
}

int main(){

    int n = 0;
    bool rodando = true;

    // Enquanto houver entrada válida, continue lendo
    while (cin >> n) {
        fizzBuzz(n);
    }

    return 0;
}