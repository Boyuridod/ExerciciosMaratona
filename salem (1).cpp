// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/N

// Fazer um monte de testes igual o Bruno Monteiro ensinou

#include <bits/stdc++.h>

using namespace std;

string toBinario(int converter){

    string convertido = "";

    if(converter > 1)
        convertido += toBinario(floor(converter/2));

    convertido += to_string(converter % 2);

    return convertido;

}

string to16bits(string converter){

    int i = 16 - converter.size();

    while(i--){

        converter = "0" + converter;

    }

    return converter;

}

int main(){

    int i = 0, j = 0, k = 0, T = 0, N = 0, num = 0;

    cin >> T;

    for(i = 0; i < T; i++){

        int cont = 0;
        vector<string> binario;

        cin >> N;

        for(j = 0; j < N; j++){

            cin >> num;

            binario.push_back(to16bits(toBinario(num)));

        }

        for(j = 1; j < N; j++){

            for(k = 0; k < binario[j].size(); k++){

                if(binario[0][k] != binario[j][k] && binario[0][k] != 'X'){

                    cont++;

                    binario[0][k] = 'X';

                }

            }

        }

        cout << cont << endl;

    }

    return 0;

}