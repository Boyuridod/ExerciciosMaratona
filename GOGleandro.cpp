#include <bits/stdc++.h>

using namespace std;
#define int long long
#define INF 999999999

int32_t main(){

    int N = 0, i = 0, j = 0, mint = 0;

    cin >> N;
    int x;
    int mi, resp=-INF;

    for(i = 0; i < N; i++){
        mi=INF;
        for(j = 0; j < N; j++){

            cin >> x;
            mi=min(x,mi);
        }
        resp=max(mi,resp);
    }
    cout<<resp<<"\n";

    return 0;

}