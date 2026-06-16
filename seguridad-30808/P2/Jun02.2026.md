# 2 - Junio - 2026

## Objetivos de Aprendizaje

1. Criptografía Simétrica
  - Des
  - SDES
  - AES
    - 128 bits
    - 192 bits
    - 256 bits
2. Práctica de Laboratorio: Criptografía Simétrica
  - OpenSSL

## Meditación

### Jeff Bezos

En 1994, al identificar el rápido crecimiento de Internet, Bezos decidió abandonar su empleo y fundar Amazon desde el garaje de su casa en Seattle. Inicialmente, la empresa operaba como una librería en línea, pero rápidamente amplió su catálogo hasta convertirse en una plataforma global de comercio electrónico. Bajo su liderazgo, Amazon diversificó sus servicios hacia áreas como computación en la nube, inteligencia artificial, entretenimiento digital y dispositivos electrónicos.

Además de Amazon, Bezos fundó Blue Origin en el año 2000 con el objetivo de desarrollar tecnologías para la exploración espacial. También adquirió el periódico The Washington Post en 2013. Su visión empresarial, centrada en la innovación, la experiencia del cliente y la inversión a largo plazo, lo convirtió en una de las figuras más influyentes del mundo de los negocios y la tecnología.

- _"Si decides que solo harás las cosas que sabes que funcionarán, dejarás muchas oportunidades sobre la mesa."_
- _"Nos enfocamos obsesivamente en el cliente y no en la competencia."_
- _"Tu marca es lo que la gente dice de ti cuando no estás en la habitación."_

## Criptografía

Es el proceso de encriptado y desencriptado un mensaje con la misma clave recreada o privada.
El objetivo es que no sea descifrada por el criptoanálisis.

### AES

AES (Advanced Encryption Standard) es uno de los algoritmos de cifrado simétrico más utilizados en la actualidad. Fue adoptado como estándar por el gobierno de los Estados Unidos y se caracteriza por utilizar claves de 128, 192 o 256 bits para proteger la información. Su diseño ofrece una combinación de alta seguridad y eficiencia, permitiendo cifrar grandes cantidades de datos de manera rápida y confiable.

### XOR

XOR (Exclusive OR) es una operación lógica utilizada en criptografía para combinar datos con una clave mediante la aplicación de la función OR exclusiva. Cuando un bit del mensaje se combina con un bit de la clave, el resultado es 1 si ambos bits son diferentes y 0 si son iguales. Esta propiedad permite que la misma operación sea utilizada tanto para cifrar como para descifrar la información.

## Tarea

Realizar 4 ejercicios de encriptación y desencriptación con XOR tal como el ejemplo Linux.

### CAT

Clave
: `K` - 75

| Carácter | ASCII | Operación XOR         | Resultado |
| -------- | ----- | --------------------- | --------- |
| C        | 67    | $$67 \oplus 75 = 8$$  | 8         |
| A        | 65    | $$65 \oplus 75 = 10$$ | 10        |
| T        | 84    | $$84 \oplus 75 = 31$$ | 31        |

: Operación de Encriptado para `CAT`

| Valor Cifrado | Operación XOR         | Resultado ASCII | Carácter |
| ------------- | --------------------- | --------------- | -------- |
| 8             | $$8 \oplus 75 = 67$$  | 67              | C        |
| 10            | $$10 \oplus 75 = 65$$ | 65              | A        |
| 31            | $$31 \oplus 75 = 84$$ | 84              | T        |

: Operación de Desencriptado para `CAT`

### DOG

Clave
: `K` - 75

| Carácter | ASCII | Operación XOR         | Resultado |
| -------- | ----- | --------------------- | --------- |
| D        | 68    | $$68 \oplus 75 = 15$$ | 15        |
| O        | 79    | $$79 \oplus 75 = 4$$  | 4         |
| G        | 71    | $$71 \oplus 75 = 12$$ | 12        |

: Operación de Encriptado para `DOG`

| Valor Cifrado | Operación XOR         | Resultado ASCII | Carácter |
| ------------- | --------------------- | --------------- | -------- |
| 15            | $$15 \oplus 75 = 68$$ | 68              | D        |
| 4             | $$4 \oplus 75 = 79$$  | 79              | O        |
| 12            | $$12 \oplus 75 = 71$$ | 71              | G        |

: Operación de Desencriptado para `DOG`

### SUN

Clave
: `K` - 75

| Carácter | ASCII | Operación XOR         | Resultado |
| -------- | ----- | --------------------- | --------- |
| S        | 83    | $$83 \oplus 75 = 24$$ | 24        |
| U        | 85    | $$85 \oplus 75 = 30$$ | 30        |
| N        | 78    | $$78 \oplus 75 = 5$$  | 5         |

: Operación de Encriptado para `SUN`

| Valor Cifrado | Operación XOR         | Resultado ASCII | Carácter |
| ------------- | --------------------- | --------------- | -------- |
| 24            | $$24 \oplus 75 = 83$$ | 83              | S        |
| 30            | $$30 \oplus 75 = 85$$ | 85              | U        |
| 5             | $$5 \oplus 75 = 78$$  | 78              | N        |

: Operación de Desencriptado para `SUN`

### BOOK

Clave
: `K` - 75

| Carácter | ASCII | Operación XOR        | Resultado |
| -------- | ----- | -------------------- | --------- |
| B        | 66    | $$66 \oplus 75 = 9$$ | 9         |
| O        | 79    | $$79 \oplus 75 = 4$$ | 4         |
| O        | 79    | $$79 \oplus 75 = 4$$ | 4         |
| K        | 75    | $$75 \oplus 75 = 0$$ | 0         |

: Operación de Encriptado para `BOOK`

| Valor Cifrado | Operación XOR        | Resultado ASCII | Carácter |
| ------------- | -------------------- | --------------- | -------- |
| 9             | $$9 \oplus 75 = 66$$ | 66              | B        |
| 4             | $$4 \oplus 75 = 79$$ | 79              | O        |
| 4             | $$4 \oplus 75 = 79$$ | 79              | O        |
| 0             | $$0 \oplus 75 = 75$$ | 75              | K        |

: Operación de Desencriptado para `BOOK`
