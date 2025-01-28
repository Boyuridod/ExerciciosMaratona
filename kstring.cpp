// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/C

#include <bits/stdc++.h>

using namespace std;

int main(){

    int k = 0, i = 0, j = 0, l = 0;
    string teste = "";
    vector<int> alfa(26, 0);
    bool certo = true;

    cin >> k;

    cin >> teste;

    for(i = 0; i < teste.size(); i++)
        alfa[teste[i] - 'a']++;

    for(i = 0; i < alfa.size(); i++){
        
        if(alfa[i] % k != 0)
            certo = false;

    }

    if(!certo)
        cout << -1 << endl;

    else{

        for(l = k; l > 0; l--){

            for(i = 0; i < alfa.size(); i++){

                for(j = 0; j < alfa[i]/k; j++)
                    cout << char(i + 'a');
            
            }

        }

        cout << endl;

    }

    return 0;

}