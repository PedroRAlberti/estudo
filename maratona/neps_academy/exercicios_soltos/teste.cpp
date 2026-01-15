#include <iostream>
#include <map>
#include <set>

using namespace std;

int main() {
    map<int, set<int>> mp; // Mapeia cada índice a um conjunto de inteiros
    set<int> r;            // Armazena os índices cujos conjuntos ficaram vazios

    int N, K, U, x;
    cin >> N >> K >> U;

    // Leitura dos conjuntos iniciais
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < K; j++) {
            cin >> x;
            mp[i].insert(x);
        }
    }

    // Processamento das atualizações
    for (int i = 0; i < U; i++) {
        for (int j = 0; j < N; j++) {
            cin >> x;

            // Verifica se o valor está no conjunto e o remove
            auto it = mp[j].find(x);
            if (it != mp[j].end()) {
                mp[j].erase(it);
            }

            // Se o conjunto ficar vazio, adiciona o índice a `r`
            if (mp[j].empty() && r.find(j) == r.end()) {
                r.insert(j);
            }
        }
    }

    // Imprime os índices cujos conjuntos ficaram vazios
    for (auto idx : r) {
        cout << idx << " ";
    }
    cout << endl;

    return 0;
}
