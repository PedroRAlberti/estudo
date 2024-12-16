#include <iostream>

using namespace std;

int main(){

    int A,B,C;

    cin >> A >> B >> C;

    if (A == B && A == C)
        cout << "3";

    else if (A != B && A!= C && B!= C )
        cout << "1";

    else if (A == B) {
        if (A + B < C)
            cout << "1";
        else 
            cout << "2";
    }

    else if (A == C) {
        if (A + C < B)
            cout << "1";
        else 
            cout << "2";
    }

    else if (C == B) {
        if (C + B < A)
            cout << "1";
        else 
            cout << "2";
    }

    return 0;
}