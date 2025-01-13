#include <iostream>
using namespace std;

class Inimigo {
    int id;
    int x;
    int y;
    bool vivo;

public:
    // Construtor vazio
    Inimigo() : id(-1), x(0), y(0), vivo(false) {}

    // Construtor parametrizado
    Inimigo(int id, int x, int y, bool vivo) {
        this->id = id;
        this->x = x;
        this->y = y;
        this->vivo = vivo;
    }

    // Método que verifica se o inimigo foi acertado
    bool foi_acertado(int x, int y) {
        if (this->x == x && this->y == y && this->vivo) {
            this->vivo = false;
            return true;  // Acertado pela primeira vez
        }
        return false;  // Não acertado ou já morto
    }

    // Getter para o status do inimigo
    bool isVivo() const { return vivo; }

    // Getter para o ID do inimigo
    int getId() const { return id; }
};

class Fase {
    Inimigo* inimigos;
    int quantidade_inimigos;
    int pontos;
    int municao;

public:
    // Construtor da classe Fase
    Fase(int quantidade_inimigos, int municao)
        : quantidade_inimigos(quantidade_inimigos), pontos(0), municao(municao) {
        inimigos = new Inimigo[quantidade_inimigos];
    }

    // Destrutor para liberar memória
    ~Fase() {
        delete[] inimigos;
    }

    // Método para inicializar os inimigos
    void inicializar_inimigos() {
        for (int i = 0; i < quantidade_inimigos; i++) {
            int x, y;
            cin >> x >> y;
            inimigos[i] = Inimigo(i, x, y, true);
        }
    }

    // Método para jogar a fase
    void jogar(int T) {
        for (int i = 0; i < min(municao, T); i++) {
            int x, y;
            cin >> x >> y;

            bool acertou = false;

            for (int j = 0; j < quantidade_inimigos; j++) {
                if (inimigos[j].foi_acertado(x, y)) {
                    pontos += 10;
                    acertou = true;
                    break;  // Interrompe, pois o disparo já acertou um inimigo
                }
            }

            if (!acertou) {
                // Disparo falhou, mas ainda consome munição
            }

            municao--;  // Decrementa munição após cada tentativa
        }
    }

    // Método para imprimir o relatório da fase
    void imprimir_relatorio() {
        cout << "Relatorio da Fase\n";
        cout << "Pontuacao: " << pontos << endl;
        cout << "Municao restante: " << municao << endl;
        cout << "Inimigos mortos:" << endl;

        for (int i = 0; i < quantidade_inimigos; i++) {
            if (!inimigos[i].isVivo()) {
                cout << "Inimigo " << inimigos[i].getId() << " foi derrotado." << endl;
            }
        }
    }
};

int main() {
    int N; // Quantidade de inimigos
    int M; // Quantidade de munição

    cin >> N >> M;

    Fase fase = Fase(N, M);

    fase.inicializar_inimigos();

    int T; // Quantidade de tentativas de disparo
    cin >> T;

    fase.jogar(T);
    fase.imprimir_relatorio();

    return 0;
}
