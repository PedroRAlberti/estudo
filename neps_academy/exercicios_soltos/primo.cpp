#include <iostream>
#include <math.h>

using namespace std;

int main() {

    long long int A,b;

    bool primo = true;

    cin >> A;

    b = int(sqrt(A));

    for (int i = 2 ; i <= b + 1; i ++ )
    {
        if (i == A)
            continue;
        if (A%i == 0)
        {
            primo = false;
            break;
            cout << i;
        }
    }

    if (primo && A != 1)
        cout << "S";

    else 
        cout << "N";

    return 0;
}