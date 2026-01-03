#include <stdio.h>
#include <stdlib.h>



int main() {
    int N;
    int x[100000], y[100000];

    scanf("%d", &N);

    for (int i = 0; i < N; i++)
        scanf("%d %d", &x[i], &y[i]);


    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            if (y[i] > y[j] || (y[i] == y[j] && x[i] > x[j])) {
                int temp;
                temp = y[i]; y[i] = y[j]; y[j] = temp;
                temp = x[i]; x[i] = x[j]; x[j] = temp;
            }
        }
    }

    for (int i = 0; i < N; i++)
        printf("%d %d\n", x[i], y[i]);

    return 0;
}
