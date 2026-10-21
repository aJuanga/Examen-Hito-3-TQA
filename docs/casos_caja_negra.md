# Casos de prueba de caja negra – SauceDemo

Aplicación probada: https://www.saucedemo.com/ · Ejecutados por Juan Gabriel Ibañez Copatiti el 20/10/2026 · Ambiente: QA (sitio de demostración) · Navegador: Chromium 141 · resolución 1280x720.

Cada caso tiene su plantilla completa de diseño y ejecución en [`docs/plantillas/`](plantillas/).

## Resumen

| ID | Título | Módulo | Tipo | Prioridad | Resultado | Bug |
|---|---|---|---|---|---|---|
| TC-001 | Inicio de sesión exitoso con usuario estándar | Inicio de sesión | Funcional | Alta | **PASS** | N/A |
| TC-002 | Bloqueo de acceso a un usuario deshabilitado | Inicio de sesión | Negativa | Alta | **PASS** | N/A |
| TC-003 | Agregar y eliminar productos del carrito | Carrito de compras | Funcional | Media | **PASS** | N/A |
| TC-004 | Ordenar productos por precio de menor a mayor | Catálogo – ordenamiento | Funcional | Media | **FAIL** | BUG-002 |
| TC-005 | Completar los datos del checkout con información válida | Checkout | Funcional | Alta | **FAIL** | BUG-001 |

Resultado: 3 casos **PASS** y 2 casos **FAIL**. Los dos fallos están documentados como BUG-001 y BUG-002.

## TC-001 · Inicio de sesión exitoso con usuario estándar

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar que un usuario registrado y habilitado accede al catálogo de productos al ingresar credenciales válidas. |
| Módulo | Inicio de sesión |
| Tipo / Prioridad | Funcional / Alta |
| Precondiciones | Navegador abierto en la página de login de SauceDemo, sin sesión iniciada. Usuario: standard_user (usuario de demostración habilitado). |
| Datos de prueba | Usuario / contraseña: standard_user / secret_sauce |

**Pasos y resultado esperado**

| # | Paso | Dato | Resultado esperado |
|---|---|---|---|
| 1 | Abrir la URL de la aplicación | https://www.saucedemo.com/ | Se muestra el formulario de login con los campos Username y Password. |
| 2 | Ingresar el usuario en el campo Username | standard_user | El campo muestra el texto ingresado. |
| 3 | Ingresar la contraseña en el campo Password | secret_sauce | El campo muestra caracteres ocultos. |
| 4 | Presionar el botón Login | — | El sistema redirige a /inventory.html con el título Products. |
| 5 | Verificar el catálogo | — | Se listan los 6 productos con nombre, precio y botón Add to cart. |

**Criterio de éxito:** El usuario accede a /inventory.html y visualiza el catálogo completo sin mensajes de error.

**Ejecución**

- Resultado: **PASS**
- Resultado obtenido: Tras presionar Login, la aplicación redirigió a https://www.saucedemo.com/inventory.html, mostró el título Products y listó los 6 productos con sus precios.
- Comparación: Coincide con el resultado esperado.
- Bug asociado: N/A
- Evidencia: [TC-001_01_credenciales.png](../evidencias/capturas/TC-001_01_credenciales.png), [TC-001_02_catalogo.png](../evidencias/capturas/TC-001_02_catalogo.png)
- Comentario: Recomendación: agregar a futuro un caso de login con contraseña incorrecta para el mismo usuario y un caso de cierre de sesión, de modo que el módulo quede cubierto en sus flujos principales.

## TC-002 · Bloqueo de acceso a un usuario deshabilitado

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar que un usuario bloqueado no puede ingresar al sistema y que se le informa el motivo. |
| Módulo | Inicio de sesión |
| Tipo / Prioridad | Negativa / Alta |
| Precondiciones | Navegador abierto en la página de login, sin sesión iniciada. Usuario: locked_out_user (usuario de demostración bloqueado). |
| Datos de prueba | Usuario / contraseña: locked_out_user / secret_sauce |

**Pasos y resultado esperado**

| # | Paso | Dato | Resultado esperado |
|---|---|---|---|
| 1 | Abrir la URL de la aplicación | https://www.saucedemo.com/ | Se muestra el formulario de login. |
| 2 | Ingresar el usuario bloqueado | locked_out_user | El campo muestra el texto ingresado. |
| 3 | Ingresar la contraseña | secret_sauce | El campo muestra caracteres ocultos. |
| 4 | Presionar el botón Login | — | El sistema no permite el acceso y permanece en la página de login. |
| 5 | Verificar el mensaje | — | Se muestra: "Epic sadface: Sorry, this user has been locked out." |

**Criterio de éxito:** El acceso se rechaza y aparece un mensaje claro que indica que el usuario está bloqueado.

**Ejecución**

- Resultado: **PASS**
- Resultado obtenido: La aplicación se mantuvo en la página de login, marcó los campos en rojo y mostró el mensaje "Epic sadface: Sorry, this user has been locked out."
- Comparación: Coincide con el resultado esperado.
- Bug asociado: N/A
- Evidencia: [TC-002_01_usuario_bloqueado.png](../evidencias/capturas/TC-002_01_usuario_bloqueado.png)
- Comentario: Recomendación: el mensaje cumple su función, pero conviene que indique al usuario qué hacer a continuación (por ejemplo, contactar al administrador) y que se ofrezca en el idioma del usuario.

## TC-003 · Agregar y eliminar productos del carrito

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar que el carrito refleja correctamente los productos agregados y eliminados, y que el contador del ícono se actualiza. |
| Módulo | Carrito de compras |
| Tipo / Prioridad | Funcional / Media |
| Precondiciones | Sesión iniciada con standard_user en el catálogo, con el carrito vacío. Usuario: standard_user. |
| Datos de prueba | Productos: Sauce Labs Backpack ($29.99) y Sauce Labs Bike Light ($9.99) |

**Pasos y resultado esperado**

| # | Paso | Dato | Resultado esperado |
|---|---|---|---|
| 1 | Presionar Add to cart en Sauce Labs Backpack | Backpack | El botón cambia a Remove y el contador muestra 1. |
| 2 | Presionar Add to cart en Sauce Labs Bike Light | Bike Light | El contador del carrito muestra 2. |
| 3 | Abrir el carrito desde el ícono superior | — | Se listan ambos productos con su precio. |
| 4 | Presionar Remove en Sauce Labs Backpack | Backpack | El producto desaparece del carrito. |
| 5 | Verificar el contador del carrito | — | El contador muestra 1 y solo queda Sauce Labs Bike Light. |

**Criterio de éxito:** El carrito y su contador reflejan en todo momento los productos agregados y eliminados.

**Ejecución**

- Resultado: **PASS**
- Resultado obtenido: El contador mostró 2 al agregar ambos productos. En el carrito se listaron Sauce Labs Backpack y Sauce Labs Bike Light. Al eliminar el Backpack, solo quedó Bike Light y el contador bajó a 1.
- Comparación: Coincide con el resultado esperado.
- Bug asociado: N/A
- Evidencia: [TC-003_01_dos_productos.png](../evidencias/capturas/TC-003_01_dos_productos.png), [TC-003_02_carrito.png](../evidencias/capturas/TC-003_02_carrito.png), [TC-003_03_producto_eliminado.png](../evidencias/capturas/TC-003_03_producto_eliminado.png)
- Comentario: Recomendación: complementar con un caso que verifique que el carrito se conserva al cerrar y volver a iniciar sesión, porque es un punto donde suelen aparecer defectos de persistencia.

## TC-004 · Ordenar productos por precio de menor a mayor

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar que el filtro Price (low to high) reordena el catálogo de forma ascendente según el precio. |
| Módulo | Catálogo – ordenamiento |
| Tipo / Prioridad | Funcional / Media |
| Precondiciones | Sesión iniciada con problem_user en el catálogo, con el orden por defecto Name (A to Z). Usuario: problem_user (usuario de demostración). |
| Datos de prueba | Opción de ordenamiento: Price (low to high) |

**Pasos y resultado esperado**

| # | Paso | Dato | Resultado esperado |
|---|---|---|---|
| 1 | Iniciar sesión con problem_user | problem_user / secret_sauce | Se muestra el catálogo ordenado por nombre. |
| 2 | Anotar el orden inicial de precios | — | Orden inicial: $29.99, $9.99, $15.99, $49.99, $7.99, $15.99. |
| 3 | Abrir el filtro de ordenamiento | — | Se despliegan las 4 opciones de orden. |
| 4 | Seleccionar Price (low to high) | Price (low to high) | El filtro muestra la opción elegida. |
| 5 | Verificar el orden de los productos | — | Los precios quedan en orden ascendente, de $7.99 a $49.99. |

**Criterio de éxito:** Los productos se muestran ordenados de menor a mayor precio y el filtro conserva la opción seleccionada.

**Ejecución**

- Resultado: **FAIL**
- Resultado obtenido: Al seleccionar Price (low to high), el catálogo no cambió: los precios siguieron en el orden $29.99, $9.99, $15.99, $49.99, $7.99, $15.99 y el filtro volvió a mostrar Name (A to Z).
- Comparación: No coincide. El orden no se aplica y la selección del filtro se revierte. Con standard_user el mismo filtro sí ordena correctamente, por lo que el defecto se presenta con este usuario.
- Bug asociado: BUG-002
- Evidencia: [TC-004_01_orden_no_aplicado.png](../evidencias/capturas/TC-004_01_orden_no_aplicado.png), [CTRL_orden_standard_user_ok.png](../evidencias/capturas/CTRL_orden_standard_user_ok.png)
- Comentario: Recomendación: corregir el defecto y repetir el caso con las cuatro opciones del filtro (A-Z, Z-A, precio ascendente y descendente) como prueba de regresión. También se observó que todos los productos muestran la misma imagen, lo que conviene revisar por separado.

## TC-005 · Completar los datos del checkout con información válida

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar que el formulario Checkout: Your Information valida los campos obligatorios y permite continuar al ingresar nombre, apellido y código postal válidos. |
| Módulo | Checkout |
| Tipo / Prioridad | Funcional / Alta |
| Precondiciones | Sesión iniciada con problem_user y un producto en el carrito (Sauce Labs Backpack). Usuario: problem_user (usuario de demostración). |
| Datos de prueba | Nombre / Apellido / Código postal: Juan / Ibanez / 0201 |

**Pasos y resultado esperado**

| # | Paso | Dato | Resultado esperado |
|---|---|---|---|
| 1 | Abrir el carrito y presionar Checkout | Sauce Labs Backpack | Se muestra el formulario Checkout: Your Information. |
| 2 | Presionar Continue con los campos vacíos | — | Aparece el mensaje Error: First Name is required. |
| 3 | Ingresar el nombre en First Name | Juan | El campo First Name muestra Juan. |
| 4 | Ingresar el apellido en Last Name | Ibanez | El campo Last Name muestra Ibanez. |
| 5 | Ingresar el código postal | 0201 | El campo Zip/Postal Code muestra 0201. |
| 6 | Presionar Continue | — | El sistema avanza a Checkout: Overview con el resumen de la compra. |

**Criterio de éxito:** Con los tres campos completos, el sistema avanza al resumen de la compra sin mostrar errores.

**Ejecución**

- Resultado: **FAIL**
- Resultado obtenido: La validación de campos vacíos funcionó. Sin embargo, al escribir el apellido en Last Name, el texto apareció en First Name (reemplazando Juan por Ibanez) y Last Name quedó vacío. Al presionar Continue se mostró Error: Last Name is required y no fue posible avanzar.
- Comparación: No coincide. El campo Last Name no recibe el texto ingresado y la compra queda bloqueada en el primer paso del checkout.
- Bug asociado: BUG-001
- Evidencia: [TC-005_01_campos_obligatorios.png](../evidencias/capturas/TC-005_01_campos_obligatorios.png), [TC-005_02_apellido_en_nombre.png](../evidencias/capturas/TC-005_02_apellido_en_nombre.png), [TC-005_03_error_apellido.png](../evidencias/capturas/TC-005_03_error_apellido.png), [CTRL_checkout_standard_user_ok.png](../evidencias/capturas/CTRL_checkout_standard_user_ok.png)
- Comentario: Recomendación: es el defecto más crítico encontrado porque impide finalizar una compra. Una vez corregido, se sugiere ejecutar de nuevo el flujo completo hasta la pantalla Thank you for your order! y agregar validaciones de longitud y caracteres especiales en los tres campos.
