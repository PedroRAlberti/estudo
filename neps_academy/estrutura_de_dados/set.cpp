#include <iostream>
#include <set>

using namespace std;

int main() {
	// Declarando um set de inteiros
	set <int> st;

    //Inserindo elementos no set
    st.insert(1);
    st.insert(10);
    st.insert(4);
    st.insert(6);
    st.insert(1);

    // Removendo elementos do set
    st.erase(1);
    st.erase(101010);

    auto ptr = st.begin();
	// O primeiro é o menor, logo será 1
	cout << *ptr << endl;

    ptr = st.end();
    // Movendo o ponteiro para acessar o maior elemento no set
    ptr--;
	cout << *ptr << endl;

    ptr = st.find(4);

    cout << *ptr << endl;

    cout << st.size() << endl;

    st.clear();

    cout << st.size() << endl;

    return 0;
}