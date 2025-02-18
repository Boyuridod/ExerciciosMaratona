// https://codeforces.com/contest/2064/problem/C

#include <bits/stdc++.h>

using namespace std;

int modulo(int x){

    if(x >= 0)
        return x;
    else
        return x * -1;

}

int main(){

    int N = 0, k = 0;

    cin >> N;

    for(k = 0; k < N; k++){

        int coin = 0, qtt = 0, i = 0, aux = 0, pos = 0;

        cin >> qtt;

        vector<int> a;

        vector<int> vets;

        for(i = 0; i < qtt; i++){

            cin >> aux;

            a.push_back(aux);

        }

        aux = a[0];

        vets.push_back(aux);

        for(i = 1; i < qtt; i++){

            if(aux >= 0 && a[i] >= 0){

                vets[pos] += a[i];

            }

            else{

                aux = a[i];

                vets.push_back(aux);

            }

        }

        for(i = 0; i < vets.size(); i++){

            cout << vets[i] << " ";

        }

        cout << endl;

        cout << coin << endl;

    }

    return 0;

}
