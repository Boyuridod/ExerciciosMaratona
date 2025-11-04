// https://codeforces.com/contest/2123/problem/B

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

string exercicio(){

    int n = 0, j = 0, k = 0, i = 0;
    int campeao = 0, qtt = 0;

    cin >> n >> j >> k;

    vector<int> jog(n, 0);

    for(i = 0; i < n; i++){
        cin >> jog[i];

        if(i + 1 == j){
            campeao = jog[i];
        }
    }

    sort(jog.rbegin(), jog.rend());

    for(i = 1; i < n; i++){
        if(jog[i] != campeao){
            jog[i] = 0;
            qtt++;
        }
    }

    // for(i = 0; i < n; i++){
    //     cout << jog[i] << " ";
    // }

    // cout << " | " << n - qtt << " " << k << " ";

    if(k > 1 or jog[0] == campeao){
        return "YES";
    }

    return "NO";
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