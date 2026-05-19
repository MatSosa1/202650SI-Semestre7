# 16 - Abril - 2026

## Objetivos de Aprendizaje

- Herramientas tecnológicas para garantizar la tríada CID/CIA
- Comprender el escaneo de puertos y su importancia

## Meditación

Se recordó el terremoto en Ecuador del 16 de abril de 2016.


### Tríada CID

Confidencialidad
: Protección contra accesos no autorizados

Integridad
: Información no alterada

Disponibilidad
: Acceso cuando se requiera

NR
: No repudio

ID
: Identificación

AU
: Autenticación

TZ
: Trazabilidad

Resiliencia
: Capacidad de recuperación ante fallos

## Escaneo de puertos y su importancia

El escaneo de puertos es una técnica utilizada para identificar servicios disponibles y puertos abiertos en un sistema o red. Este proceso permite conocer qué aplicaciones están ejecutándose en un host y detectar posibles vulnerabilidades asociadas a servicios expuestos [@weidman2014penetration].

La importancia del escaneo de puertos radica en que constituye una de las primeras etapas dentro de auditorías de seguridad y pruebas de penetración. Herramientas especializadas permiten identificar configuraciones inseguras, servicios innecesarios y posibles vectores de ataque que podrían comprometer la infraestructura tecnológica [@scarfone2008guide].

![Representación Gráfica de las Conexiones entre Dispositivos mediante Internet](./img/port_scan.jpg)

## SIEM (Security Information and Event Management)

Los sistemas SIEM permiten recopilar, correlacionar y analizar eventos de seguridad provenientes de diferentes dispositivos y aplicaciones dentro de una organización. Estas plataformas centralizan registros de actividad para facilitar la detección temprana de incidentes y amenazas cibernéticas [@chuvakin2013logging].

Además de monitorear eventos en tiempo real, los SIEM ayudan a automatizar alertas, generar reportes y mantener trazabilidad sobre actividades sospechosas. Su implementación es fundamental para fortalecer la capacidad de respuesta ante incidentes y cumplir con normativas de seguridad y auditoría [@bejtlich2013practice].

![Security Information and Event Management](./img/siem.jpg)

## Herramientas tecnológicas

La tríada CID, también conocida como CIA por sus siglas en inglés, representa los principios fundamentales de la seguridad de la información: confidencialidad, integridad y disponibilidad. Para garantizar estos principios se utilizan herramientas tecnológicas enfocadas en cifrado, monitoreo, autenticación, control de acceso y respaldo de información [@stallings2018security].

Las organizaciones implementan soluciones de seguridad que permiten proteger datos sensibles, detectar actividades maliciosas y asegurar la continuidad operativa. Entre estas herramientas se incluyen sistemas de monitoreo de eventos, plataformas criptográficas y aplicaciones de análisis de red utilizadas tanto en entornos empresariales como académicos [@kim2021cybersecurity].

### Reconocimiento pasivo

El reconocimiento pasivo recopila información sobre un objetivo sin interactuar directamente con sus sistemas. Estas herramientas permiten obtener información relacionada con dominios, registros DNS, infraestructura y presencia digital utilizando fuentes públicas y abiertas [@haddad2019osint].

| Herramienta | Tipo | Función principal | Uso común |
|---|---|---|---|
| `nslookup` | Consulta DNS | Obtiene información de registros DNS | Resolución de dominios |
| `host` | Consulta DNS | Traduce dominios a IP y viceversa | Verificación rápida DNS |
| `dig` | Consulta DNS avanzada | Consulta detallada de registros DNS | Diagnóstico DNS |
| whoisdomaintool | OSINT | Consulta información WHOIS de dominios | Información de registro |
| DNSDumpster | OSINT DNS | Mapea infraestructura DNS | Reconocimiento de dominios |
| `dnsenum` | Enumeración DNS | Descubre subdominios y registros | Auditorías DNS |
| `dnsrecon` | Reconocimiento DNS | Recolección automatizada DNS | Pentesting |
| Google dorks | OSINT | Búsquedas avanzadas indexadas | Exposición de información |

: Herramientas de reconocimiento pasivo y su función

### Reconocimiento activo

El reconocimiento activo implica interacción directa con el objetivo mediante escaneos y consultas sobre sistemas y servicios disponibles. Estas herramientas permiten identificar hosts activos, puertos abiertos, sistemas operativos y configuraciones vulnerables [@weidman2014penetration].

Las técnicas de reconocimiento activo son ampliamente utilizadas en pruebas de penetración y auditorías de seguridad para evaluar el nivel de exposición de una infraestructura tecnológica [@ec2018ethical].

| Herramienta / Técnica | Función principal | Información obtenida | Uso común |
|---|---|---|---|
| `nmap` | Escaneo de red | Hosts, puertos y servicios | Reconocimiento de red |
| IP vecinas | Descubrimiento de hosts | Equipos cercanos en red | Mapeo de infraestructura |
| Sistemas operativos | Fingerprinting | Sistema operativo remoto | Análisis de objetivos |
| Protocolos | Detección de servicios | Protocolos activos | Auditoría de servicios |
| Puertos abiertos | Escaneo de puertos | Servicios expuestos | Identificación de riesgos |
| scanme.org | Entorno de pruebas | Simulación de escaneos | Prácticas legales |
| `enum4linux` | Enumeración SMB | Usuarios y recursos compartidos | Auditoría Windows/Linux |
| Criptografía | Protección de datos | Integridad y confidencialidad | Seguridad de información |
| OpenSSL | Herramienta criptográfica | Certificados y cifrado | Gestión TLS/SSL |
| GPG (GNU Privacy Guard) | Cifrado y firmas digitales | Protección y autenticación | Seguridad de archivos |

: Herramientas de reconocimiento activo y su función
