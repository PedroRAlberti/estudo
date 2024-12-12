#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5};

    // Iterador no início do vetor
    auto ptr = v.begin();
    cout << (*ptr) << endl;

    // Iterador no final (ajustado para o último elemento válido)
    ptr = v.end() - 1;
    cout << (*ptr) << endl;

    cout << v.size() << endl;

    // Utilizando resize: reduzir o tamanho
    v.resize(2, 4);
    for (auto i : v)
        cout << i << " ";
    cout << endl;

    // Utilizando resize: aumentar o tamanho
    v.resize(5, 3);
    for (auto i : v)
        cout << i << " ";
    cout << endl;

    // Limpar o vetor
    vector<int> t = {1, 2, 3};
    t.clear();
    cout << t.size() << endl;

    // Inserindo um elemento no final do vetor
    v.push_back(6);
    for (auto i : v)
        cout << i << " ";
    cout << endl;

    // Inserindo elementos em posições específicas
    v.insert(v.begin(), 6); // Inserir na posição 0
    v.insert(v.begin() + 3, 10); // Inserir na posição 3

    // Removendo o elemento na segunda posição
    v.erase(v.begin() + 1);

    // Removendo o último elemento
    v.pop_back();

    // Exibindo o vetor final
    for (auto i : v)
        cout << i << " ";
    cout << endl;

    // Acessando diretamente o elemento na 3ª posição
    cout << v[2] << endl;

    return 0;
}
