#include <iostream>
using namespace std;

struct Inimigo {    
    int id;
    int x; 
    int y;
    bool vivo;

    //É necessário ter um construtor sem parâmetros para criar o vetor na função principal
    Inimigo(){
        id = -1;
        x = -1; 
        y = -1;
        vivo = false;
    }

    //TODO: Crie um construtor que inicializa um inimigo usando os parâmetros abaixo.
    Inimigo(int ID, int X, int Y, bool VIVO){    
            id = ID;
            x = X;
            y = Y;
            vivo = VIVO;
    }

    //TODO: Método que muda a o status do inimigo de vivo para morto caso seja acertado pelo lazer na posição (X,Y).
    void foi_acertado(int X, int Y){       
        if (X == x & Y == y)
            vivo = false; 
    }

};

int main(){

    int N; //Quantidade de Inimigos
    cin >> N;

    Inimigo inimigo[N];

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

    bool espaco = false;

    for (int i = 0 ; i < N ; i++)
    {
        if (!inimigo[i].vivo){

            if(espaco) 
                cout << " ";

            espaco = true;

            cout << i;
            }
        } 
    }

