#include <stdio.h>

int main(){

    int x,i;

    scanf("%d",&x);

    unsigned long long int Fib[x + 1];

    Fib[0] = 0;
    Fib[1] = 1;

    for ( i=2 ; i < x + 1; i++)
    {
        Fib[i] = Fib[i-1] + Fib[i-2];
    }

    printf("Fib(%d) = %llu",x,Fib[x]);

    return 0;
}