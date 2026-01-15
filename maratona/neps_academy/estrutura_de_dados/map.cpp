// analogo ao dicionario do python
#include <iostream>

#include <map>

using namespace std;

int main() {

    map <char , int> mp;

    mp.insert({'a', 1});
    mp.insert(make_pair('b', 2));
    mp.insert(make_pair('c', 3));

    auto ptr = mp.begin();

    cout << "chave " << ptr->first << " elemento " << ptr->second << endl;
    
    ptr = mp.end();

    ptr--;

    cout << "chave " << ptr->first << " elemento " << ptr->second << endl;
    
    cout << mp.size() << endl;

    mp.erase('c');

    cout << mp.size() << endl;

    ptr = mp.find('b');

    cout << ptr->first<< endl;

    mp['d'] = 4;

    cout << mp['d'] << endl;

    mp['d'] = 5;

    mp.clear();

    cout << mp.size();

    return 0;
}