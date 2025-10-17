// https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/K

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    longo t = 0, a, b = 0, soma = 0, possivel = 0, i = 0;

    cin >> t;

    for(i = 0; i < t; i++){
        cin >> a >> b;

        if(i == 0){
            soma = a;
            soma -= b;
            possivel = a;
        }

        if(i > 0){
            soma += a;
            
            if(possivel < soma) possivel = soma;
            
            if(i < t - 1) soma -= b;

            // if(soma >= 0) possivel = soma;
        }
        
    }

    cout << possivel << endl;

    return 0;
}