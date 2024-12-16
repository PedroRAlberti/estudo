#include <iostream>
using namespace std;

int main() {

    long long int A,B,aux = 1,aux1 = 1,aux2 = 1;
 
    cin >> A;

    for (int i = 0 ; i < A ; i ++)
    {
        cin >> B;

        if (i == A - 1)
            aux *= B;

        if (i < 2)
            aux1 *= B;

        if (i > A - 3)
            aux2 *= B;
    }

    if (A == 3)
        aux *= aux1;

    else
        aux *= max(aux1,aux2);

    cout << aux;

    return 0;
}