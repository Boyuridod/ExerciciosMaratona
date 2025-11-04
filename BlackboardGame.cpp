// https://codeforces.com/contest/2123/problem/A

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

vector<bool> primos(100, true);

void crivo(int num = 100){
    primos[0] = false;
    primos[1] = false;

    for(int i = 2; i <= num; i++){
        if(primos[i]){
            for(int j = i*i; j <= num; j += i){
                primos[j] = false;
            }
        }
    }
}

string exercicio(){

    int num = 0;

    cin >> num;

    if(num%4){
        return "Alice";
    }

    else{
        return "Bob";
    }
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    crivo();

    int t = 0;

    cin >> t;

    while (t--){

        cout << exercicio() << endl;

    }

    return 0;
}