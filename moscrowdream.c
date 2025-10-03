// https://open.kattis.com/submissions/18325233

#include <stdio.h>
int main() {
    int a, b, c, n;
    scanf("%d %d %d %d", &a, &b, &c, &n);
    if ((a >= 1) && (b >= 1) && (c >= 1) && (a+b+c >= n && n >= 3))
        printf("YES\n");
    else
        printf("NO\n");
    return 0;
}