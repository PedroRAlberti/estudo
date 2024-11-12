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

    int DET;

    DET = MATRIZ[0][0] * MATRIZ[1][1] - MATRIZ[0][1] * MATRIZ[1][0];
    
    printf ("%d", DET);

    return 0;
}