// https://codeforces.com/problemset/problem/2148/B

#include <bits/stdc++.h>

using namespace std;

int exercicio(){

    int n = 0, m = 0, x = 0, y = 0;
    int contx = 0, conty = 0, i = 0;

    cin >> n >> m >> x >> y;

    vector<int> y_lazers(n, 0), x_lazers(m, 0);

    for(i = 0; i < n; i++){
        cin >> y_lazers[i];

        if(y_lazers[i] <= y) conty++;
    }

    for(i = 0; i < m; i++){
        cin >> x_lazers[i];

        if(x_lazers[i] <= x){
            contx++;
        }
    }

    return contx+conty;

}

int main(){

    int T = 0;

    cin >> T;

    while (T--){

        cout << exercicio() << endl;

    }

    return 0;

}