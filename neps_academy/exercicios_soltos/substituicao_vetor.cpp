#include <iostream>

using namespace std;

int main() {

    int v[10] , min = 100 , x , Oco , ind[10];

    for (int i = 0 ; i < 10 ; i++){
        cin >> x;

        if (x < min){
            min = x;
            Oco = 1;
            ind[0] = i;
        }
        
        else if (x == min){
            ind[Oco] = i;
            Oco++;
        }
        
        v[i] = x;

    }

    for ( int i = 0; i < Oco ; i++)
        v[ind[i]] = -1;

    cout << "Menor: " << min<< endl;

    cout << "Ocorrencias: ";

    for (int i = 0; i < Oco ; i ++)
        cout << ind[i] << " ";

    cout << endl;

    for (int i = 0; i < 10 ; i++)
        cout << v[i] << " ";

    return 0;
}