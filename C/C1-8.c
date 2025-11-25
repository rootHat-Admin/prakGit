#include <stdio.h>

int main() {
  int year = 2025;
  float ball = 78.5;
  double temp = 43.123;

  char text[] = "Hello";
  char text2[] = "You Normal?";
  char t = 'g';

  printf("To day year: %d\n", year);
  printf("Your Ball: %.2f\n", ball);
  printf("To day temperature: %.2f\n", temp);
  printf(text, "\n - Hello", text2);
  printf("\n - %c\n", t);

  return 0;
}
