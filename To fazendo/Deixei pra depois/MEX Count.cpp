// https://codeforces.com/contest/2123/problem/E

#include <bits/stdc++.h>

using namespace std;

typedef long long int longo;

const int mod = 1e9+7; // Primo
const int INF = 1e9; // Infinito ou (INT_MAX)
const double EPS = 1e-9; // Epsilon (Numero muito pequeno) (ou 1e-12)

int mex(vector<int> vet, int qtt){

    int min = INF, i = 0, j = 0;

    for(i = 0; i < qtt; i++){
        vet.pop_back();
    }

    for(i = 0; i < vet.size() - 1; i++){
        for(j = vet[i] + 1; j < vet[i + 1] - 1; j++){
            if(min > j){
                min = j;
                break;
            }
        }
        if(min != INF){
            break;
        }
    }

    if(min == INF){
        try{
            min = vet[vet.size() - 1] + 1;
        }
        catch(const std::exception& e){
            min = 1;
        }
    }

    return min;

}

void exercicio(){

    int n = 0, i = 0;

    cin >> n;

    vector<int> a(n, 0);

    for(i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    for(i = 0; i < n; i++){
        cout << mex(a, i) << " ";
    }

    cout << 1 << endl;
}

int main(){

    ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

    int t = 0;

    cin >> t;

    while (t--){

        exercicio();

    }

    return 0;
}