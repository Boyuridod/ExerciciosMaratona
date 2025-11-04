// https://codeforces.com/contest/2123/problem/C

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

void exercicio(){

    int n = 0, i = 0;
    int min = INF, max = EPS;

    cin >> n;

    vector<int> a(n, 0);
    vector<bool> pre(n, false), suf(n, false);

    for(i = 0; i < n; i++){
        cin >> a[i];
        if(a[i] < min){
            min = a[i];
            pre[i] = true;
        }
    }

    for(i = n - 1; i >= 0; i--){
        if(a[i] > max){
            max = a[i];
            suf[i] = true;
        }
    }

    for(i = 0; i < n; i++){
        if(pre[i] or suf[i]){
            cout << 1;
        }
        else{
            cout << 0;
        }
    }

    cout << endl;
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