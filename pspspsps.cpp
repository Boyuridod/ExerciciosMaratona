// https://codeforces.com/problemset/problem/2049/B

#include <bits/stdc++.h>

typedef long long longo;

#define mod longo(1e9+7)

using namespace std;

int main(){

    int N = 0, aux = 0;
    string psps = "";
    bool p = false, s = false;

    cin >> N;

    while(N--){

        p = false; s = false;

        cin >> aux;

        cin >> psps;

        if(psps[0] == 's') psps[0] = '.';

        if(psps[aux - 1] == 'p') psps[aux - 1] = '.';

        while(aux--){

            if(psps[aux] == 's') s = true;

            if(psps[aux] == 'p') p = true;

        }

        if(!(s && p)){

            cout << "YES" << endl;

        }

        else{

            cout << "NO" << endl;

        }

    }

    return 0;

}