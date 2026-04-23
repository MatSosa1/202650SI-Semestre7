# Vulnerabilidades y sus Costes

El riesgo aumenta desde que se descubre la vulnerabilidad hasta que se parchea.

![Zerodium: Página para ver vulnerabilidades](https://zerodium.com/)

## Gestión de Vulnerabilidades

Dada la gran cantidad de vulnerabilidades descubiertas, es necesario disponer de estándares que permitan referenciarlas unívocamente, para poder conocer su gravedad de forma objetiva y obtener el conocimiento necesario para mitigarlas.

Existen varios estándares:

- CVE
- CWE
- etc.

### CVE (Common Vulnerabilities and Exposures)

Es un diccionario o catálogo público de vulnerabilidades, administrado por MITRE, que normaliza su descripción y las organiza desde diferentes tipos de vista (vulnerabilidades web, de diseño, implementación, etc).

$$\text{CVE-2012-4212}$$

| CVE, seguido del año en el que se asignó el código a la vulnerabilidad |
| Número de cuatro cifras que identifica la vulnerabilidades del año |

![https://www.cvedetails.com](https://www.cvedetails.com)

![https://cve.mitre.org/cve/search_cve_list.html](https://cve.mitre.org/cve/search_cve_list.html)

### CVSS

![Calculadora NIST](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)

Es un sistema que escalona la severidad de una vulnerabilidad, de manera estricta a través de fórmulas, proporcionándolo un estándar para comunicar las características y el impacto de una vulnerabilidad identificada con su código CVE.

Su modelo cuantitativo asegura una medición exacta y repetible a la vez que permite ver características subyacentes que se usaron para generar su puntuación.

El cálculo se realiza en base a tres tipos de métricas base, temporales y ambientales, siendo las dos últimas opcionales.

En cuanto a las métricas base, se tienen dos subconjuntos:

Explotabilidad
: Vectores de acceso

Impacto
:

**Revisar Fórmula**

### CWE (Common Weakness Enumeration)

Estándar internacional y de libre uso que ofrece un conjunto unificado de debilidades o defectos de software medibles.

Sus principales objetivos son:

- Proporcionar un lenguaje común para describir los defectos y debilidades de seguridad de software en su arquitectura, diseño y codificación.
- Proporcionar un estándar de comparación de herramientas de auditoría seguridad de software.
- Proporcionar una línea base para la identificación de vulnerabilidades, su mitigación y los esfuerzos de prevención.

Para documentar vulnerabilidades:

- Nombre del tipo de debilidad
- Descripción del tipo
- Términos alternativos para la debilidad
- Descripción del comportamiento de la debilidad
- Descripción de la debilidad
- Probabilidad de explotar la debilidad
- Descripción de las consecuencias de la explotación
- Posibles mitigaciones
- Otras debilidades relacionadas
- Taxonomías de las fuentes
- Ejemplos de código para los lenguajes/arquitecturas
- Identificadores de vulnerabilidades CVE para las que ese tipo de debilidad existe
- Referencias

### Otras Clasificaciones

Existen muchas clasificaciones ot axonomías de vulnerabilidades, unas se adaptan a todo tipo de aplicaciones, como son:

MITRE Top 25
: ![URL](http://cwe.mitre.org/top25)

SANS Top 20
: ![URL](http://www.sans.org/top20)

OWASP Top 10
: ![]

WASC Threat Clasification v2.0
: 
