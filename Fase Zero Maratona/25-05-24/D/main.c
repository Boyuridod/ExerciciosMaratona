/*#include <stdio.h>
#include <stdlib.h>

int main(){

    int E = 0, V = 0, hora = 0, minuto = 0;
    double horas = 0, minutos = 0;

    scanf("%d %d",&E, &V);

    horas = (E / V) + 19;

    hora = hora;

    minutos = (horas - hora) * 60;

    printf("%.2d:%.2lf", hora, minutos);

    return 0;
}
*/

#include <stdio.h>
#include <math.h>

int main() {
    int E, V;
    scanf("%d %d", &E, &V);

    double horas = (E / (double)V) + 19;
    horas = fmod(horas, 24);

    double minutos = (horas - (int)horas) * 60;
    if (minutos < 1 && minutos > 0.5) {
        minutos = 1;
    } else {
        minutos = (int)minutos;
    }

    int horas_int = (int)horas;

    if (horas_int < 10) {
        printf("0");
    }
    printf("%d:", horas_int);

    if ((int)minutos < 10) {
        printf("0");
    }
    printf("%d", (int)minutos);

    return 0;
}
