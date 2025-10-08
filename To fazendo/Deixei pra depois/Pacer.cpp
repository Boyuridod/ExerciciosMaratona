// https://codeforces.com/problemset/problem/2148/C

#include <bits/stdc++.h>

using namespace std;

int exercicio(){

    int n = 0, m = 0, i = 0;

    cin >> n >> m;

    vector<vector<int>> a(n, vector<int> (2, 0));

    for(i = 0; i < n; i++){
        cin >> a[i][0] >> a[i][1];
    }

}

int main(){

    int T = 0;

    cin >> T;

    while (T--){

        cout << exercicio() << endl;

    }

    return 0;

}