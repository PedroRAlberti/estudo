#include <iostream>
#include <map>
#include <set>
using namespace std;

int main() {

    map <int , int > mp;

    set <int> st;

    int x , y ,auxq = 0,auxv = 0;

    cin >> x ;

    for (int i = 1 ; i < 13 ; i ++)
    {
        mp.insert({i,0});
    }

    for (int i = 0 ; i < x ; i ++) 
    {
        cin >> y;
        auto ptr = mp.find(y);
        ptr->second += 1;
    }

    for (int i = 1 ; i < 13 ; i ++)
    {
        if (mp[i] > auxv)
        {
            auxv = mp[i];
            auxq = 1;
            st.clear();
            st.insert(i);
        }

        else if  (mp[i] == auxv)
        {
            auxq += 1;
            st.insert(i);
        }

    }

    auto ptr = st.begin();

    for (int i = 0; i < auxq; i ++)
    {
        cout << *ptr << " ";
        ptr++;
    }

    return 0;
}