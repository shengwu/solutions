/*
 * In this problem, we need to check numbers between
 * 1 and 1000000000 and see if they are prime. We can do this by
 * generating primes between 1 and sqrt(1000000000) and
 * seeing if any of those primes evenly divide a candidate. 
 * If so, then the candidate is not prime.
 *
 * We check primality for each candidate in the given ranges
 * and print the number if it is prime.
 */

#include <stdio.h>
#include <math.h>

long primes[3405] = {2, 3};

void check_and_add_prime(long n, int *idx) {
    int i;
    int curr_prime = 1;
    for (i = 0; i < *idx; i++) {
        if (n % primes[i] == 0) {
            curr_prime = 0;
            break;
        }
    }
    if (curr_prime == 1) {
        primes[*idx] = n;
        *idx += 1;
    }
}

void check_and_print_prime(long n) {
    if (n == 5) {
        printf("%d\n", 5);
        return;
    }
    int i = 0;
    long sqrt_n = (long) ceil(sqrt((double) n));
    while (primes[i] <= sqrt_n) {

        if (primes[i] < 1) {
            printf("err idx: %d\n", i);
        }

        if (n % primes[i] == 0) {
            return;
        }
        i += 1;
    }
    printf("%d\n", n);
}

int main(int argc, char* argv[]) {
    int i, k, m;
    long n;
    int idx;
    int n_cases;
    long start;
    long end;
    static int SQRT_MAX = 31650; /* just above sqrt(1000000000) */

    /* 
     * Populate the array of primes.
     * Primes greater than 3 have the form 6k +/- 1.
     */
    k = 1;
    idx = 2;
    while (6*k+1 < SQRT_MAX) {
        check_and_add_prime(6*k-1, &idx);
        check_and_add_prime(6*k+1, &idx);
        k += 1;
    }

    /* Process test cases */
    scanf("%d", &n_cases);
    for (i = 0; i < n_cases; i++) {
        scanf("%d %d", &start, &end);

        /* 
         * Check primes in range that have form 6k +/- 1
         * (add m = 2 or 4 to n alternately)
         */
        k = start / 6;
        if (6*k+1 < start || k == 0) {
            k += 1;
        }
        if (start <= 6*k-1) {
            n = 6*k-1;
            m = 2;
        } else {
            n = 6*k+1;
            m = 4;
        }
        /* handle 2, 3 */
        if (start <= 2) {
            printf("2\n");
        }
        if (start <= 3) {
            printf("3\n");
        }
        while (n <= end) {
            check_and_print_prime(n);
            n += m;
            if (m == 2) {
                m = 4;
            } else {
                m = 2;
            }
        }
        printf("\n");
    }

    return 0;
}
