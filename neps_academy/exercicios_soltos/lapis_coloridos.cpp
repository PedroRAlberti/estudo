#include <iostream>
using namespace std;

int main() {

    int x = 0,dist,dist1,dist2;

    cin >> x;

    int T[x];

    for (int i = 0; i < x ; i ++) 
    {
        cin >> T[i];
    }

    for (int i = 0 ; i < x ; i ++)
    {
        dist1 = 0;
        dist2 = 0;

        if (T[i] == 0)
            continue;

        for (int j = i ; j > 0 ; j --)
        {
            dist1 ++;
            if (T[j-1] == 0)
                break;
            if (j == 1)
                dist1 = 9999;
        }

        for (int j = i ; j < x - 1 ; j ++)
        {
            dist2 ++;
            if (T[j+1] == 0)
                break;
            if (j == x-2)
                dist2 = 9999;
        }

        if (i == 0)
        {
            T[i] = dist2;
            continue;
        }

        if (i == x - 1)
        {
            T[i] = dist1;
            continue;
        }

       dist = min(dist1,dist2);
       T[i] = min(dist,9);

    }

    for (int i = 0 ; i < x ; i++)
    {
        cout << T[i] << " ";
    }

    return 0;
}