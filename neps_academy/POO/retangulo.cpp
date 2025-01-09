#include <iostream>
using namespace std;

class Retangulo
{
pair <int,int> a, b ;

public:

    void set_pontos(int x1, int y1, int x2, int y2){
        a = {x1,y1};
        b = {x2,y2};
    }

    void area(){
        cout << abs((a.first - b.first)*(a.second - b.second)) << endl;
    }
};

//TODO: Implemente a classe Retangulo

int main(){

    Retangulo retangulo;
    int N;

    cin >> N;

    for(int i=0;i<N;i++){
        int x1, y1, x2, y2;
        char operacao;

        cin >> operacao;

        if(operacao == 'R'){ //Redimensionar
            cin >> x1 >> y1 >> x2 >> y2;
            retangulo.set_pontos(x1, y1, x2, y2);
        }else if(operacao == 'A'){ //Imprimir a área
            retangulo.area();
        }
    }
}
