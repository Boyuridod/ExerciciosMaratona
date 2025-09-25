// https://codeforces.com/problemset/problem/339/A

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int i = 0;
    string a;

    cin >> a;

    vector<int> b;

    for(i = 0; i < a.size(); i+=2){
        b.push_back(a[i] - 48);
    }

    sort(b.begin(), b.end());

    for(i = 0; i < b.size() - 1; i++){
        cout << b[i] << "+";
    }

    cout << b[i] << endl;

    return 0;
}