// https://codeforces.com/contest/2123/problem/D

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

string exercicio(){

    int n = 0, k = 0, i = 0, transformar = 0;

    cin >> n >> k;

    string s;

    cin >> s;

    for(i = 0; i < n; i++){
        if(s[i] == '1'){
            transformar++;
        }
    }

    if(transformar > k and (int)(n / 2) >= k){
        return "Bob";
    }

    return "Alice";
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