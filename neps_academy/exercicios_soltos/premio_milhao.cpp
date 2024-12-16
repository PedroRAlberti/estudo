#include <iostream>

using namespace std;

int main() {

    int dia = 0,N , Vi , Vt = 0;

    cin >> N;

    for (int i = 0; i < N ; i ++ ){
        cin >> Vi;
        Vt += Vi;
        dia ++;
        if (Vt < 1000000)
            continue;
        else
            break;
    }

    cout << dia;

    return 0;
}