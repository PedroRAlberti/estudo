#include <stdio.h>

int main() {
    int n;
    do {
        scanf("%d", &n); // Corrigido: Passando o endereço da variável
    } while (n != 10);
    printf("O valor final é %d\n", n);
    return 0;
}
