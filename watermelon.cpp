#include <iostream>

using namespace std;

// https://codeforces.com/problemset/problem/4/A

int main(){

    bool possivel = 0;
    int pete = 0, billy = 0;

    cin>>pete;

    while(pete > billy && possivel == 0){

        pete--;

        billy++;

        if (pete % 2 == 0 && billy % 2 == 0){
            possivel = 1;
        }

    }

    if(possivel){
        cout<<"YES";
    }

    else{
        cout<<"NO";
    }

    return 0;

}