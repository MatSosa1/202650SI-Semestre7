# Fórmulas

$$ \text{Indice de Calidad} = 100 - \text{Reglas Incumplidas} $$

$$ \text{Reglas Incumplidas} = 100 * \frac{\sum_{n = 1}^{5} \text{Número de Errores}_i * \text{Puntuación Error}_i}{\text{Número Líneas Código}} $$

Es ideal que se mantenga un **valor mayor a 90%** para el índice de calidad.

# calculadora.py

![Análisis en SonarQube sobre proyecto `calculadora.py`](./img/calculadora.png)

Num Errores | Tipo Error | Puntuación | 
:---:|:---:|:---:|
0 | Blocking | 9 |
3 | High | 5 |
0 | Medium | 3 |
0 | Low | 1 |
0 | Info | 0 |

: Conteo total de Número de Errores con Respecto a su Puntuación en Proyecto `calculadora.py`

$$ \text{Reglas Incumplidas} = 100 * \frac{(0 + 15 + 0 + 0 + 0)}{67} = 22.38\% $$

$$ \text{Indice de Calidad} = 100 - 22.38 = 77.62\% $$

# DVWA

![Análisis en SonarQube sobre proyecto `DVWA`](./img/dvwa.png)

Num Errores | Tipo Error | Puntuación | 
:---:|:---:|:---:|
7 | Blocking | 9 |
114 | High | 5 |
241 | Medium | 3 |
696 | Low | 1 |
5 | Info | 0 |

: Conteo total de Número de Errores con Respecto a su Puntuación en Proyecto `DVWA`

$$ \text{Índice de Calidad} = 100 * \frac{(63 + 570 + 723 + 696 + 0)}{9300} = 22.06\% $$

$$ \text{Indice de Calidad} = 100 - 22.06 = 77.94\% $$
