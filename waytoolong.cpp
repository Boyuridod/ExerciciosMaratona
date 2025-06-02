// https://codeforces.com/problemset/problem/71/A

#include <bits/stdc++.h>
using namespace std;

void exercicio(){
    
    int i = 0, tam = 0;
    string palavra;
    
    cin >> palavra;
    
    tam = palavra.size();
    
    if(tam > 10){
        
        cout << palavra[0] << tam - 2 << palavra[tam - 1] << endl;
        
    }
    
    else{
        
        cout << palavra << endl;
        
    }
    
}

int main(){
    
    int N = 0;
    
    cin >> N;
    
    while(N--){
        
        exercicio();
        
    }

    return 0;
}