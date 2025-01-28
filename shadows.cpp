#include <bits/stdc++.h>

using namespace std;

# define pi 3.14159265358979323846  /* pi */
#define print cout <<
#define fim << endl

double dist(double catetoOposto, int angulo){

    double angulo_radiano = (angulo * pi) / 180.0;

    return (catetoOposto * (1 / tan(angulo_radiano)));

}

int main(){

    int O = 0, N = 0, maiorx = 0;
    int i = 0;
    double distance = 0;

    cin >> O >> N;

    vector<int> altura(N);
    vector<vector<double>> coord(N, vector<double>(2));

    for(i = 0; i < N; i++){

        cin >> coord[i][0] >> altura[i];

        distance = dist(altura[i], O);

        coord[i][1] = coord[i][0] + distance;

        // // Debug
        // cout << coord[i][1] << endl;

    }

    sort(coord.begin(), coord.end());

    distance = coord[0][1] - coord[0][0];

    maiorx = coord[0][1];

    // // Debug
    // cout << coord[0][0] << " " << coord[0][1] << " " << distance << endl;

    for(i = 1; i < N; i++){

        if(coord[i][0] >= maiorx){

            distance += coord[i][1] - coord[i][0];

            maiorx = coord[i][1];
        }

        else if(coord[i][0] < maiorx && coord[i][1] > maiorx){

            distance += coord[i][1] - maiorx;

            maiorx = coord[i][1];
        }

        // // Debug
        // cout << coord[i][0] << " " << coord[i][1] << " " << distance << endl;

    }

    cout << fixed;
    cout.precision(5);
    print distance fim;

    return 0;

}