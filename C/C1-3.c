#include <stdio.h>

int main() {
  int age = 40;
  float height = 1.753;
  double weight = 68.45678;
  char grade = 'A';
  char name[] = "Alex";

  const int days_in_year = 365;
  const float PI = 3.14159;

  printf("Name: %s\n", name);
  printf("Age: %d\n", age);
  printf("Grade: %c\n", grade);

  printf("Height: %.2f\n", height);
  printf("Weight: %.3f\n", weight);
  printf("PI: %.5f\n", PI);

  printf("There are %d days in a year\n", days_in_year);

  printf("\nNumber Square Cube\n");
  for (int i = 1; i <= 5; i++) {
    printf("%-7d %-7d %-7d\n", i, i * i, i * i * i);
  }

  return 0;
}
