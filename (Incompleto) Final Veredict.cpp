// https://codeforces.com/contest/2078/problem/0

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0;

    cin >> N;

    while (N--){

        int n = 0, x = 0, i = 0;
        bool certo = false;

        cin >> n >> x;

        vector<int> a(n, 0);

        for(i = 0; i < n; i++){

            cin >> a[i];

        }

        int k = -1;

        for(i = 2; i < a.size(); i++){

            if(a.size() % i == 0){
                k = i;
                break;
            }

        }

        if(k == -1)
            k = 1;

        vector<vector<int>> mat(, vector<int>(colunas, 0));

        if(certo)
            cout << "Yes" << endl;
        else
            cout << "No" << endl;

    }

    return 0;

}