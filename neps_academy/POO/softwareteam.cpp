#include <stdio.h>


class Projeto {
public:
    int requisito_programacao;
    int requisito_design;
};

class Empregado {
protected:
    int valor_por_projeto;
    int valor_recebido;
public:

    //Um empregado normal não é capaz de entregar nenhum projeto :(
    bool capaz(Projeto P){
        return false;
    }

    void receber_recompensa(){
        this->valor_recebido += valor_por_projeto;
    }

    int get_valor_recebido(){
        return this->valor_recebido;
    }

};

class Programador : public Empregado {
    int habilidade_programacao;
public:

    //TODO: Complete o código do construtor inicializando os valores corretamente.
    Programador(int valor_por_projeto, int habilidade_programacao){
        this->habilidade_programacao = habilidade_programacao;
        this->valor_por_projeto = valor_por_projeto;
        this->valor_recebido = 0;
    }

    //TODO: Um programador deve ser capaz de entregar um projeto se sua habilidade de programação é maior que o requisito de programação do projeto.
    bool capaz(Projeto P){
        return this->habilidade_programacao >= P.requisito_programacao;
    }
};

class Designer : public Empregado {
    int habilidade_design;
public:

    //TODO: Complete o código do construtor inicializando os valores corretamente.
    Designer(int valor_por_projeto, int habilidade_design){
        this->habilidade_design = habilidade_design;
        this->valor_por_projeto = valor_por_projeto;
        this->valor_recebido = 0;
    }

    //TODO: Um designer deve ser capaz de entregar um projeto se sua habilidade de design é maior que o requisito de design do projeto.
    bool capaz(Projeto P){
        return this->habilidade_design >= P.requisito_design;
    }
};

int main(){

    int valor, habilidade;

    scanf("%d %d", &valor, &habilidade);

    Programador programador = Programador(valor, habilidade);

    scanf("%d %d", &valor, &habilidade);

    Designer designer = Designer(valor, habilidade);

    int N;
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        Projeto projeto;
        scanf("%d %d", &projeto.requisito_programacao, &projeto.requisito_design);

        //TODO:Use os métodos das classes acima para calcular quando tanto o programador quanto o designer conseguem desenvolver o projeto P e dê a recompensa a cada um caso eles consigam.
        if (programador.capaz(projeto) && designer.capaz(projeto)){
            programador.receber_recompensa();
            designer.receber_recompensa();
        }
    
    }

    printf("Programador: R$ %d\n", programador.get_valor_recebido());
    printf("Designer: R$ %d\n", designer.get_valor_recebido());
}