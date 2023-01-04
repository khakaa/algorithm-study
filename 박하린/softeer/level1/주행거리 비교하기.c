#include <stdio.h>

int main(void){
    int a, b = 0;
    scanf("%d %d", &a, &b);

    if (a > b) 
        printf("%c", 'A');
    else if (a < b) 
        printf("%c", 'B');
    else 
        printf("%s", "same");
    return 0;
}