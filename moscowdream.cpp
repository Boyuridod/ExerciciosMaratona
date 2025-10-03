// https://open.kattis.com/contests/eqnk5p/problems/moscowdream

#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int i = 0, soma = 0;
    char dummy;
    vector<int> a;

    while(scanf("%d%c", &i, &dummy)){
        a.push_back(i);
        if(dummy == '\n') break;
    }

    for(i = 0; i < a.size() - 1; i++){
        if(a[i] < 1){
            cout << "NO" << endl;
            return 0;
        }

        soma += a[i];
    }

    if(soma >= a[3] && a[3] >= 3){
        cout << "YES" << endl;
    }

    else{
        cout << "NO" << endl;
    }

    return 0;
}