#include <bits/stdc++.h>

using namespace std;

typedef long long longo;

int main(){

    longo N, B = 0;
    longo ponteirox = 0, ponteiroy = 0;
    longo solucaox = 0, solucaoy = 0;

    cin >> N >> B;

    while(B > 0){

        if((B - N - ponteirox) > 0){

            B -= N - ponteirox;
            
            ponteirox++;
            ponteiroy++;
            
            if((B - N - ponteiroy) > 0){
                
                B -= N - ponteiroy;
        
                ponteiroy++;
        
                if((B - N - ponteirox) > 0){
                    
                    B -= N - ponteirox;
            
                    ponteirox++;
                    ponteiroy++;

                    if((B - N - ponteiroy) > 0){

                        B -= N - ponteiroy;
                
                        ponteirox++;

                    }

                    else{

                        ponteiroy += B;

                        B = 0;

                    }
        
                }

                else{

                    ponteirox += B;

                    B = 0;

                }
    
            }

            else{

                ponteiroy += B;

                B = 0;

            }

        }

        else{

            ponteirox += B;

            B = 0;

        }

    }

    cout << N - ponteirox << " " << N - ponteiroy;

    return 0;
}