#include <bits/stdc++.h>
using namespace std;

typedef long long longo;

int main() {
    const longo N = 1000; // 10^7 — 10^9 é pesado demais
    vector<longo> vetor(N + 1);
    ofstream primos("primos.txt");

    if (!primos.is_open()) {
        cout << "Erro ao criar o arquivo!" << endl;
        return -1;
    }

    for (longo i = 0; i <= N; i++) vetor[i] = i;

    for (longo i = 2; i * i <= N; i++) {
        if (vetor[i] != 0) {
            for (longo j = i * i; j <= N; j += i) {
                vetor[j] = 0;
            }
        }
    }

    primos << "vector<longo> primos = {";
    bool first = true;
    for (longo i = 2; i <= N; i++) {
        if (vetor[i] != 0) {
            if (!first) primos << ", ";
            primos << i;
            first = false;
        }
    }
    primos << "};" << endl;

    cout << "Arquivo 'primos.txt' gerado com sucesso!" << endl;
    return 0;
}
