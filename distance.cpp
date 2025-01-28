// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/H

#include <bits/stdc++.h>

using namespace std;

double dist(int x1, int y1, int x2, int y2){

    return (x2 - x1) + (y2 - y1);

}

int main(){

    int t = 0;
    double calc = 0;
    vector<int> a = {0, 0};
    vector<int> b(2, 0);

    cin >> t;

    while(t--){

        cin >> b[0] >> b[1];

        calc = dist(a[0], a[1], b[0], b[1]) / 2;

        if(b[0] % 2 == 0 && b[1] % 2 == 0){

            cout << b[0] / 2 << " " << b[1] / 2 << endl;

        }

        else if((b[0] + b[1]) % 2 == 0){

            if(b[0] > b[1])
                b[0] -= calc;
            else
                b[1] -= calc;

            cout << b[0] << " " << b[1] << endl;

        }

        else{

            cout << -1<< " " << -1 << endl;

        }

    }

    return 0;
}