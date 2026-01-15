#include <iostream> 
#include <queue>

using namespace std;

int main(){

	// Declarando uma Fila de Prioridade
	priority_queue <int, vector <int>, greater <int>> pq;
    // ela necessita de 3 parametros, o primeiro é tipo de dado a ser armazenado, o segundo é o container onde os dados serão os elementos e o terceiro é a funcao d comparacao
	
    for (int i = 0; i < 6 ; i++){
        pq.push(i);
    }

    pq.push(10);
    pq.push(50);
    pq.push(30);

    cout << pq.top() << endl;

    pq.pop();

    cout << pq.top() << endl;

    cout << pq.size() << endl;

    return 0;
}

