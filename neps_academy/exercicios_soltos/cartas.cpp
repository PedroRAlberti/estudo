#include <iostream>
#include <set>

using namespace std;

int main() {

    set <int> st;
    int x = 0;
    cin >> x;
    st.insert(x);

    for (int i = 0; i < 2 ; i++){
        cin >> x;
        auto ptr = st.find(x);
        if (ptr != st.end()){
            st.erase(x);
        }
        else {
            st.insert(x);
        }
    }

    auto ptr = st.begin();

    cout << *ptr;

    return 0;
}