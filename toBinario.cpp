#include <bits/stdc++.h>

using namespace std;

string toBinario(int converter){

    string convertido = "";

    if(converter > 1)
        convertido += toBinario(floor(converter/2));

    convertido += to_string(converter % 2);

    return convertido;

}

string to16bits(string converter){

    int i = 16 - converter.size();

    while(i--){

        converter = "0" + converter;

    }

    return converter;

}

int main(){

    cout << to16bits(toBinario(10000)) << endl;

    return 0;

}