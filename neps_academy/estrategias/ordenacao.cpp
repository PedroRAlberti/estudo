#include <iostream>
using namespace std;

int main() {

    int x;

    cin >> x;

    int v[x];

    for (int i = 0 ; i < x ; i ++)
    {
        cin >> v[i];
    }

    for (int i = 0 ; i < x ; i ++)
    {
        for (int j = 0 ; j < x ; j ++)
        {
            if (v[j] > v[j+1])
                swap(v[j],v[j+1]);
        }
    }

    for (int i = 0 ; i < x ; i ++)
    {
        cout << v[i] << " ";
    }

    return 0;
}