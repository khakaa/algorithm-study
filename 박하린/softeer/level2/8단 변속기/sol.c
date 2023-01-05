#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// char *delete_space(char s[]){
//     char *str = (char*)malloc(sizeof(s));
//     int i,k =0;

//     for (i=0; i<strlen(s); i++){
//         if(s[i] != ' ') str[k++] = s[i];
//     }
//     str[k] = '\0';
//     return str;
// }

// int main(void){
    // char trans[16];
    // char asc[9] = "12345678";
    // char des[9] = "87654321";
    // scanf("%[^\n]s", trans);
    // if (strcmp(delete_space(trans),asc) == 0)
    //     printf("ascending");
    // else if (strcmp(delete_space(trans),des) == 0)
    //     printf("descending");
    // else
    //     printf("mixed");
// }

int main(void){
    char t[9];
    char asc[9] = "12345678";
    char des[9] = "87654321";
    for(int i=0; i<8; i++){
        scanf("%s", &t[i]);
    }
    if (strcmp(t,asc) == 0) printf("ascending");
    else if (strcmp(t,des) == 0) printf("descending");
    else printf("mixed");
}