#include <iostream>

using namespace std;

int main() {

    int x;

    cin >> x;

    int T[x],Ta[x];

    for (int i = 0; i < x ; i++)
    {
        cin >> T[i];
    }

    for (int i = 1; i < x - 1; i++)
    {
        Ta[i] = T[i-1] + T[i] + T[i+1];
    }

    Ta[0] = T[0] + T[1];    

    Ta[x-1] = T[x-2] + T[x-1];

    for (int i = 0 ; i < x ; i++)
    {
        cout << Ta[i] << endl;
    }

    return 0;
}