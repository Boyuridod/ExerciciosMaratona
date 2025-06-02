// https://codeforces.com/contest/2116/problem/A

#include <bits/stdc++.h>

using namespace std;

typedef long long longo;

void exercicio(){

    longo k = 1, i = 0, menor = 0, posMenor = 0;
    longo a = 0, b = 0, c = 0, d = 0;

    vector<longo> v(4,0);

    for(i = 0; i < 4; i++){
        cin >> v[i];
        if(i == 0 or v[i] <= menor){
            menor = v[i];
            posMenor = i;
        }
    }

    if(posMenor == 0){
        if(v[0] != v[1] and v[0] != v[3]){
            cout << "Flower" << endl;
        }
        else{
            cout << "Gellyfish" << endl;
        }
    }

    else if(posMenor == 2){
        if(v[2] != v[1] and v[2] != v[3]){
            cout << "Flower" << endl;
        }
        else{
            cout << "Gellyfish" << endl;
        }
    }

    else{
        cout << "Gellyfish" << endl;
    }
    

}

int main() {

    int N = 0;

    cin >> N;

    while(N--){

        exercicio();

    }
    
    return 0;
}