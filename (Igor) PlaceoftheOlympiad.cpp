#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin>>t;

    while(t--){
        long long int m,n,k,c, tot;
        
        cin>>m>>n>>k;
        
        c = k/m;
        
        if(k%m != 0){
            c+=1;
        }
        
        k = c;
        
        c = n+1-k;
        
        tot = (n-(c-1))/c;
        
        if((n-(c-1)) % c != 0){
            tot+=1;
        }
        
        cout<<tot<<"\n";
        
    }

    return 0;
}