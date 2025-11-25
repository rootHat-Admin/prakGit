#include <stdio.h>

int main() {
  char name[] = "Atar";
  int age = 20;
  float height = 1.70;
  const int months = 12;

  printf("User %s is %d years old, height %.2f m. There are %d months in a "
         "year.\n",
         name, age, height, months);

  return 0;
}
