// https://vjudge.net/contest/687524/problemPdf/H?descKey=2469277870581605

#include <bits/stdc++.h>

using namespace std;

int main(){

    int t = 0, a = 0, b = 0, c = 0, d = 0;
    int x = 0, y = 0;

    cin >> t;

    for(t; t > 0; t--){

        cin >> a >> b;
        cin >> c >> d;

        if(c - a != d - b && (b - a) != 0 && (d - c) != 0){

            cout << -1 << endl;

        }

        else{

            y = c - a;

            while(d % y != 0){

                b++;
                d++;

            }

            while((c - 1) % y != 0){

                a--;
                c--;

            }

            x = d / y;

            cout << a << " " << b << " " << c << " " << d << " " << x << " " << y << endl;

            if(a % y != 1 || c % y != 1){

                cout << -1 << endl;

            }

            else{

                cout << x << " " << y << endl;

            }

        }

    }

    return 0;

}