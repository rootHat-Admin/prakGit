#include <stdio.h>

int main() {
  const float PI = 3.14159;
  int radius = 5;
  double area = PI * radius * radius;

  printf("Radius: %d\n", radius);
  printf("Area: %.2f\n", area);

  return 0;
}
