// https://codeforces.com/group/KqUNBZJnMk/contest/584381/problem/C

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll somaDigitos(string x){

    ll d = x.size(), soma = 0;

    while (d--){
        soma += x[d] - '0';
    }

    return soma;    

}

int main(){

    int len = 400;
    cout << string(len, '5') << "\n";
    cout << (string(len - 1, '4') + '5') << "\n";

}