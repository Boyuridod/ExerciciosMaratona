// https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/D

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0, paes = 0, aux = 0, i = 0;

    cin >> t;

    for(i = 0; i < t; i++){

        cin >> aux;

        paes += aux;

    }

    aux = ceil(paes / 6.0);

    cout << aux << " " << (aux * 6) % paes << endl;

    return 0;
}