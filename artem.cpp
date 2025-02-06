// https://codeforces.com/group/KqUNBZJnMk/contest/573754/problem/A

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0, m = 0, n = 0, qttB = 0, i = 0, j = 0;

    cin >> N;

    while(N--){

        cin >> n >> m;

        qttB = ceil((n*m) / 2);

        for(i = 0; i < n; i++){

            for(j = 0; j < m; j++){

                if(i + j != 0)
                    cout << "B";

                else
                    cout << "W";

            }

            cout << endl;

        }

    }

    return 0;

}