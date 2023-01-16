#include <stdio.h>

int main(void){
    long long k,p,n = 0;
    scanf("%d %d %d", &k,&p,&n);
    
    for (int i=0; i<n; i++){
        k = (k*p) % 1000000007;
    }
    printf("%d", k);
}