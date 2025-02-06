// https://codeforces.com/problemset/problem/510/A

#include <bits/stdc++.h>

typedef long long longo;

#define mod longo(1e9+7)

using namespace std;

int main(){

    int n = 0, m = 0, i = 0;
    bool isNoInicio = false;

    cin >> n >> m;

    while(n--){

        for(i = 0; i < m; i++){

            if(n % 2 == 0){

                cout << "#";

            }

            else{

                if(isNoInicio){

                    if(i == 0)
                        cout << "#";
                    
                    else
                        cout << ".";

                    if(i == m - 1)
                        isNoInicio = false;

                }

                else{

                    if(i == m - 1)
                        cout << "#";
                    
                    else
                        cout << ".";

                    if(i == m - 1)
                        isNoInicio = true;

                }

            }

        }

        cout << endl;

    }

    return 0;

}