#include <iostream>
using namespace std;

int main(){

    int N,x, soma = 0,somaaux1,somaaux2;

    cin >> N ;

    int M[N][N];

    for (int i = 0; i < N ; i++)
    {
        for (int j = 0; j < N ; j++)
        {
            cin >> x;
            M[i][j] = x;
        }
    }

    for (int i = 0; i < N ; i++)
        soma += M[0][i];

    for (int i = 0; i < N ; i++)
    {
        somaaux1 = 0;
        somaaux2 = 0;
        for (int j = 0; j < N ; j++)
        {
            somaaux1 += M[i][j];
            somaaux2 += M[j][i];
        }

        if (somaaux1 != soma || somaaux2 != soma )
        {
            cout << "-1";
            return 0;
        }

    }

    somaaux1 = 0;
    somaaux2 = 0;

    for (int i = 0; i < N ; i++){
        somaaux1 += M[i][i];
        somaaux2 += M[N - 1 - i][i];
    }

    if (somaaux1 != soma || somaaux2 != soma )
    {
        cout << "-1";
        return 0;
    }

    cout << soma;

    return 0;
}