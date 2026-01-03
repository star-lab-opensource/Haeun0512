#include <stdlib.h>

int main()
{
    int n, sum = 0;
    int min = 100;
    for (int i = 0; i < 7; i++) {
        scanf("%d", &n);
        if (n % 2 == 1) {
            sum += n;
            if (n < min) min = n;
        }
    }
    if (sum == 0) printf("-1");
    else printf("%d\n%d", sum, min);
    return 0;
}
