// https://vjudge.net/contest/687522/problemPdf/D?descKey=2456279111465724

#include <bits/stdc++.h>

#define mod (int)(1e9 + 7)

using namespace std;

int mult(int x, int y){

    return (x * y) % mod;

}

int expon(int x, int y){

    int aux;

    if(y == 0){
        return 1;
    }

    else if(y == 1){

        return x;

    }

    else if(y % 2 == 0){

        aux = expon(x, y/2);
        return mult(aux, aux);

    }

    else{

        aux = expon(x, floor(y/2));

        return mult(mult(aux, aux), x);

    }

}

int main(){

    int N = 0, i = 0, j = 0, maior = INT_MIN;

    cin >> N;

    N = expon(N, 2);

    vector<int> mat(N, 0);
    // int mat[N] = {0};

    for(i = 0; i < N; i++){

        cin >> mat[i];

        if(mat[i] > maior){

            maior = mat[i];

        }

    }

    // // Debug

    // for(i = 0; i < N; i++){

    //     cout << mat[i] << " ";

    // }

    cout << endl;

    for(i = 0; i < N; i++){

        for(j = 0; j < N; j++){

            if(i != j && (mat[i] + mat[j]) > maior){

                maior = (mat[i] + mat[j]);

                // cout << maior << " " << mat[i] << " " << mat[j] << endl;

            }

        }

    }

    cout << maior << endl;

}