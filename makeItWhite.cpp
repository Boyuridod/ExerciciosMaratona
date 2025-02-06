// https://codeforces.com/problemset/problem/1927/A

#include <bits/stdc++.h>

typedef long long longo;

#define mod longo(1e9+7)

using namespace std;

int main(){

    int N = 0, aux = 0, primeiro = INT_MAX, ultimo = INT_MIN;
    string linha = "";

    cin >> N;

    while(N--){

        primeiro = INT_MAX; ultimo = INT_MIN;

        cin >> aux;

        cin >> linha;

        while(aux--){

            if(linha[aux] == 'B'){

                if(aux < primeiro) primeiro = aux;

                if(aux > ultimo) ultimo = aux;

            }

        }

        cout << ultimo - primeiro + 1 << endl;

    }

    return 0;

}