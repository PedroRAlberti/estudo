#include <stdio.h>

// detalhes importantes 
// ao fazer *p = &x voce está direcionando o ponteiro p ao endereço de memória x
// e ao adicionar 1 no endereço de memória, será adicionado a quantidade de bytes do tipo usado, ex: x é um int e int tem 4 bytes, então pula de 4 em 4
// se o endereco de memoria estiver vazio, será dito somente o proprio endereco
int main(){
    printf("Tamanho de um inteiro: %d\n\n", sizeof(int));

    int x = 1;

    int *p = &x;

    int *j = p + 1;

    int k = x + *p;

    printf("k = %d\n",k);
    printf("p aponta para %d\n", *p);
    printf("p+1 aponta para %d\n", *j);
    printf("p+2 aponta para %d\n", p+2);

    // x = 2;

    // printf("p aponta para %d\n", *p);

    *p = 2;

    printf("x passou a ser %d",x);
}
