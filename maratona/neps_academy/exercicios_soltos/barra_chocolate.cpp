#include <iostream>

using namespace std;

int main() {

    int N, Xi, Yi, Xf, Yf;

    cin >> Xi >> Yi >> Xf >> Yf;

    if (((Xi <= N/2 && Xf <= N/2) || (Xi > N/2 && Xf < N/2)) && ((Yi <= N/2 && Yf <= N/2) || (Yi > N/2 && Yf < N/2)))
        cout << "N";

    else 
        cout << "S";

    return 0;
}