#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {

    set <int> st;

    vector <int> a;

    int x,y,z;

    cin >> x;

    for (int i = 0 ; i < x ; i ++)
    {
        cin >> z;
        a.push_back(z);
    }

    cin >> y;

    for (int i = 0 ; i < y ; i ++)
    {
        cin >> z;
        st.insert(z);
    }

    for (int i = 0 ; i < x ; i++)
    {
        if(st.find(a[i]) == st.end())
            cout << a[i] << " ";
    }

    return 0;
}