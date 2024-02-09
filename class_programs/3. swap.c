#include <stdio.h>

int main()
{
    int a = 5;
    int b = 6;
    printf("%d\n", a);
    printf("%d\n", b);
    int temp = 0;
    temp = a;
    a = b;
    b = temp;
    printf("--- After Swapping ---\n");
    printf("%d\n", a);
    printf("%d\n", b);

    return 0;
}
