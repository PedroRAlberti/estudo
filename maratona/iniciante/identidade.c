#include <stdio.h>

struct identidade 
{
    char nome[100];
    int cpf;
    int rg;
};

typedef struct identidade id;

int main(){
    
    id patetas[3];

    int i;
    
    for ( i = 0 ; i < 3 ; i++ ){
        scanf("%s", &patetas[i].nome);
        scanf("%d", &patetas[i].cpf);
        scanf("%d", &patetas[i].rg);
    }

    for ( i = 0; i < 3 ; i ++){
        printf("o pateta %s de cpf %d e rg %d\n",patetas[i].nome,patetas[i].cpf,patetas[i].rg);
    }

    return 0;
}