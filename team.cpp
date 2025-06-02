// https://codeforces.com/problemset/problem/231/A

#include <bits/stdc++.h>

using namespace std;

int exercicio(){

    int soma = 0, aux = 0, i = 0;

    for(i = 0; i < 3; i++){

        cin >> aux;

        soma += aux;

    }

    if(soma >= 2){

        return 1;

    }

    else{

        return 0;

    }

}

int main(){

    int problems = 0, resp = 0;

    cin >> problems;

    while(problems--){

        resp += exercicio();

    }

    cout << resp << endl;

}