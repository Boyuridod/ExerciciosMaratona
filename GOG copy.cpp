#include <bits/stdc++.h>

using namespace std;

#define endl endl << flush

void printaMatriz(vector<vector<int>> matriz)
{

    int i = 0, j = 0, N = 0;

    N = matriz.size();

    for (i = 0; i < N; i++)
    {

        for (j = 0; j < N; j++)
        {

            cout << matriz[i][j] << " ";
        }

        cout << endl;
    }
}

int main()
{

    int N = 0, i = 0, j = 0, k = 0, soma = 0, objetivo = 0, cl = 0, x = 0, y = 0;

    cin >> N;

    // int board[N][N];

    vector<vector<int>> board(N, vector<int>(N));
    vector<int> linha(N, 0);
    vector<int> coluna(N, 0);

    for (i = 0; i < N; i++)
    {

        for (j = 0; j < N; j++)
        {

            cin >> board[i][j];
        }
    }

    // // Debug
    // printaMatriz(board);

    for (k = N; k > 1; k--)
    {
        // Jogador 1 | Coluna [j]

        objetivo = 100000;

        for(i = 0; i < N; i++){

            for(j = 0; j < N; j++){

                if(coluna[i] == 0 && linha[j] == 0){

                    if(objetivo > board[i][j]){

                        objetivo = board[i][j];

                        cl = i;

                    }

                }

            }

        }

        coluna[cl]++;

        // // Debug
        // cout << cl << " " << objetivo << " ";

        // Jogador 2 | Linha [i]

        objetivo = 0;

        for (i = 0; i < N; i++){
            soma = 0;

            for(j = 0; j < N; j++){

                if(linha[i] == 0 && coluna[j] == 0){

                    if(objetivo < board[j][i]){

                        objetivo = board[j][i];

                        cl = i;

                    }

                }

            }

        }

        linha[cl]++;

        // // Debug
        // cout << cl << " " << objetivo << endl;

        // // Debug
        // for(i = 0; i < N; i++){

        //     cout << coluna[i] << endl;

        // }

        // for(i = 0; i < N; i++){

        //     cout << linha[i] << " ";

        // }

        // cout << endl;
        
    }

    // Saida

    for (i = 0; i < N; i++)
    {

        if (linha[i] == 0)
        {
            y = i;
        }

        if (coluna[i] == 0)
        {
            x = i;
        }
    }

    // // Debug
    // cout << x << " " << y << " ";    

    cout << board[x][y] << endl;
}