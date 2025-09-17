#include <stdio.h>

int main() {
  char name[] = "Atar";
  int age = 18;
  float height = 1.70;
  double weight = 70.12;
  char colorLetter = 'B';
  const int months = 12;

  printf("Name: %s\n", name);
  printf("Age: %d\n", age);
  printf("Height: %.2f\n", height);
  printf("Weight: %.1f\n", weight);
  printf("ColorLetter: %c\n", colorLetter);
  printf("Mouths: %d\n", months);

  return 0;
}
