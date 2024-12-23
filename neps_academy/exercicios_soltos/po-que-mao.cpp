#include <iostream>
#include <queue>

using namespace std;

int main() {

    priority_queue < int,vector < int>, greater<int>> pq;

    int N,X,Y,Z,aux = 0;

    cin >> N >> X >> Y >> Z;

    pq.push(X);
    pq.push(Z);
    pq.push(Y);

    for (int i = 0 ; i < 3 ; i ++)
    {
        aux += pq.top();
        pq.pop();

        cout << aux;

        if (aux > N)
        {
            cout << i;
            break;
        }
    }

    if (aux <= N)
        cout <<"3";

    return 0;
}