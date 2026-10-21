# Escenarios Gherkin – SauceDemo

Los escenarios describen en lenguaje de negocio los flujos probados en los casos de caja negra. El archivo con la sintaxis lista para usar es [`saucedemo.feature`](saucedemo.feature).

```gherkin
Feature: Inicio de sesión en SauceDemo
  Como cliente de Swag Labs
  quiero iniciar sesión con mi usuario
  para acceder al catálogo de productos

  Background:
    Given que estoy en la página de login de "https://www.saucedemo.com/"

  Scenario: Acceso exitoso con un usuario habilitado
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And presiono el botón "Login"
    Then debería ver la página "Products"
    And el catálogo debería mostrar 6 productos

  Scenario: Acceso denegado a un usuario bloqueado
    When ingreso el usuario "locked_out_user" y la contraseña "secret_sauce"
    And presiono el botón "Login"
    Then debería permanecer en la página de login
    And debería ver el mensaje "Epic sadface: Sorry, this user has been locked out."


Feature: Datos del comprador en el checkout
  Como cliente con productos en el carrito
  quiero ingresar mis datos de envío
  para continuar con la compra

  Background:
    Given que inicié sesión como "standard_user"
    And tengo el producto "Sauce Labs Backpack" en el carrito
    And estoy en la página "Checkout: Your Information"

  Scenario: Continuar con todos los datos completos
    When ingreso "Juan" en "First Name"
    And ingreso "Ibanez" en "Last Name"
    And ingreso "0201" en "Zip/Postal Code"
    And presiono el botón "Continue"
    Then debería ver la página "Checkout: Overview"

  Scenario Outline: No continuar si falta un dato obligatorio
    When ingreso "<nombre>" en "First Name"
    And ingreso "<apellido>" en "Last Name"
    And ingreso "<postal>" en "Zip/Postal Code"
    And presiono el botón "Continue"
    Then debería ver el mensaje "<mensaje>"
    But no debería avanzar a "Checkout: Overview"

    Examples:
      | nombre | apellido | postal | mensaje                            |
      |        | Ibanez   | 0201   | Error: First Name is required      |
      | Juan   |          | 0201   | Error: Last Name is required       |
      | Juan   | Ibanez   |        | Error: Postal Code is required     |
```

Cada escenario tiene un paso **Given** que deja el sistema en un estado conocido, un **When** con una sola acción del usuario y un **Then** que se puede verificar en pantalla. El escenario exitoso del checkout corresponde al flujo que falla con `problem_user` (BUG-001).
