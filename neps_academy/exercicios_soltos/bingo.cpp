#include <iostream>
#include <map>
#include <set>

using namespace std;

int main() {

    map <int , set<int>> mp;

    set <int> r;

    bool aux = false;

    int N, K, U,x;

    cin >> N >> K >> U;

    for (int i = 0; i < N ; i ++)
    {
        for (int j = 0; j < K ; j++)
        {
            cin >> x;
            mp[i].insert(x);
        }
    }

    for (int i = 0 ;  i < U ; i++)
    {

        if (aux)
            cin >> x;

        else
        {
            for (int j = 0 ; j < N ; j++)
            {
                cin >> x;
                auto ptr = mp[j].find(x);

                if (ptr != mp[j].end())
                    mp[j].erase(x);

                if (mp[j].empty())
                {
                    r.insert(j);
                    aux = true;
                }
            }
        }
    }

    for (auto idx : r) 
    {
        cout << idx << " ";
    }

    return 0;
}