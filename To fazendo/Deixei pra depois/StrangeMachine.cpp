// https://codeforces.com/contest/2156/problem/B

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

void exercicio(){

    longo n = 0, q = 0, i = 0, soma = 10, j = 0;
    string s;
    cin >> n >> q;

    vector<longo> a(q, 0);
    vector<longo> resp(q, 0);

    cin >> s;

    for(i = 0; i < q; i++){
        cin >> a[i];
    }

    for(i = 0; i < q; i++){
        while(a[i] > 0){
            for(j = 0; j < n; j++){
                if(a[i] == 0) break;
                if(s[j] == 'A'){
                    a[i] -= 1;
                }
                else{
                    a[i] = floor(a[i]/2);
                }
                resp[i] += 1;
            }
        }
        
        cout << resp[i] << endl;
    }
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0;

    cin >> t;

    while (t--){

        exercicio();

    }

    return 0;
}