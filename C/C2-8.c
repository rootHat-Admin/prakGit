#include <stdio.h>

int main() {
  // Using for loop
  printf("Number from 1 to 5 using for loop:\n");
  for (int i = 1; i <= 5; i++) {
    printf("%d ", i);
  }
  printf("\n");

  // Using while loop
  printf("Numbers from 1 to 5 using while loop:\n");
  int j = 1;
  while (j <= 5) {
    printf("%d", j);
    j++;
  }
  printf("\n");

  return 0;
}
