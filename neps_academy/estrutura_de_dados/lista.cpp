// a lista é utilizada como lista encadeada, onde cada elemento aponta para o proximo e o ultimo para void
// além disso há alguns métodos que serão usados durante a aplicação

#include <iostream> 
//Biblioteca com a implementação da lista
#include <list>

// Para evitar o uso do std::
using namespace std;

int main(){
	list <int> l = {1, 2, 3};
	// O auto é o tipo automático do C++, ou seja, ele é resolvido em tempo de compilação
	// Note que a linha abaixo é equivalente a list<int>::iterator it = l.begin()
	auto ptr = l.begin();
	// Observe que 1 é o primeiro elemento da lista
	cout << *ptr << endl;
	
    ptr = l.end();
	// ptr tem a referência para o final da lista
	// Vamos acessar o último elemento da lista, para isso, basta retroceder o point 1 possição
	ptr--;
	// Note que 3 é o último elemento da lista
	cout << *ptr << endl;
    
    cout << l.size() << endl;

    l.clear();

    list <int> k = {1,2,3,4,5,6};

    ptr = k.begin();

    // Vamos mover o ponteiro até a segunda posição
	int pos = 1;
	while(pos != 2){
		pos++;
		ptr++;
	}
	// Inserindo o elemento na posição desejada 
	l.insert(ptr, 10);
	// Note que o 10 agora está na segunda posição
	for(auto i : k)
		cout << i << " ";
	cout << endl;

    ptr--;

	l.erase(ptr);
	for(auto i : k)
		cout << i << " ";
	cout << endl;

    return 0;
}