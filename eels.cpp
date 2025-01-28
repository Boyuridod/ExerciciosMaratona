// https://codeforces.com/group/KqUNBZJnMk/contest/573754/problem/H

#include <bits/stdc++.h>

using namespace std;

typedef long long longo;

int main(){

    longo Q = 0, i = 0, j = 0, k = 0, l = 0, enguia = 0, perigo = 0, tam = 0, aux = 0;
    char op = ' ';
    vector<longo> eels;

    cin >> Q;

    for(k = 0; k < Q; k++){

        cin >> op >> enguia;

        if(op == '+'){
            eels.push_back(enguia);
        }

        else{

            for(i = eels.size() - 1; i >= 0; i--){

                if(eels[i] == enguia){
                    eels.erase(i + eels.begin());

                    i = -1;
                }

            }

        }

        vector<longo> copia = eels;

        perigo = 0;

        i = j = l = 0;

        tam = copia.size();

        sort(copia.begin(), copia.end());

        while(j < tam){
        
            if(copia[i] >= copia[j] && i != j){

                l = 0;

                if(copia[i] <= (copia[j] * 2))
                    perigo++;

                copia[i] += copia[j];

                copia.erase(j + copia.begin());

                tam -= 1;

                j = 0;

            }

            else if(copia[j] >= copia[i] && i != j){

                if(copia[j] <= (copia[i] * 2))
                    perigo++;

                copia[j] += copia[i];

                copia.erase(i + copia.begin());

                tam -= 1;

                j = 0;

            }

            j++;

        }

        cout << perigo << endl;

    }

    return 0;

}