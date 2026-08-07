**05-I. Registro de Hallazgos — Versión Individual**

**5.1 Control Documental**

Código del documento: PLA-SQA-RH-001-I

Versión: 1.0

Fecha de emisión: 26/07/2026

Proyecto/Organización: Auditoría interna SQA al proyecto Healthy+

Auditor (integrante): Mateo Sosa

Área / Fase auditada: Planificación y Requisitos

Elaborado por: Mateo Sosa

Revisado por: Marcos Escobar (Auditor Líder)

**5.2 Historial de Cambios**

| **Versión** | **Fecha** | **Descripción del cambio** |
| --- | --- | --- |
| 1.0 | 26/07/2026 | Creación inicial del registro de hallazgos individual. |

**5.3 Objetivo**

Registrar y clasificar los hallazgos detectados por el integrante durante la evaluación de su área, con su evidencia, severidad y responsable, para su integración en el registro de hallazgos consolidado.

**5.4 Alcance**

Este registro aplica a todos los hallazgos levantados por el integrante dentro del área o fase auditada, desde su identificación hasta su entrega al Auditor Líder.

**5.5 Registro de Hallazgos del Área**

| **Nro.** | **Proceso / Área** | **Hallazgo** | **Tipo** | **Evidencia** | **Severidad (Peso)** | **Responsable (auditado)** | **Acción Correctiva Sugerida** | **Estado** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LBA | Versionamiento | NC | [README de LBA](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBA/Readme.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 2 | LBC | Versionamiento | NC | [README de LBC](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBC/Readme.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 3 | LBD | Versionamiento | NC | [README de LBD](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBD/Readme.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 3.1 | LBD | Diagrama Casos Uso | OBS | [LBD](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBD/CU_V1.0.1.pdf) | Informativo (0) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Se registran los actores "Usuario/Cuidador" y "Reloj del Sistema", pero debido a que el sistema es un CRUD, no se identifica el actor que interactía con los datos, por lo que se supone se mantiene en memoria y se borra al cerrar el aplicativo. | Cerrado |
| 4 | LBR | Versionamiento | C | [README de LBR](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBR/Readme.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | - | Cerrado |
| 4.1 | LBR | Fechas de creación y firma | NC | [README de LBR](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBR/Readme.md), [ERS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBR/ERS_V1.0.0.pdf), [ERS Anexo](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.0.%20Linea%20Base/LBR/ERS_Anexo_V1.0.0.pdf) | Bloqueante (9) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Se audita de forma crítica las fechas de los documentos. Se advierte que el ERS ha sido formalmente firmado con fecha 24/05/2025, pero su versionamiento en el Readme se contempla el 08/01/2026. Siendo esta la única versión, debería coincidir con la fecha de creación. | Cerrado |
| 5 | ERS | Versionamiento | C | [README de Especificación RS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/README.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Existe versionamiento, pero se solicita registrarlo dentro del Readme. | Cerrado |
| 5.1 | ERS | Fechas de creación y firma | NC | [README de Especificación RS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/README.md), [ERS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/ERS_V1.0.1.pdf), [ERS Anexo](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/ERS_Anexo_V1.0.0.pdf) | Bloqueante (9) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Se audita de forma crítica las fechas de los documentos. Se advierte que el ERS ha sido formalmente firmado con fecha 24/05/2025, pero su versionamiento en el Readme se contempla el 08/01/2026. Siendo esta la única versión, debería coincidir con la fecha de inicio | Cerrado |
| 5.2 | ERS | Aprobación | C | [README de Especificación RS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/README.md), [ERS](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/ERS_V1.0.1.pdf), [ERS Anexo](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.1%20Especificación%20RS/ERS_Anexo_V1.0.0.pdf) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | - | Cerrado |
| 6 | Cronograma | Versionamiento | NC | [README de Cronograma](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/README.md), [Cronograma](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/CRON_V3.0.0.xlsx) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 6.1 | Cronograma | Aprobación | C | [README de Cronograma](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/README.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | - | Cerrado |
| 6.2 | Cronograma | Fechas de Creación | NC | [README de Cronograma](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/README.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | El documento, según el Readme, tiene por fecha de creación 08/01/2026, pero su versionamiento indica la fecha 15/06/2025. | Cerrado |
| 7 | Matriz IREB | Versionamiento | NC | [README de Matriz IREB](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.3%20Matriz%20IREB/Readme.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 7.1 | Matriz IREB | Aprobación | C | [README de Matriz IREB](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.3%20Matriz%20IREB/Readme.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | - | Cerrado |
| 7.2 | Matriz IREB | Fechas de Creación | NC | [README de Matriz IREB](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.3%20Matriz%20IREB/Readme.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | El documento, según el Readme, tiene por fecha de creación 08/01/2026, pero su versionamiento indica la fecha 02/07/2025. | Cerrado |
| 8 | Historias de Usuario | Versionamiento | NC | [README de Historias de Usuario](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.4%20Historias%20de%20Usuario/README.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 8.1 | Historias de Usuario | Estado de Requisitos | NC | [Matriz de Historias de Usuario](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.4%20Historias%20de%20Usuario/HU_V1.0.2.xlsx), [Cronograma](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/CRON_V3.0.0.xlsx) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | La información es contradictoria entre la matriz de historias de usuario y el cronograma, puesto que sus versiones finales presentan el estado de los requisitos funcionales como _completado_ (Cronograma) y _No iniciado_ (Historias de Usuario) a la vez. | Cerrado |
| 9 | Actas de Reunión | Fechas de Creación | NC | [README de Actas de Reunión](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.2%20Cronograma/README.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | La reunión, según el Readme, tiene por fecha de creación 25/01/2026, pero su versionamiento indica la fecha 01/02/2026. | Cerrado |
| 10 | Backlog | Versionamiento | NC | [README de Backlog](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.6%20Backlog/README.md) | Medio (3) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir versiones anteriores y registrarlas en el README.md | Cerrado |
| 10.1 | Backlog | Conclusiones y Recomendaciones | NC | [Backlog](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.6%20Backlog/BL_V2.0.0.xlsx) | Bajo (1) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | Añadir conclusiones y recomendaciones a la matriz del Backlog en base al diagrama de tiempo presentado. | Cerrado |
| 10.2 | Backlog | Fechas de Creación | NC | [README de Backlog](./27837_G1_ADS/Biblioteca%20Maestra/1.%20ELICITACIÓN/1.6%20Backlog/README.md) | Alto (5) | Marcelo Acuña, Abner Arboleda, Christian Bonifaz | El documento, según el Readme, tiene por fecha de creación 08/01/2026, pero su versionamiento indica la fecha 21/08/2025. | Cerrado |

**5.6 Clasificación de Hallazgos**

* **C:** Conformidad.
* **NC:** No conformidad (Mayor o Menor según el PLA-SQA-003).
* **OBS:** Observación u oportunidad de mejora.

**5.7 Pesos de Severidad (para el cálculo de Reglas Incumplidas)**

Bloqueante (9), Alto (5), Medio (3), Bajo (1) e Informativo (0), conforme al PLA-SQA-003.

**5.8 Resumen del Área**

* Total de hallazgos: 21
* No conformidades (NC): 15
* Observaciones (OBS): 1
* Defectos ponderados del área (suma de pesos): 86

**5.9 Cierre**

Cada hallazgo se entrega con evidencia objetiva y severidad asignada, para su integración y análisis en el registro consolidado F-SQA-02.
