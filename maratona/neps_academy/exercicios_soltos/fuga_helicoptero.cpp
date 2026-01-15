#include <iostream>
using namespace std;

int main() {

    int H,P,F,D,x,Dcerta;

    Dcerta = -1;

    cin >> H >> P >> F >> D;

    x = F;

    while (x != H)
    {
        x--;

        if (x == -1)
            x = 15;

        if (x == P)
        {
            Dcerta = 1;
            break;
        }
    }

    if (Dcerta == D)
        cout << "S";

    else 
        cout << "N";

    return 0;
}