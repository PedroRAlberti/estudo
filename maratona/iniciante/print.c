// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int A = 100;
    scanf("%d",&A);
    int B = 200;
    float SOMA = 0;
    SOMA = A + B;
    if (SOMA > 100){
        printf("vsf : %1.2f\n",SOMA);
    }
    printf("a soma e %f",SOMA);
    int K = 11;
    while (K < 5 || K > 10){
        scanf("%d",&K);
        printf("o valor recebido nao vale: %d\n", K);
    }
    printf("finalmente : %d", K);

    return 0;
}