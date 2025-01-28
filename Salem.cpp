// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/N

#include <bits/stdc++.h>

using namespace std;

int main(){

    int T = 0, N = 0, aux = 0, i = 0, j = 0, k = 0;

    cin >> T;

    for(i = 0; i < T; i++){

        cin >> N;

        vector<string> vec(N);

        int cont = 0;

        for(j = 0; j < N; j++){

            cin >> aux;

            vec[i] = bitset<16>(aux).to_string();

            cout << vec[i] << endl;

        }

        // for(j = 1; j < N; j++){

        //     for(k = 0; k < 16; k++){

        //         if(vec[0][k] != vec[j][k] && vec[0][k] != 'X'){

        //             cont++;

        //             vec[0][k] = 'X';

        //         }

        //     }

        // }

        cout << cont << endl;

    }

    return 0;

}