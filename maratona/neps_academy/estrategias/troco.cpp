#include <iostream>
using namespace std;

int main(){

    int S[] = {1,5,10,25,50,100};

    int V,aux = 0;

    cin >> V;

    for (int i = 5 ; i >= 0 ; i--)
    {
        while (V >= S[i])
        {
            V -= S[i];
            aux ++;
        }
    }

    cout << aux;
    
    return 0; 
}