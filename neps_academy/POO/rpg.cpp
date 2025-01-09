#include <iostream>

using namespace std;

struct Personagem {
    char nome[50];
    int ataque;
    int defesa;
    int vida;
        
    bool sobreviveu(int danorecebido) {
        return (vida + defesa - danorecebido) > 0;
    }

    };

int main(){
    Personagem personagem;

    int dano;

    cin >> personagem.nome;
    cin >> personagem.ataque;
    cin >> personagem.defesa;
    cin >> personagem.vida;
    cin >> dano;

    if(personagem.sobreviveu(dano)){
        cout << personagem.nome << " sobreviveu!!!";
    }else{
        cout << personagem.nome << " morreu :(";
    }
}

