#include <bits/stdc++.h>
#define int long long
#define mod (long)(1e9+7)

using namespace std;

int multi(int x, int y){

    return (x * y) % mod;

}

int32_t main(){

    ios_base :: sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int x = 0, y = 0;
    char op;

    cin >> x >> op >> y;

    // cout << x << op << y << endl;

    switch(op){

        case '+':
            cout << (x + y) % mod << endl;
        break;

        case '-':
            cout << ((x - y) + mod) % mod << endl;
        break;

        case '*':
            cout << multi(x, y) << endl;
        break;

        case '^':
            int res = 1;

            if(y > (10e5)){

                int j = 0;
                j = (int)(y / 10e4);
                int step = 0;

                for(int i = 0; i < 10e4; i++){

                    step *= multi(step, x);

                }

                for(int i = 0; i < j; i++){

                    res *= multi(res, step);

                }

                j = (y) % (int)(j * 10e4);

                for(int i = 0; i < j; i++){

                    res *= multi(res, x);

                }

                cout << res << endl;

            }

            else{

                for(int i = 0; i < y; i++){

                    res = multi(res, x);

                }

                cout << res << endl;

            }

        break;

    }

    return 0;
}