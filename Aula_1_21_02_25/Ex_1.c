#include <stdio.h>

int main (){
    long num, div= 10000, count = 0;

    printf("Digite um numero: ");
    scanf("%d", &num);

aux = num;

while(aux != 0)
{
    count++
    aux = num/(long)pow(10,count)
}

for(int i = 4; i <= 0; i--){
    printf("%d", num/ (long)pow(10,i));
    num = num% (long) pow(10,i);

}
}