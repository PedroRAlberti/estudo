#include <iostream>
using namespace std;

int main() {

    int M[31][2], N, x, aux = 0;

    char L;

    cin >> x;

    for (int i = 0 ; i < 31 ; i ++)
    {
        for (int j = 0 ; j < 2 ; j++)
        {
            M[i][j] = 0;
        }
    }

    for (int i = 0; i < x ; i++)
    {
        cin >>  N >> L;

        if(L == 'D')
            M[N-30][0]++;

        else if(L == 'E')
            M[N-30][1]++;
    }

    for (int i = 0 ; i < 31 ; i++)
    {
        aux += min(M[i][0],M[i][1]);
    }

    cout << aux;

    return 0;
}