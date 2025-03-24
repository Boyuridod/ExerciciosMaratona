// https://codeforces.com/contest/2090/problem/A

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0;

    cin >> N;

    while (N--){

        int x = 0, y = 0, i = 0;
        double a = 0;

        cin >> x >> y >> a;

        a = int(a) % (x + y);

        a += 0.5;

        for(i = 0; a > 0; i++){

            if(i % 2 == 0)
                a -= x;
            else
                a -= y;

            // cout << a << " ";

        }

        if(i % 2 == 0)
            cout << "YES" << endl;

        else
            cout << "NO" << endl;

    }

    return 0;

}