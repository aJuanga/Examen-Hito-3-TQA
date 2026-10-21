# Análisis de caja blanca – `validar_compra`

Código analizado (copia en [`codigo/compra.py`](../codigo/compra.py)):

```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:                          # D1
        return "Compra no permitida: edad"

    if not cuenta_activa:                  # D2
        return "Compra no permitida: cuenta"

    if saldo >= monto and monto > 0:       # D3
        return "Compra aprobada"

    return "Compra rechazada"
```

## 1. Decisiones y condiciones simples

| Decisión | Expresión | Condiciones simples | Si es verdadera | Si es falsa |
|---|---|---|---|---|
| D1 | `edad < 18` | C1: `edad < 18` | "Compra no permitida: edad" | pasa a D2 |
| D2 | `not cuenta_activa` | C2: `cuenta_activa` es falso | "Compra no permitida: cuenta" | pasa a D3 |
| D3 | `saldo >= monto and monto > 0` | C3: `saldo >= monto` · C4: `monto > 0` | "Compra aprobada" | "Compra rechazada" |

El código tiene **3 decisiones**, **4 condiciones simples** y **4 sentencias `return`**, que son las 4 salidas posibles de la función.

## 2. Criterio utilizado

Se eligió la **cobertura de decisiones**: cada decisión debe tomar al menos una vez el valor verdadero y una vez el falso. Este criterio exige más que la cobertura de sentencias y es el que se trabajó en clase como base.

## 3. Mínimo de casos para el criterio

Las tres decisiones están en secuencia y las dos primeras terminan la función cuando son verdaderas. Por eso cada resultado verdadero necesita un caso propio:

- D1 verdadera → un caso que termina en la primera salida.
- D2 verdadera → un caso que pasa D1 (falsa) y termina en la segunda salida.
- D3 verdadera → un caso que pasa D1 y D2 (falsas) y llega a "Compra aprobada".
- D3 falsa → otro caso que pasa D1 y D2 y llega a "Compra rechazada".

Los resultados falsos de D1 y D2 quedan cubiertos por los casos que llegan a D2 y D3. En total, **el mínimo es 4 casos**. Coincide con la complejidad ciclomática del código: V(G) = decisiones + 1 = 3 + 1 = 4.

Como referencia, la cobertura de sentencias también exige 4 casos (uno por cada `return`). La cobertura de condiciones exige 5, porque Python evalúa `and` en cortocircuito: para que C4 sea falsa, C3 tiene que ser verdadera, así que hacen falta dos casos distintos que hagan falsa a D3.

## 4. Casos diseñados

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Qué cubre |
|---|---|---|---|---|---|---|
| CB-01 | 16 | True | 500 | 200 | Compra no permitida: edad | D1 verdadera (C1 = V) |
| CB-02 | 25 | False | 500 | 200 | Compra no permitida: cuenta | D1 falsa, D2 verdadera (C2 = V) |
| CB-03 | 30 | True | 500 | 200 | Compra aprobada | D1 falsa, D2 falsa, D3 verdadera (C3 = V, C4 = V) |

Resultado de cobertura de decisiones con los 3 casos: D1 (V y F), D2 (V y F) y D3 (solo V). Se cubren **5 de 6 resultados (83 %)**. La sentencia `return "Compra rechazada"` no se ejecuta.

## 5. Ajuste necesario

Los 3 casos **no alcanzan** la cobertura de decisiones, porque D3 nunca es falsa. El ajuste es agregar un cuarto caso:

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Qué cubre |
|---|---|---|---|---|---|---|
| CB-04 | 30 | True | 100 | 300 | Compra rechazada | D3 falsa (C3 = F) |

Con CB-01 a CB-04 se cubren los 6 resultados de decisión (100 %) y las 4 sentencias.

Si además se busca cobertura de condiciones, hace falta un quinto caso:

| ID | edad | cuenta_activa | saldo | monto | Resultado esperado | Qué cubre |
|---|---|---|---|---|---|---|
| CB-05 | 30 | True | 500 | 0 | Compra rechazada | C3 = V, C4 = F |

## 6. Comprobación con coverage.py

Los casos se automatizaron con pytest y se midió la cobertura de ramas con `coverage run --branch`. El detalle está en [`evidencias/cobertura_caja_blanca.txt`](../evidencias/cobertura_caja_blanca.txt).

| Conjunto de casos | Sentencias sin ejecutar | Ramas parciales | Cobertura |
|---|---|---|---|
| CB-01 a CB-03 | 1 (línea 11) | 1 | 86 % |
| CB-01 a CB-04 | 0 | 0 | 100 % |
| CB-01 a CB-05 | 0 | 0 | 100 % |

La medición confirma el análisis: la rama que falta con los 3 casos es justamente la salida "Compra rechazada".

**Observación:** con `monto = 0` o un monto negativo la función devuelve "Compra rechazada", el mismo mensaje que con saldo insuficiente. Se recomienda devolver un mensaje distinto para montos inválidos, así el usuario entiende por qué se rechazó la compra.
