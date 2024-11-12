#include <stdio.h>

int main(){
    int A = 1,B = 0,C = 0,ENTRADA,CONTADOR = 0;
    scanf ("%d",&ENTRADA);
    while (CONTADOR < ENTRADA){
        printf("%d ",B);
        C = B;
        B = A;
        A = B + C;
        CONTADOR = CONTADOR + 1;
    }
    return 0;

}