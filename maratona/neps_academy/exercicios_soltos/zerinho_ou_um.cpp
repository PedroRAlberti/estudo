#include <iostream>

using namespace std;

int main (){

    int A,B,C;

    cin >> A >> B >> C;

    if (A == B && A == C){
        cout << "*";
    }

    if ( A == B && A != C){
        cout << "C";
    }

    if ( A == C && A != B){
        cout << "B";
    }

    if ( C == B && A != C){
        cout << "A";
    }

    return 0;
}