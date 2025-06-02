// https://codeforces.com/contest/2116/problem/B

#include<bits/stdc++.h>

using namespace std;

typedef long long longo;

const long long mod = 998244353;

longo somaMod(longo a, longo b) {
    return (a + b) % mod;
}

longo multMod(longo a, longo b) {
    return (a * b) % mod;
}

longo exponenciacaoRapida(longo base, longo expoente) {
    if(expoente == 0) return 1;
    if(expoente == 1) return base % mod;
    if(expoente % 2 == 0){
        longo aux = exponenciacaoRapida(base, expoente / 2);
        return multMod(aux, aux);
    }
    else{
        longo aux = exponenciacaoRapida(base, (expoente - 1) / 2);
        return multMod(multMod(aux, aux), base);
    }
}

void exercicio() {

    int n = 0, i = 0, j = 0;
    longo maximo = 0, r = 0;

    cin >> n;

    vector<longo> v(n);
    vector<longo> v2(n);

    for(i = 0; i < n; i++){

        cin >> v[i];

    }

    for(i = 0; i < n; i++){

        cin >> v2[i];

    }

    for(i = 0; i < n; i++){

        for(j = 0; j <= i; j++){

            r = somaMod(exponenciacaoRapida(2, v[j]), exponenciacaoRapida(2, v2[i - j]));

            // cout << v[j] << " " << v2[i - j] << endl;
            // cout << exponenciacaoRapida(2, v[j]) << " " << exponenciacaoRapida(2, v2[i - j]) << endl << endl;

            if(j == 0 or maximo < r){
                maximo = r;
            }

        }

        cout << maximo << " ";

    }

    cout << endl;
    
}

int main(){

    int N = 0;

    cin >> N;

    while (N--){
        exercicio();
    }

    return 0;
}