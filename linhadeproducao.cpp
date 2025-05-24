#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    long long int M;

    cin>>M;
    
    if(log2(M*8000000)/int(log2(M*8000000)) != 1){
        cout<<int(log2(M*8000000))+1;
    }else{
        cout<<int(log2(M*8000000));
    }

   return 0;
}