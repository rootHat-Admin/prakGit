#include <stdalign.h>
#include <stdio.h>

int main() {
  int a, b;
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);

  if (a > b) {
    printf("The maximum is %d\n", a);
  } else {
    printf("The maximum is %d\n", b);
  }

  return 0;
}
