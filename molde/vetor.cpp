#include <bits/stdc++.h>

using namespace std;

int main(){

    int i = 0;

    // Declaração do vetor
    vector<int> v;

    // Inserção no vetor
    v.push_back(5);
    v.push_back(2);
    v.push_back(51);
    v.push_back(4);

    v.push_back(99);

    // Remoção no vetor (Ultimo valor)

    v.pop_back();

    for(i = 0; i < v.size(); i++){

        cout << v[i] << " ";

    }

    cout << endl;

    // Tamanho do vetor

    cout << "Tamanho: " << v.size() << endl;

    // Ordenação

    sort(v.begin(), v.end());

    for(i = 0; i < v.size(); i++){

        cout << v[i] << " ";

    }

    cout << endl;

    // Ordenação inversa

    sort(v.rbegin(), v.rend());

    for(i = 0; i < v.size(); i++){

        cout << v[i] << " ";

    }

    cout << endl;

    // Inserir no meio

    int posicao = 1, valor = 7;

    v.insert(posicao + v.begin(), valor);

    for(i = 0; i < v.size(); i++){

        cout << v[i] << " ";

    }

    cout << endl;

    // Remover no meio

    v.erase(posicao + v.begin());

    for(i = 0; i < v.size(); i++){

        cout << v[i] << " ";

    }

    cout << endl;

    return 0;

}