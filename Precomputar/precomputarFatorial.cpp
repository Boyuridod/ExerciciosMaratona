#include <bits/stdc++.h> // Pré-computar fatorial
#include <fstream>

typedef long long longo;

#define mod (longo)(1e9 + 7)

using namespace std;

longo mult(longo x, longo y){

    return (x * y) % mod;

}

int main(){

    longo N = 1e6, i = 0, fat = 1;
    double porcen = 0;
    ofstream fatoriais;
    string coloca = "";

    fatoriais.open("fatoriais.txt");

    fatoriais.clear();

    if(fatoriais.good()){

        cout << "Arquivo criado!" << endl << endl;

    }

    else{

        return -1;

    }

    fatoriais << "vector<longo> fat(" << N << ");" << endl << endl;

    fatoriais << "fat = [";

    for(i = 1; i <= N; i++){

        fat = mult(fat, i);

        if(i < N)
            fatoriais << fat << ", ";

        else
            fatoriais << fat;

        // cout << i << endl;

        // porcen = (longo)((i / N) * 10000);

        // cout << porcen << "% concluído" << endl;

    }

    fatoriais << "];";

    cout << 100 << "% concluído" << endl;

    fatoriais.close();

}