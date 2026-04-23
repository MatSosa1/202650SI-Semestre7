---
author: Mateo Sosa
nrc: 30808
assignment: Ingeniería de la Seguridad del Software

---

# Objetivos de Aprendizaje

Al finalizar esta práctica, usted será capaz de:

- Diferenciar entre reconocimiento pasivo y activo
- Aplicar escaneo de red con nmap
- Analizar información de un host público controlado: `scanme.nmap.org`
- Utilizar enum4linux en un entorno local controlado
- Identificar:
  - Puertos abiertos y servicios
  - Sistema operativo aproximado
  - Usuarios, grupos y recursos compartidos
  - Evaluar riesgos de exposición de información

# Topología del experimento

- Virtualización: VirtualBox o VMware
- Máquinas virtuales:
  - Ubuntu Desktop 24.04.5 LTS (Noble Numbat) — ejecución de búsquedas y análisis, objetivo local con servicios SMB habilitados
  - Kali Linux 2026.3 — apoyo en análisis de seguridad (opcional)
- Herramientas:
  - Navegador web (Firefox/Chrome)
- Red: Ambas máquinas conectadas en red NAT (entorno controlado)
- Objetivo público controlado: `scanme.nmap.org`

# Marco Teórico

El reconocimiento es la fase inicial en la evaluación de seguridad de redes y sistemas, cuyo objetivo es recopilar información relevante sobre la infraestructura objetivo, como hosts activos, puertos abiertos y servicios disponibles. Esta etapa es clave para comprender la superficie de ataque y posibles vectores de riesgo (Stallings, 2018).

Se distingue entre reconocimiento pasivo y activo. El reconocimiento pasivo obtiene información sin interactuar directamente con el sistema, mientras que el activo implica interacción mediante técnicas como escaneo de puertos o identificación de servicios, lo que permite mayor precisión, aunque con mayor probabilidad de detección (Bishop, 2018).

En este contexto, **Nmap** es una herramienta fundamental para el reconocimiento activo, ya que permite descubrir hosts, identificar puertos y servicios, y realizar análisis de red de forma eficiente (Nmap Project, 2024). Por otro lado, **enum4linux** se utiliza para la enumeración de sistemas que exponen servicios SMB, permitiendo obtener información como usuarios, grupos y recursos compartidos (Kali Tools, 2024).

El uso de entornos controlados como `scanme.nmap.org` permite practicar estas técnicas de forma segura.

| Herramienta | Tipo de reconocimiento | Descripción | Ejemplo de uso |
|------------|----------------------|-------------|----------------|
| `nmap -sn` | Pasivo / descubrimiento | Identifica hosts activos sin escanear puertos | `nmap -sn 192.168.56.0/24` |
| `nmap -sV` | Activo | Detecta servicios y versiones | `nmap -sV scanme.nmap.org` |
| `nmap -O` | Activo | Identifica sistema operativo | `nmap -O scanme.nmap.org` |
| `nmap` | Activo | Escaneo general del host | `nmap scanme.nmap.org` |
| `enum4linux -a` | Activo (SMB) | Extrae usuarios, grupos y recursos | `enum4linux -a 192.168.56.20` |
| `smbclient -L` | Activo | Enumera recursos compartidos | `smbclient -L //192.168.56.20 -N` |
| `who / w` | Local | Muestra usuarios conectados | `who` / `w` |
| `host / dig` | Pasivo | Consulta DNS | `dig scanme.nmap.org` |

# Desarrollo

# Conclusiones

- El reconocimiento es la fase inicial de cualquier ataque
- `scanme.nmap.org` permite practicar escaneo sin riesgo legal
- SMB puede exponer información sensible si está mal configurado
- Nmap y enum4linux permiten analizar la superficie de ataque
