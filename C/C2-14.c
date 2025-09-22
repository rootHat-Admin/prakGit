#include <stdio.h>

int main() {
  int n;
  unsigned long long fact = 1; // factorial can grow big
  printf("Enter a number n: ");
  scanf("%d", &n);

  for (int i = 1; i <= n; i++) {
    fact *= i;
  }
  printf("%d! = %llu\n", n, fact);

  return 0;
}
