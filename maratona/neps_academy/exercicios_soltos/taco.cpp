#include <iostream>
#include <set>

using namespace std;

int main() { 

    int r = 0,x,y;

    set < int> st;

    cin >> x;

    for (int i = 0 ; i < x ; i ++)
    {
        cin >> y;

        if (st.find(y) == st.end())
        {
            st.insert(y);
            r += 2;
        }

        else
            st.erase(y);

    }

    cout << r;

    return 0;
}