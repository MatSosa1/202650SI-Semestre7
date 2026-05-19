#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  char nombre[5] = "";
  char apellido[10] = "";

  printf("Ingrese su nombre: ");
  scanf("%s", &nombre);

  printf("Ingrese su apellido: ");
  scanf("%s", &apellido);

  printf("\nSu nombre es: %s\n", nombre);
  printf("\nSu apellido es: %s\n", apellido);
}
