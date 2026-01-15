// lembrando que a fila opera sobre a ideia de FIFO 
// basicamente o primeiro a sair é o primeiro que entrou, tal como uma fila de caixa

#include <iostream> 
// Biblioteca com a implementação da fila
#include <queue>

using namespace std;

int main(){
	// Declarando uma fila de inteiros
	queue <int> q;
	// Inserindo elementos na fila
	q.push(1);
	q.push(2);
    q.push(3);
    q.push(4);
    q.push(5);

    cout << q.front() << endl;
    // o front retorna o primeiro elemento inserido
    
    q.pop();
    // o pop retira o elemento da frente da lista

    cout << q.size() << endl;

    queue <int> temp = q; // Copiando a fila
    while (!temp.empty()) {
        cout << temp.front() << " "; // Mostra o elemento da frente
        temp.pop();                  // Remove o elemento da cópia
    }
    cout << endl;

    return 0;
}