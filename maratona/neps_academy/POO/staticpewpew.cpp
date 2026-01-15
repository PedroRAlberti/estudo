#include <iostream>
using namespace std;

struct Inimigo {    
    int id;
    int x; 
    int y;
    bool vivo;
    static int quantidade_vivos;

    //É necessário ter um construtor sem parâmetros para criar o vetor na função principal
    Inimigo(){
        id = -1;
        x = -1; 
        y = -1;
        vivo = false;
    }

    //TODO: Crie um construtor que inicializa um inimigo usando os parâmetros abaixo.
    Inimigo(int ID, int X, int Y, int VIVO){   
        id = ID;
        x = X;
        y = Y;
        vivo = VIVO;     
    }

    //TODO: Método que muda a o status do inimigo de vivo para morto caso seja acertado pelo lazer na posição (X,Y). Também deve atualizar a variável quantidade_vivos.
    void foi_acertado(int X, int Y){       
        if (x == X & y == Y & vivo == true)
        {
        vivo = false;
        quantidade_vivos --;
        }
    }

};

int Inimigo::quantidade_vivos = 0;

int main(){

    int N; //Quantidade de Inimigos
    cin >> N;

    Inimigo inimigo[N];
    Inimigo::quantidade_vivos = N;

    for(int id=0;id<N;id++){
        int x, y;
        cin >> x >> y;

        inimigo[id] = Inimigo(id, x, y, true);
    }

    int M; //Quantidade de Inimigos
    cin >> M;

    for(int i=0;i<M;i++){
        int x, y;
        cin >> x >> y;

        for(int id=0;id<N;id++){
            inimigo[id].foi_acertado(x,y);
        }
    }

    cout << "vivos: " << Inimigo::quantidade_vivos << endl;

    cout << "mortos: " << N - Inimigo::quantidade_vivos << endl;

    //TODO: Imprima a saída conforme indicada no enunciado do exercício.
}
