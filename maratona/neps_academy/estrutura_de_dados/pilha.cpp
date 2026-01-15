#include <iostream>
#include <stack>

using namespace std;

int main(){

    // Declarando uma pilha de inteiros
	stack <int> q;	
	// Inserindo elementos na pilha
    int i = 0;
	while ( i < 6){
        q.push(i);
        i++;
    }

	// Retorna o topo da pilha, no caso, será 5
	cout << q.top() << endl;

    //Removendo o elemento do topo da pilha
	// O novo elemento do topo será o 1
	q.pop();

	// Retorna o topo da pilha, no caso, será 4
	cout << q.top() << endl;

	// Tamanho da pilha 
	cout << q.size() << endl;

    return 0; 
}