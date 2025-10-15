// https://codeforces.com/contest/2116/problem/B

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 998244353; // Primo

map<string, longo> potencia;

longo somaMod(longo a, longo b) {
    return (a + b) % mod;
}

longo multMod(longo a, longo b) {
    return (a * b) % mod;
}

longo exponenciacaoRapida(longo base, longo expoente) {
    cout << base + "^" + expoente << endl;
    if(potencia[(char)base + "^" + (char)expoente] != 0){
        return potencia[(char)base + "^" + (char)expoente];
    }
    else{
        if(expoente == 0) return 1;
        if(expoente == 1) return base;
        if(expoente % 2 == 0){
            longo aux = exponenciacaoRapida(base, expoente / 2);
            return multMod(aux, aux);
        }
        else{
            longo aux = exponenciacaoRapida(base, (int)(expoente / 2) + 1);
            return multMod(multMod(aux, aux), base);
        }
    }
}

void exercicio(){

    int n = 0, i = 0, j = 0;
    longo maximo = 0, raux = 0;

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
        maximo = 0;
        for(j = 0; j <= i; j++){
            // cout << exponenciacaoRapida(2, v[j]) << " " << exponenciacaoRapida(2, v2[i - j]) << " " << v[j] << " " << v[i-j] << endl;
            raux = somaMod(exponenciacaoRapida(2, v[j]), exponenciacaoRapida(2, v2[i - j]));
            if(raux > maximo){
                maximo = raux;
            }
        }

        // cout << maximo << " " << endl;
    }

    cout << endl;
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    potencia["2^0"] = 1;

    int t = 0;

    cin >> t;

    while (t--){

        exercicio();

    }

    // cout << potencia["2^2"] << endl;

    return 0;
}