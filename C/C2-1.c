#include <stdio.h>

int main() {
  int number = -5;

  // Check if the number is positive, negative, or zero
  if (number > 0) {
    printf("Positive\n"); // Number is greater than 0
  } else if (number < 0) {
    printf("Negative\n"); // Number is less than 0
  } else {
    printf("Zero\n"); // Number equals 0
  }

  return 0;
}
