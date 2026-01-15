#include <iostream>

using namespace std;

int main(){

    int A,B,C,MT;

    cin >> A >> B >> C;

    MT = ( B + 2*C);

    if (MT > A + C)
        MT = A + C;

    if (MT > 2*A + B)
        MT = 2*A + B;

    cout << 2*MT;

    return 0;
}