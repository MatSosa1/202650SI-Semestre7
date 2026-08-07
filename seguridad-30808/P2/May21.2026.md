# 21 - Mayo - 2026

## Objetivos de Aprendizaje

1. Introducción a la Criptografía
  - Definiciones
  - Historia
2. Práctica de Laboratorio: Criptografía basada en el Código César

## Meditación

### Thomas Alba Edison

Nació en 1912 en Ohio, Estados Unidos.
No terminó sus estudios pero fue uno de los mayores inventores de la humanidad.

- Bombilla
- Fonógrafo
- Quinetoscopio

Cuenta la leyenda que él era incomprendido dentro de su escuela.
Un día, el director le envió una carta a su madre donde decía que él era muy tonto para entender.
Sin embargo, al leerla su madre, le dijo todo lo contrario: que era un genio y que no podían darle clases porque no tenían personal para enseñarle.

- _"El éxito llega a quienes perseveran"_
- _"Hay una manera de hacerlo mejor; encuéntrala"_
- _"No he fracasado, simplemente he encontrado 10000 formas que no funcionan"_
- _"Casi todo mundo deja pasar la oportunidad porque llega disfrazada de trabajo duro"_
- _"Para tener una gran idea, hay que tener muchas"_
- _"Genious is one percent inspiration, ninety-nine percent perspiration"_

# Criptología

La criptología es la ciencia que estudia los métodos y técnicas relacionados con la protección y el análisis de la información. Su objetivo principal es garantizar la seguridad de los datos mediante mecanismos que permitan ocultar su contenido a personas no autorizadas y, al mismo tiempo, desarrollar procedimientos para evaluar o comprometer dichos mecanismos. La criptología constituye la base teórica de gran parte de la seguridad informática moderna y desempeña un papel fundamental en la protección de las comunicaciones digitales.

Esta disciplina se divide principalmente en dos áreas: la criptografía y el criptoanálisis. Mientras la criptografía se enfoca en diseñar sistemas seguros para proteger la información, el criptoanálisis estudia las técnicas utilizadas para descubrir vulnerabilidades o descifrar mensajes sin conocer las claves legítimas. La interacción entre ambas áreas impulsa el desarrollo continuo de algoritmos más robustos y métodos de protección más eficaces.

![Dispositivo Utilizado para Cifrar en la Antiguedad](./img/cryptology_device.jpg)

## Criptografía

La criptografía es la rama de la criptología encargada de desarrollar técnicas para proteger la información mediante procesos de cifrado y descifrado. Su finalidad es transformar datos legibles en un formato incomprensible para cualquier persona que no posea la clave adecuada, garantizando así la confidencialidad de la información durante su almacenamiento o transmisión.

Además de la confidencialidad, la criptografía moderna proporciona mecanismos para asegurar la integridad, autenticidad y no repudio de los datos. Tecnologías como el cifrado simétrico, el cifrado asimétrico, las funciones hash y las firmas digitales son ampliamente utilizadas en aplicaciones como banca electrónica, comercio digital, redes privadas virtuales y sistemas de autenticación seguros.

## Criptoanálisis

![Representación del Análisis de la Criptografía](./img/cryptoanalisis.png)

El criptoanálisis es la rama de la criptología dedicada al estudio y evaluación de sistemas criptográficos con el propósito de identificar debilidades o recuperar información protegida sin disponer de las claves legítimas. Esta disciplina analiza algoritmos, protocolos y mecanismos de cifrado para determinar su nivel de resistencia frente a distintos tipos de ataques.

Su importancia radica en que permite validar la seguridad de los sistemas criptográficos antes de que sean utilizados en entornos reales. Los especialistas en criptoanálisis emplean métodos matemáticos, estadísticos y computacionales para descubrir vulnerabilidades, contribuyendo al fortalecimiento de los algoritmos y al desarrollo de soluciones más seguras para la protección de la información.

## Tipos de Criptología

La criptología puede clasificarse principalmente en criptografía y criptoanálisis, aunque dentro de estas áreas existen diversas especializaciones. La criptografía incluye técnicas como la criptografía simétrica, asimétrica, de clave pública y las funciones hash, cada una diseñada para resolver necesidades específicas de seguridad en la gestión de la información.

Por otro lado, el criptoanálisis abarca diferentes métodos de ataque y evaluación, como el análisis de frecuencia, los ataques de fuerza bruta y el estudio de vulnerabilidades matemáticas en algoritmos criptográficos. La combinación de ambas áreas permite mantener un equilibrio entre la creación de mecanismos de protección y la evaluación constante de su efectividad frente a nuevas amenazas tecnológicas.

## Código César

$$ C(x) = (x + n) mod26 $$
$$ D(x) = (x - n) mod26 $$

Donde:

C
: Cifrado

D
: Descifrado

x
: Mensaje o la posición de la letra en el abecedario o alfabeto

n
: Desplazamiento

26
: Es el número de letras del alfabeto latino
