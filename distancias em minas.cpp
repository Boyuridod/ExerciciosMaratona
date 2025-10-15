// https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/J

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0, aux;
    longo soma = 0;

    cin >> t;

    while (t--){

        cin >> aux;

        soma += aux;

    }

    if(soma >= 500){
        cout << soma << endl << "Grande viagem" << endl;
    }
    else{
        cout << soma << endl << "Viagem curta" << endl;
    }

    return 0;
}