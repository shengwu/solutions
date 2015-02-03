#include <stdio.h>
#include <math.h>

int main(int argc, char* argv[]) {
    int n, squares, i;
    scanf("%d", &n);
    while (n != 0) {
        squares = 0;
        for (i = 1; i <= n; i++) {
            squares += (int) pow(i, 2);
        }
        printf("%d\n", squares);
        scanf("%d", &n);
    }
    return 0;
}
