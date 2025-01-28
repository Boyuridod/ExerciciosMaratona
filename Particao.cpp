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

    int N = 0, res = 1;

    cin >> N;

    for(int i = 1; i < N; i++){

        res = multi(res, 2);

    }

    res = res % mod;

    cout << res << endl;

    return 0;
}