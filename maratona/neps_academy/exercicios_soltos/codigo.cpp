#include <iostream>
using namespace std;

int main(){

    int x,aux = 0;

    cin >> x;

    int C[x];

    for (int i = 0; i < x ; i ++)
    {
        cin >> C[i];
    }

    for (int i = 0; i < x - 2 ; i++)
    {
        if ((C[i] == 1) && (C[i+1] == 0) && (C[i+2] == 0 ))
            aux += 1;
    }

    cout << aux;

    return 0;
}