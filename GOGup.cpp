#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0, i = 0, j = 0, mint = 0;

    cin >> N;

    vector<vector<int>> board(N, vector<int>(N));
    vector<int> min(N);

    for(i = 0; i < N; i++){

        for(j = 0; j < N; j++){

            cin >> board[i][j];

        }

    }

    for(i = 0; i < N; i++){

        mint = INT_MAX;

        for(j = 0; j < N; j++){

            if(mint > board[i][j]){

                mint = board[i][j];

            }

        }

        min[i] = mint;

    }

    mint = INT_MIN;
    
    for(i = 0; i < N; i++){

        if(mint < min[i]){

            mint = min[i];

        }

    }

    cout << mint << endl;

    return 0;

}