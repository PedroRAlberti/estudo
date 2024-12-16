#include <iostream>

using namespace std;

int main() {
    int v[10], min = 100, x, Oco = 0, ind[10];

    // Leitura do vetor e cálculo do menor elemento
    for (int i = 0; i < 10; i++) {
        cin >> x;

        if (x < min) {
            // Novo menor encontrado
            min = x;
            Oco = 1;  // Reseta o contador de ocorrências para 1
            ind[0] = i;  // Salva o índice do menor
        } else if (x == min) {
            // Outra ocorrência do menor
            ind[Oco] = i;  // Salva o índice
            Oco++;
        }

        v[i] = x;  // Armazena o valor no vetor principal
    }

    // Substituir os menores valores por -1
    for (int i = 0; i < Oco; i++)
        v[ind[i]] = -1;

    // Exibir resultados
    cout << "Menor: " << min << endl;

    cout << "Ocorrencias: ";
    for (int i = 0; i < Oco; i++)
        cout << ind[i] << " ";
    cout << endl;

    cout << "Vetor atualizado: ";
    for (int i = 0; i < 10; i++)
        cout << v[i] << " ";
    cout << endl;

    return 0;
}
