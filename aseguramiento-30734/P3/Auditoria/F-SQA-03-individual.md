**07-I. Plan de Acciones Correctivas — Versión Individual**

> Formato individual que cada auditor entrega al Auditor Líder (Marcos Escobar) para su consolidación en **F-SQA-03.md**. Contiene las propuestas de cambio y acciones correctivas del área asignada al integrante. Entrega máxima: 24/07/2026.

**7.1 Control Documental**

Código del documento: PLA-SQA-PAC-001-I

Versión: 1.0

Fecha de emisión: 26/07/2026

Proyecto/Organización: Auditoría interna SQA al proyecto Healthy+

Auditor (integrante): Mateo Sosa

Área / Fase auditada: Planificación y Requisitos

Elaborado por: Mateo Sosa

Revisado por: Marcos Escobar (Auditor Líder)

**7.2 Historial de Cambios**

| **Versión** | **Fecha** | **Descripción del cambio** |
| --- | --- | --- |
| 1.0 | 26/07/2026 | Creación inicial del plan de acciones correctivas individual. |

**7.3 Objetivo**

Proponer las acciones correctivas y preventivas para los hallazgos detectados por el integrante en su área, con su análisis de causa raíz y responsable sugerido, para su integración en el plan consolidado.

**7.4 Alcance**

Este plan aplica a los hallazgos registrados por el integrante en su F-SQA-02 individual que requieran tratamiento correctivo o preventivo.

**7.5 Metodología de Tratamiento**

* Identificación del hallazgo (referencia al F-SQA-02 individual).
* Análisis de causa raíz (5 Porqués, Ishikawa o Pareto).
* Definición de la acción correctiva o preventiva.
* Asignación de responsable sugerido y fecha compromiso.
* Verificación de eficacia posterior por el equipo de SQA.

**7.6 Propuesta de Acciones Correctivas y de Cambios**

| **Nro.** | **Hallazgo (ref. F-SQA-02-I)** | **Causa raíz** | **Acción correctiva / preventiva propuesta** | **Tipo** | **Responsable sugerido** | **Fecha compromiso** | **Estado** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | LBA – Versionamiento (Hallazgo 1) | No existe un procedimiento formal para registrar el historial de versiones en el README. | Actualizar el README incorporando el historial completo de versiones del documento y establecer como práctica obligatoria registrar cada modificación futura. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 2 | LBC – Versionamiento (Hallazgo 2) | Ausencia de control documental sobre el historial de cambios. | Incorporar todas las versiones previas en el README y definir un procedimiento de control de versiones para los documentos de línea base. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 3 | LBD – Versionamiento (Hallazgo 3) | El versionamiento no fue documentado desde el inicio del proyecto. | Registrar retrospectivamente las versiones generadas y exigir que toda modificación futura sea documentada antes de su publicación. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 4 | LBD – Diagrama de Casos de Uso (Hallazgo 3.1) | Definición incompleta de actores y alcance funcional del sistema. | Revisar el modelo de casos de uso para justificar los actores existentes o incorporar el actor que interactúa con la persistencia de datos, documentando el criterio adoptado. | Correctiva / Preventiva | Abner Arboleda | 26/07/2026 | Propuesta |
| 5 | LBR – Fechas de creación y firma (Hallazgo 4.1) | Inconsistencia entre las fechas registradas en el README y las evidencias documentales. | Revisar y corregir las fechas oficiales de creación, aprobación y versionamiento, asegurando que toda la documentación mantenga coherencia cronológica. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 6 | ERS – Fechas de creación y firma (Hallazgo 5.1) | Falta de validación entre el versionamiento y las fechas de aprobación del documento. | Actualizar el registro de versiones para que coincida con las fechas reales de creación y aprobación, implementando una revisión documental antes de publicar nuevas versiones. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 7 | ERS – Aprobación (Hallazgo 5.2) | El proceso de aprobación no cuenta con un mecanismo uniforme de verificación documental. | Formalizar un procedimiento de revisión y aprobación que asegure la existencia de firmas, fechas y registros consistentes antes de liberar una versión oficial. | Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 8 | Cronograma – Versionamiento (Hallazgo 6) | Historial de cambios incompleto en el repositorio documental. | Incorporar el historial de versiones al README y exigir que cada actualización del cronograma incluya su respectivo registro de cambios. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 9 | Cronograma – Aprobación (Hallazgo 6.1) | El proceso de aprobación depende de controles manuales. | Implementar una lista de verificación previa a la aprobación para validar integridad, firmas y consistencia del documento. | Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 10 | Cronograma – Fechas de creación (Hallazgo 6.2) | Registro cronológico inconsistente entre documentos relacionados. | Corregir las fechas del README para reflejar la fecha real de creación del cronograma y validar la consistencia con el historial de versiones. | Correctiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 11 | Matriz IREB – Versionamiento (Hallazgo 7) | El historial de versiones no fue mantenido durante el desarrollo del proyecto. | Registrar todas las versiones existentes y establecer un procedimiento de actualización obligatoria del README para futuras modificaciones. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 12 | Matriz IREB – Aprobación (Hallazgo 7.1) | No existe una verificación estandarizada antes de aprobar la documentación. | Definir un flujo de revisión y aprobación que valide la documentación antes de su liberación oficial. | Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 13 | Matriz IREB – Fechas de creación (Hallazgo 7.2) | Desalineación entre las fechas del README y el historial de cambios. | Corregir las fechas registradas y verificar que el historial documental mantenga coherencia temporal en todas las versiones. | Correctiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 14 | Historias de Usuario – Versionamiento (Hallazgo 8) | El control de versiones fue realizado de manera parcial. | Completar el historial de cambios en el README e incorporar una política de actualización documental obligatoria. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 15 | Historias de Usuario – Estado de requisitos (Hallazgo 8.1) | Falta de sincronización entre los artefactos que gestionan el avance del proyecto. | Revisar y unificar el estado de los requisitos funcionales entre la matriz de historias de usuario y el cronograma, definiendo una única fuente oficial de seguimiento. | Correctiva / Preventiva | Marcelo Acuña | 26/07/2026 | Propuesta |
| 16 | Actas de Reunión – Fechas de creación (Hallazgo 9) | Registro incorrecto de las fechas en el README. | Actualizar las fechas para que correspondan con la fecha real de elaboración del acta y establecer una revisión documental antes de su publicación. | Correctiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 17 | Backlog – Versionamiento (Hallazgo 10) | El historial de cambios no fue registrado de forma continua. | Completar el historial de versiones del backlog y definir un procedimiento para documentar cada modificación realizada. | Correctiva / Preventiva | Christian Bonifaz | 26/07/2026 | Propuesta |
| 18 | Backlog – Conclusiones y recomendaciones (Hallazgo 10.1) | El documento fue considerado finalizado sin incluir el análisis de resultados. | Incorporar una sección de conclusiones y recomendaciones basada en el análisis del comportamiento del backlog y establecerla como requisito para futuras entregas. | Correctiva / Preventiva | Marcelo Acuña | 26/07/2026 | Propuesta |
| 19 | Backlog – Fechas de creación (Hallazgo 10.2) | Inconsistencia entre la fecha registrada y el historial de versiones. | Corregir la fecha de creación registrada en el README y validar su consistencia con el historial documental antes de aprobar nuevas versiones. | Correctiva | Christian Bonifaz | 26/07/2026 | Propuesta |

**7.7 Resumen del Área**

* Total de acciones propuestas: 19
* Acciones correctivas: 16
* Acciones preventivas: 15

**7.8 Cierre**

Las acciones propuestas se entregan al Auditor Líder para su consolidación en el plan F-SQA-03 y su posterior negociación con la parte auditada en la reunión de cierre.
