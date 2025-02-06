// https://vjudge.net/contest/689473#problem/A

#include <bits/stdc++.h>

using namespace std;

#define A 0
#define B 1
#define C 2
#define AB 3
#define AC 4
#define BC 5

int main(){

    int beleza = 0, i = 0;
    string palavra = "";
    vector<int> combinacao(6, 0);

    cin >> palavra;

    for(i = 0; i < palavra.size(); i++){

        if(palavra[i] == 'A'){

            if(combinacao[BC] >= 1){

                combinacao[BC]--;

                beleza++;

            }

            else if(combinacao[B] >= 1){

                combinacao[AB]++;

                combinacao[B]--;

            }

            else if(combinacao[C] >= 1){

                combinacao[AC]++;

                combinacao[C]--;

            }

            else{

                combinacao[A]++;

            }

        }

        else if(palavra[i] == 'B'){

            if(combinacao[AC] >= 1){

                combinacao[AC]--;

                beleza++;

            }

            else if(combinacao[A] >= 1){

                combinacao[AB]++;

                combinacao[A]--;

            }

            else if(combinacao[C] >= 1){

                combinacao[BC]++;

                combinacao[C]--;

            }

            else{

                combinacao[B]++;

            }

        }

        else if(palavra[i] == 'C'){

            if(combinacao[AB] >= 1){

                combinacao[AB]--;

                beleza++;

            }

            else if(combinacao[A] >= 1){

                combinacao[AC]++;

                combinacao[A]--;

            }

            else if(combinacao[B] >= 1){

                combinacao[BC]++;

                combinacao[B]--;

            }

            else{

                combinacao[C]++;

            }

        }

    }

    cout << beleza/2 << endl;

    return 0;

}