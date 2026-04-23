# 21 - Apr - 2026

## Objetivos de Aprendizaje

1. Herramienta Tecnológica para asegurar la triada CID
2. _Ethical Hacking_
    - Reconocimiento Pasivo
        - Google Dorks
        - Comandos Linux
    - Reconocimiento Activo
        - `nmap`
        - `enum4linux`
3. Escaneo
    - Herramientas Tecnológicas
        - `nmap --vulnerability`
        - **SIEM**
        - **UTM**
        - **NGFM**
        - **OpenXDR**
    - Equipos Organizacionales
        - **SOC**
        - **CERT/CSIRT**

## Meditación

### Fórmula de la Felicidad

$$F = M + V + CA$$

F
: Felicidad

M
: Metas

V
: Vínculos

CA
: Cualidades Afectivas

## CERT / CSIRT

Equipos de Respuesta a Incidentes Informáticos.

Servicios Proactivos, Preventivos y Correctivos

### Definiciones

CERT
: Computer Emergency Response Team

CSIRT
: Computer Security Incident Response Team

SOC
: Security Operation Center

### Actividades

- Análisis de Vulnerabilidades
- Inteligencia de Amenazas
- Operativos
    - Software Especializado
        - Shodan
    - Hardware Especializado
        - SIEM
        - UTM
        - NGFW
        - XDR

## SIEM

1. Estructura de un SIEM
2. Marcas
3. Costos
4. Funcionalidades

![Diagrama de Funcionamiento SIEM](./img/siem.png)

### Definiciones

SIEM
: Security Information & Event Management

## Herramientas Tecnológicas

| Concepto | Acrónimo (significado) | Tipo | Función principal | Enfoque | Ejemplo | ¿Cubre capas OSI? | ¿Qué aspecto de la triada CID cubre? |
|----------|------------------------|------|------------------|---------|---------|-------------------|--------------------------------------|
| SOC | Security Operations Center | Organizativo | Monitoreo continuo de seguridad | Detección y vigilancia | Splunk | No aplica directamente (analiza eventos de todas las capas) | Confidencialidad / Integridad / Disponibilidad (indirecto, mediante monitoreo) |
| CSIRT | Computer Security Incident Response Team | Organizativo | Respuesta a incidentes | Gestión y mitigación | CERT-EU | No aplica (gestión de incidentes) | Confidencialidad / Integridad / Disponibilidad (recuperación y respuesta) |
| SIEM | Security Information and Event Management | Tecnológico | Recolección y correlación de logs | Análisis y alertas | IBM QRadar | Indirecto (principalmente capas 2–7 según logs) | Confidencialidad / Integridad / Disponibilidad (detección de incidentes) |
| OpenXDR | Open Extended Detection and Response | Tecnológico | Detección y respuesta integrada | Correlación + automatización | Integra múltiples fuentes | Indirecto (capas 2–7 según integración) | Confidencialidad / Integridad / Disponibilidad (respuesta automatizada) |
| UTM | Unified Threat Management | Tecnológico | Seguridad perimetral todo-en-uno | Prevención centralizada | FortiGate | Parcial (capas 3–7) | Confidencialidad / Integridad / Disponibilidad (bloqueo amenazas en perímetro) |
| NGFW | Next-Generation Firewall | Tecnológico | Firewall avanzado con inspección profunda | Control de tráfico y aplicaciones | Palo Alto Networks NGFW | Capas 3–7 | Confidencialidad / Integridad / Disponibilidad (control granular del tráfico) |
