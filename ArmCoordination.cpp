#include <bits/stdc++.h>

using namespace std;

int main(){

    int x = 0, y = 0, r = 0;

    cin >> x >> y;

    cin >> r;

    cout << x - r << " " << y + r << endl;

    cout << x + r << " " << y + r << endl;

    cout << x + r << " " << y - r << endl;

    cout << x - r << " " << y - r << endl;

    return 0;

}