#include <stdio.h>

int main() {
  int i = 0;

  // Execute loop at least once
  do {
    printf("i = %d\n", i);
    i++;
  } while (i < 100);

  return 0;
}
