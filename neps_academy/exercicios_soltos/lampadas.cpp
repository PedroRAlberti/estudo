#include <iostream>

using namespace std;

int main() {

    int A,B,C,D;

    cin >> A >> B >> C >> D;

    if ( A == C && B == D ){
        cout << "0";
    }

    else if ((A != C && B == D) || (A != C && B != D) ){
        cout << "1";
    }

    else {
        cout << "2";
    }

    return 0;
}