// https://vjudge.net/problem/UVA-11764

#include <bits/stdc++.h>

using namespace std;

void exercicio(int k){
    int n = 0, i = 0, high = 0, low = 0;

    cin >> n;

    vector<int> wall(n, 0);

    for(i = 0; i < n; i++){
        cin >> wall[i];
    }

    for(i = 1; i < n; i++){
        if(wall[i] < wall[i - 1]){
            low += 1;
        }
        else if(wall[i] > wall[i - 1]){
            high += 1;
        }
    }

    cout << "Case " << k << ": " << high << " " << low << endl; 
}

int main(){
    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0, k = 0;

    cin >> t;

    for(k = 1; k <= t; k++){
        exercicio(k);
    }
}