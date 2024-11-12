#include <stdio.h>

int main(){

    int A,B;
    scanf("%d",&A);
    scanf("%d",&B);
    int TEMP;
    
    if (A > B){
        A = A;
        B = B;
    }
    
    else {
        TEMP = A;
        A = B;
        B = TEMP;
    }

    while (A > B){
        if (B%5 == 2 || B%5 == 3){
            printf("%d\n",B);
        }
        B = B + 1;
    }

    return 0;
}