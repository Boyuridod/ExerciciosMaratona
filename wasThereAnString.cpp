// https://codeforces.com/contest/2069/problem/A

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0;

    cin >> N;

    while (N--){

        int qtt = 0, i = 0;
        bool pode = true;

        cin >> qtt;

        vector<int> a(qtt - 2, 0);

        for(i = 0; i < qtt - 2; i++){

            cin >> a[i];

        }

        for(i = 0; i < qtt - 4; i++){

            if(a[i] == 1 && a[i + 1] == 0 && a[i + 2] == 1){

                pode = false;

                break;

            }

        }

        if(pode)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;

    }

    return 0;

}