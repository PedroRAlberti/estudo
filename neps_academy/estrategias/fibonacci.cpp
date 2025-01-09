#include <iostream>
using namespace std;

int backtracking(int x){
    if (x == 1 || x == 0)
        return 1;

    return backtracking(x-1) + backtracking(x-2);
}

int main() {

    int x;

    cin >> x;

    cout << backtracking(x);

    return 0;
}