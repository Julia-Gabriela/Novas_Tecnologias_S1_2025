#include <stdio.h>

int main(){
    int num, quad = 0;

    printf("Digite um numero: ");
    scanf("%d", &num);

    for(int i = 1, j = 1; j<= num; j++, i+=2){
        quad = quad+i;
    }

    printf("%d^2 = %d", num, quad);
}