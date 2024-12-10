// a ideia geral é que se nao usar ponteiros, voce simplesmente cria uma nova variavel na funcao mas na main continua inalterado
// ao usar os ponteiros desta forma, na verdade está sendo alterado o valor associado aos endereços de memória de A e B
#include <stdio.h>

int troca(int *a, int *b){
    int aux = *a;

    *a = *b;

    *b = aux;

    printf("troca -> a = %d e b = %d\n", *a, *b);
}

int main(){
    int a = 1;

    int b = 2;

    printf("main -> a = %d e b = %d\n", a, b);

    troca(&a, &b);

    printf("main -> a = %d e b = %d\n", a, b);
}

