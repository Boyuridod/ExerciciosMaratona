// https://codeforces.com/contest/2091/problem/B

#include <bits/stdc++.h>

using namespace std;

int main(){

    int t = 0;

    cin >> t;

    while (t--){

        int n = 0, x = 0, i = 0, qtt = 0, aux = 0, team = 1;

        cin >> n >> x;

        vector<int> student;

        for(i = 0; i < n; i++){

            cin >> aux;

            student.push_back(aux);

            if(student[i] > x){

                qtt++;

                student.pop_back();

            }

        }

        team++;

        while(student.size() > team){

            for(i = 0; i < student.size(); i++){

                

            }

            team++;

        }

        cout << qtt << endl;

    }

    return 0;

}

/*
// Codigo do Igor
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin>>t;
    
    while(t--){
        int n,x;
        cin>>n>>x;
        int a;
        vector<int> v;
        int tot = 0;
        int l = 0;
        
        for(int i = 0; i < n; i++){
            cin>>a;
            v.push_back(a);
        }
        sort(v.rbegin(),v.rend());
        
        a = v[0];
        for(int i = 0; i < n; i++){
            a=min(a,v[i]);
            l+=1;
            if(a*l >= x){
                l = 0;
                a = v[0];
                tot+=1;
            }
        }
        cout<<tot<<"\n";
        
    }

    return 0;
}
*/