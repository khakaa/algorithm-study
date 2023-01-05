#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int x;
    int y;
} greed;

// qsort의 compare함수는 반드시 int형 반환값과 const void 포인터 매개변수 두 개를 갖는다.
// 일반적인 오름차순 정렬 조건은
// a < b -> -1
// a > b -> 1
// a = b -> 0
// 내림차순은 반대로
int compare(const void *a, const void *b){
    greed A = *(greed *)a; // void 포인터를 구조체 greed 포인터로 변환한뒤 역참조하여 값을 가져옴.
    greed B = *(greed *)b;
    
    // 내림차순
    if (A.y > B.y) return -1;
    else if (A.y == B.y){
        if (A.x > B.x) return -1;
        else return 1;
    }
    else return 1;
}

int main(void){
    greed jewels[1000001];
    int w,n,total_price = 0;
    scanf("%d %d", &w, &n);

    for (int i=0; i<n; i++){
        scanf("%d %d", &jewels[i].x, &jewels[i].y);
    }

    qsort(jewels, n, sizeof(greed), compare);

    for (int i=0; i<n; i++){
        if (w > jewels[i].x){
            total_price += jewels[i].x * jewels[i].y;
            w -= jewels[i].x;
        } else {
            total_price += w*jewels[i].y;
            break;
        }
    }

    printf("%d", total_price);
}