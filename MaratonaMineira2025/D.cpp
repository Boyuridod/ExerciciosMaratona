#include <bits/stdc++.h>

using namespace std;

int main(){

    int num = 0, i, j, k = 0, cont = 0;

    cin >> num;

    for(i = 1; i <= 6; i++){
        for(j = 1; j <= 6; j++){
            for(k = 1; k <= 6; k++){
                if((i + j + k) == num){
                    cont += 1;
                }
            }
        }
    }

    cout << fixed << setprecision(12) << (cont / (6.0 * 6.0 * 6.0)) << endl;

    return 0;

}