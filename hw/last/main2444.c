#include <stdlib.h>

int main() {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    int b1 = b % 10;
    int b2 = (b / 10) % 10;
    int b3 = b / 100;
    printf("%d\n%d\n%d\n%d", a * b1, a * b2, a * b3, a * b);
    return 0;
}
