// https://codeforces.com/group/KqUNBZJnMk/contest/573754/problem/B

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0, i = 0, caixas = 0;

    cin >> N;

    vector<int> box(N, 0);

    for(i = 0; i < N; i++){

        cin >> box[i];

    }

    sort(box.begin(), box.end());

    for(i = 1; i < N; i++){

        if(box[i - 1] == box[i])
            caixas++;

    }

    caixas++;

    cout << caixas << endl;

    return 0;

}