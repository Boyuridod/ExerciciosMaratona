// https://codeforces.com/contest/2091/problem/0

#include <bits/stdc++.h>
#include <iostream>

using namespace std;

bool testaData(vector<int> vet){

    if(vet[0] >= 3){
        if(vet[1] >= 1){
            if(vet[2] >= 2){
                if(vet[3] >= 1){
                    if(vet[5] >= 1)
                        return true;

                    else
                        return false;
                }
                else
                    return false;
            }
            else
                return false;
        }
        else
            return false;
    }

    else{
        return false;
    }

}

void printame(vector<int> vet){

    int i = 0;

    for(i = 0; i < vet.size(); i++){

        cout << i << ": " << vet[i] << " ";

    }

    cout << endl;

}

int main(){

    int N = 0;

    cin >> N;

    while (N--){

        int n = 0, a = 0, i = 0, qtt = -1;

        cin >> n;

        vector<int> nums(10, 0);

        for(i = 0; i < n; i++){

            cin >> a;

            nums[a]++;

            if(testaData(nums) && qtt == -1){
                qtt = i + 1;
            }

        }

        // printame(nums);

        if(qtt != -1){
            cout << qtt << endl;
        }

        else{
            cout << 0 << endl;
        }

    }

    return 0;

}