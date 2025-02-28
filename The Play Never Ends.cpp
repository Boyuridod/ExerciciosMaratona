// https://m1.codeforces.com/contest/2071/problem/A

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0;

    cin >> N;

    while (N--){

        int teste = 0;

        cin >> teste;

        if((teste - 1) % 3 == 0){

            cout << "YES" << endl;

        }

        else{

            cout << "NO" << endl;

        }

    }

    return 0;

}