#include <stdio.h>

int main(){

    int i,j;
    int MATRIZ[2][2];

    for ( i=0 ;  i < 2 ; i++)
    {
        for ( j = 0 ; j < 2 ; j++ )
        {
            scanf ("%d", &MATRIZ[i][j]);
        }
    }

    for ( i=0 ;  i < 2 ; i++)
    {
        for ( j = 0 ; j < 2 ; j++ )
        {
            printf ("%d ", MATRIZ[i][j]);
        }
        printf("\n");
    }

    return 0;
}