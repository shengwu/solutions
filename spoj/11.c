#include <stdio.h>
#include <math.h>

int main(int argc, char* argv[]) {
    int i, k, n_cases;
    long n, num_zeros;

    scanf("%d", &n_cases);
    for (i = 0; i < n_cases; i++) {
        scanf("%d", &n);
        k = 5;
        num_zeros = 0;
        if (k > n) {
            printf("0\n");
        } else {
            while (k <= n) {
                num_zeros += (long)floor((double)n/k);
                k *= 5;
            }
            printf("%d\n", num_zeros);
        }
    }
    return 0;
}
