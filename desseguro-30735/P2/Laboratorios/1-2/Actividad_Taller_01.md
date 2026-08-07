# Actividad de reto: detector explicable de código vulnerable

## Objetivo

Mejorar el modelo del notebook para clasificar fragmentos de código como `vulnerable` o `seguro`, evaluar su desempeño e interpretar sus predicciones usando LIME.

## Contexto

En el notebook se construyó un modelo de minería de datos aplicado a la detección de vulnerabilidades en fragmentos de código. El modelo transforma código fuente en variables numéricas mediante TF-IDF, entrena un clasificador binario y usa LIME para explicar qué tokens o patrones influyen en la predicción.

En esta actividad, los estudiantes deberán probar el modelo con fragmentos nuevos, analizar sus resultados y reflexionar sobre sus limitaciones.

## Instrucciones

### Selección de fragmentos

Seleccionen al menos 10 fragmentos nuevos de código:

- 5 fragmentos vulnerables.
- 5 fragmentos seguros.

Los fragmentos pueden estar escritos en Python, JavaScript, Java, PHP, C/C++ u otro lenguaje de programación. Se recomienda incluir vulnerabilidades como SQL Injection, Cross-Site Scripting, Command Injection, Path Traversal, uso inseguro de `eval` o deserialización insegura.

### Etiquetado manual

Clasifiquen manualmente cada fragmento con una de las siguientes etiquetas:

- `vulnerable`
- `seguro`

Además, indiquen brevemente por qué asignaron esa etiqueta.

### Evaluación con el modelo

Ejecuten el modelo del notebook sobre los fragmentos seleccionados y registren:

- Fragmento de código.
- Etiqueta real asignada manualmente.
- Predicción del modelo.
- Probabilidad de `seguro`.
- Probabilidad de `vulnerable`.
- Resultado: correcto o incorrecto.

Pueden usar una tabla como la siguiente:

| N.º | Tipo de fragmento | Etiqueta real | Predicción del modelo | Prob. seguro | Prob. vulnerable | ¿Correcto? |
|---:|---|---|---|---:|---:|---|
| 1 | SQL Injection | vulnerable | vulnerable | 0.20 | 0.80 | Sí |
| 2 | Consulta parametrizada | seguro | seguro | 0.85 | 0.15 | Sí |

### Explicabilidad con LIME

Elijan 3 fragmentos que el modelo haya clasificado como `vulnerable` y expliquen cada predicción usando LIME.

Para cada fragmento, respondan:

- ¿Qué tokens o patrones tuvieron mayor peso hacia la clase `vulnerable`?
- ¿La explicación de LIME coincide con el riesgo real del fragmento?
- ¿El modelo parece detectar una vulnerabilidad real o solo palabras sospechosas?
- ¿Qué partes del código deberían revisarse manualmente?

### Análisis de errores

Identifiquen si hubo:

- Falsos positivos: código seguro clasificado como vulnerable.
- Falsos negativos: código vulnerable clasificado como seguro.

Luego expliquen posibles causas de esos errores. Por ejemplo:

- El modelo no conoce suficiente variedad de ejemplos.
- El fragmento usa nombres de variables ambiguos.
- La vulnerabilidad depende del contexto y no solo del texto.
- El modelo aprendió patrones superficiales.

### Propuesta de mejora

Propongan al menos una mejora para el modelo. Algunas opciones son:

- Cambiar parámetros de TF-IDF.
- Probar otro clasificador.
- Agregar más ejemplos reales.
- Balancear mejor las clases.
- Separar el análisis por tipo de vulnerabilidad.
- Usar representaciones más avanzadas de código.
- Combinar el modelo con herramientas de análisis estático.

## Producto final

Entreguen un informe breve que contenga:

- Tabla con los 10 fragmentos evaluados.
- Resultados de predicción y probabilidades.
- Explicaciones LIME de 3 fragmentos vulnerables.
- Análisis de falsos positivos y falsos negativos.
- Propuesta de mejora del modelo.
- Conclusión sobre la utilidad y limitaciones del enfoque.

## Preguntas guía

- ¿Qué tipo de vulnerabilidad fue más fácil de detectar?
- ¿Qué fragmentos confundieron al modelo?
- ¿Qué tokens hicieron que el modelo clasificara como `vulnerable`?
- ¿Las explicaciones de LIME fueron técnicamente razonables?
- ¿Qué riesgos tendría usar este modelo en un entorno real sin revisión humana?
- ¿Cómo se podría mejorar el dataset para obtener mejores resultados?

## Criterios de evaluación

| Criterio | Puntaje |
|---|---:|
| Selección y etiquetado correcto de fragmentos | 20% |
| Evaluación del modelo con probabilidades y resultados | 25% |
| Uso e interpretación de LIME | 25% |
| Análisis crítico de errores | 20% |
| Propuesta de mejora | 10% |

## Recomendación final

Recuerden que este modelo tiene fines educativos. Un detector automático de vulnerabilidades no debe reemplazar la revisión humana, las pruebas de seguridad ni las herramientas especializadas de análisis estático o dinámico.
