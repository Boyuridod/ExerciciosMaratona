#include <bits/stdc++.h>

using namespace std;

void printaVetor(vector<int> vetor){
    int i = 0;

    for(i = 0; i < vetor.size(); i++){
        cout << vetor[i] << " ";
    }

    cout << endl;
}

string exercicio(){
    int n = 0, i = 0, j = 0;

    cin >> n;

    vector<int> a(n, 0), b(n, 0);

    for(i = 0; i < n; i++){
        cin >> a[i];
    }

    for(i = 0; i < n; i++){
        cin >> b[i];
    }

    for(i = 0; i < n; i++){
        while(a[i] < b[i]){
            for(j = 0; j < n; j++){
                if(a[j] - 1 < b[i] and j != i){
                    return "NO";
                }
                else if(j != i){
                    a[j]--;
                }
            }
        }

        printaVetor(a);
    }

    return "YES";
}

int main(){

    int t = 0;

    cin >> t;

    while(t--){
        cout << exercicio() << endl;
    }

    return 0;
}