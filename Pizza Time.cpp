// https://codeforces.com/contest/2156/problem/A

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int exercicio(){

    longo pedacos = 0, m1 = 0, m2 = 0, div = 0, resto = 0;

    cin >> pedacos;

    // while(pedacos > 0){

    //     printf("[DEBUG] %lld %lld %lld\n", m1, m2, pedacos);

    //     if(pedacos < 3){
    //         m2 += pedacos;
    //         pedacos = 0;
    //     }

    //     else{
    //         div = floor(pedacos / 3);
    //         resto = pedacos % 3;
    //         m1 += div;
    //         m2 += div + floor(resto / 2.0);
    //         pedacos = div + ceil(resto / 2.0);
    //     }
    // }

    // printf("[DEBUG] %lld %lld %lld\n", m1, m2, pedacos);

    m1 = floor((pedacos - 1) / 2);

    return m1;
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0;

    cin >> t;

    while (t--){

        cout << exercicio() << endl;

    }

    return 0;
}