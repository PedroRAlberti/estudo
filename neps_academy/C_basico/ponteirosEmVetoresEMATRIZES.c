#include <stdio.h>

int main (){

    int vetor[] = {1,2,3,4};

    int *p = &vetor;

    printf("%d\n",*p);

    p = &vetor[2];

    printf("%d\n",*p);

    int M[3][3] = {{1,2,3},{4,5,6},{7,8,9}};

    p = &M;

    printf("%d\n",*p);

    p = &M[2];

    printf("%d\n",*p);

    p = &M[1][1];

    printf("%d\n",*p);

    return 0;
}