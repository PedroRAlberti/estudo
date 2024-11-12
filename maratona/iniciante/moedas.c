#include <stdio.h>
//este codigo usará como valores para notas 100,20,2.
int main(){
    int P = 0,V = 0,D = 0;
    int VALOR;
    printf("digite o seu valor");
    scanf("%d",&VALOR);
    while (VALOR >= 100){
        P = P + 1;
        VALOR = VALOR - 100;
    }
    while (VALOR >= 20){
        V = V + 1;
        VALOR = VALOR - 20;
    }
    while (VALOR >= 2){
        D = D + 1;
        VALOR = VALOR - 2;
    }
    printf("100 - %d, 20 - %d, 2 - %d",P,V,D);


    return 0;
}