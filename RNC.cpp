// https://codeforces.com/group/KqUNBZJnMk/contest/584176/problem/K

#include <bits/stdc++.h>

using namespace std;

int main(){

    int N = 0, teste = 0, even = 0, odd = 0;

    cin >> N;

    for(N = N; N > 0; N--){

        cin >> teste;

        if(teste % 2 == 0)
            even++;
        else
            odd++;

    }

    teste = even - odd;

    if(teste == 0 || teste == 1 || teste == -1)
        cout << "Good" << endl;
    else
        cout << "Not Good" << endl;

    return 0;

}