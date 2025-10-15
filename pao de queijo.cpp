// https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/A

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)


int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int cvd, pdq = 0;

    cin >> cvd;

    cin >> pdq;

    if(pdq/cvd >= 2){
        cout << 1 << endl;
    }

    else{
        cout << 0 << endl;
    }

    return 0;
}