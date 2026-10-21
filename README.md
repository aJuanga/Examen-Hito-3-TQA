# Examen Práctico Hito 3 – TQA

Repositorio individual del Examen Práctico del Hito 3 de **Testing y Aseguramiento de la Calidad (TQA)** – UNIFRANZ.

- **Estudiante:** Juan Gabriel Ibañez Copatiti
- **Aplicación probada:** [SauceDemo – Swag Labs](https://www.saucedemo.com/)
- **Fecha de ejecución:** 20/10/2026
- **Seguimiento:** [GitHub Project Board](https://github.com/users/aJuanga/projects/3) e [Issues](https://github.com/aJuanga/Examen-Hito-3-TQA/issues)

## Propósito

Aplicar técnicas de caja negra, caja blanca, Gherkin y registro de defectos sobre una aplicación real de demostración, y organizar todo el trabajo con Git y GitHub.

## Resumen de resultados

| Actividad | Resultado |
|---|---|
| Caja negra | 5 casos diseñados y ejecutados: **3 PASS, 2 FAIL** |
| Bugs | 2 defectos reproducibles documentados (BUG-001 crítico, BUG-002 mayor) |
| Caja blanca | Cobertura de decisiones: mínimo 4 casos; los 3 casos diseñados cubren el 83 % y se propone CB-04 para llegar al 100 % |
| Gherkin | 2 features, 4 escenarios (incluye un Scenario Outline) |
| Informe | [`entregable/informe_hito3.pdf`](entregable/informe_hito3.pdf) |

| Caso | Título | Resultado |
|---|---|---|
| TC-001 | Inicio de sesión exitoso con usuario estándar | PASS |
| TC-002 | Bloqueo de acceso a un usuario deshabilitado | PASS |
| TC-003 | Agregar y eliminar productos del carrito | PASS |
| TC-004 | Ordenar productos por precio de menor a mayor | FAIL → BUG-002 |
| TC-005 | Completar los datos del checkout con información válida | FAIL → BUG-001 |

## Estructura

```
Examen-Hito-3-TQA/
├── README.md
├── docs/
│   ├── casos_caja_negra.md        # 5 casos con diseño y ejecución
│   ├── analisis_caja_blanca.md    # decisiones, criterio, mínimo y casos
│   ├── escenarios_gherkin.md      # escenarios explicados
│   ├── saucedemo.feature          # escenarios en formato Gherkin
│   └── plantillas/                # TC-001 a TC-005 en la plantilla de la materia
├── bugs/
│   ├── bugs_encontrados.md
│   ├── BUG-001.docx               # reportes en la plantilla de bugs
│   └── BUG-002.docx
├── codigo/
│   ├── compra.py                  # función analizada en caja blanca
│   ├── test_compra_3_casos.py     # CB-01 a CB-03
│   └── test_compra_ajuste.py      # CB-04 y CB-05
├── evidencias/
│   ├── capturas/                  # capturas de cada caso de prueba
│   └── cobertura_caja_blanca.txt  # salida de coverage.py
└── entregable/
    └── informe_hito3.pdf
```

## Cómo repetir la medición de cobertura

```bash
cd codigo
pip install pytest coverage
python -m coverage run --branch -m pytest test_compra_3_casos.py
python -m coverage report -m
```
