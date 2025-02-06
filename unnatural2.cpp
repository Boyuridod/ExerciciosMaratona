// https://codeforces.com/group/KqUNBZJnMk/contest/584381/problem/C

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll somaDigitos(ll y){

    string x = to_string(y);
    ll d = x.size(), soma = 0;

    while (d--){
        soma += x[d] - '0';
    }

    return soma;    

}

int main(){

    ll n = 0, m = 0;
    ll a = 0, b = 0;
    ll sa = 0, sb = 0, ab = 0, sab = 0;
    ll incr = 1;

    cin >> n >> m;

    a = 0;
    b = m;

    sa = somaDigitos(a); sb = somaDigitos(b);

    ab = a + b;

    sab = somaDigitos(ab);

    while(sa < n){

        a++;

        sa = somaDigitos(a);

        ab = a + b;

        sab = somaDigitos(ab);

        cout << a << endl;

    }

    while(sb < n || sab > m){

        if(sb < n){

            b += incr;

            sb = somaDigitos(b);

            ab = a + b;

            sab = somaDigitos(ab);

        }

        else if(sab > m){

            b += incr;

            sb = somaDigitos(b);

            ab = a + b;

            sab = somaDigitos(ab);

        }

        cout << "b" << b << endl;

    }

    cout << a << endl << b << endl;

}