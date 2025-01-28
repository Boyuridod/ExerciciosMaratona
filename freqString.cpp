// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/I

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0, i = 0, j = 0;
    string word = "";

    cin >> word;

    cin >> N;

    for(N = N; N > 0; N--){

        int num = 0, cont = 0, aux = 0;
        string teste = "";

        cin >> num >> teste;

        for(i = 0; i < word.size() - teste.size(); i++){

            for(j = 0; j < teste.size(); j++){

                if(word[i] == teste[j]){

                    aux++;

                }

                else{

                    j = teste.size();

                }

            }

            cont = (int)(aux / teste.size());

        }

        if(cont < num)
            cout << -1 << endl;
        else
            cout << cont << endl;

    }

    return 0;
}