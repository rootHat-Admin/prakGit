#include <stdio.h>

int main() {
  int age1, age2;
  printf("Enter age1: ");
  scanf("%d", &age1);
  printf("Enter age2: ");
  scanf("%d", &age2);

  if (age1 == age2) {
    printf("Both ages are equal!");
  } else if (age1 > age2) {
    printf("The first age is greater than the second");
  } else if (age1 < age2) {
    printf("The second age is greater than the first");
  } else {
    printf("It's not clear");
  }
}
