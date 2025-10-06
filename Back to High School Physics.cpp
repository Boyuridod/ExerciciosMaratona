// https://vjudge.net/problem/UVA-10071

#include <bits/stdc++.h>

using namespace std;

int main(){

    // ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int v = 0, t = 0;

    while(scanf("%d %d", &v, &t) != EOF){
        cout << 2 * v * t << endl;
    }

    return 0;
}