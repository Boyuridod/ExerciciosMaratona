// https://codeforces.com/group/rjjThiaoxx/contest/641718/problem/C

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int MDC(int a, int b) {
    if (b==0) return a;
    return MDC(b,a%b);
}

int MMC(int a,int b){
    return a*b/MDC(a,b);
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int n = 0, paes = 0, i = 0;

    cin >> n;

    vector<int> cap(n);

    cin >> paes;

    for(i = 0; i < n; i++){
        cin >> cap[i];
    }

    longo mmc = cap[0];

    for(i = 1; i < n; i++){
        mmc = MMC(mmc, cap[i]);
    }

    double somatorio = 0;

    for(i = 0; i < n; i++){
        somatorio += mmc / cap[i];
    }

    longo t = ceil((paes * mmc)/somatorio);

    cout << t << endl;

    return 0;
}