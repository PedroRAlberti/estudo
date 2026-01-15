// problema: dada uma sequencia de ( [ { ) ] }deve ser visto se está numa ordem coerente, a primeira entrada é a quantidade de linhas e as posteriores as linhas de fato


#include <iostream>
#include <stack>

using namespace std;

int main() {

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        string line;
        cin >> line;

        stack<char> e;
        bool aux = true;

        for (char c : line) {
            if (c == '(' || c == '[' || c == '{') {
                e.push(c);
            } else {
                if (!e.empty() && 
                    ((c == ')' && e.top() == '(') || 
                     (c == ']' && e.top() == '[') || 
                     (c == '}' && e.top() == '{'))) {
                    e.pop();
                } else {
                    aux = false;
                    break; // Para encerrar o processamento da string inválida
                }
            }
        }
        if (!e.empty()) {
            aux = false;
        }
        cout << (aux ? "balanceada" : "nao balanceada") << '\n';
    }

    return 0;
}
