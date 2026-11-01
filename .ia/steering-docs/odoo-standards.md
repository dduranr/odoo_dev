# Estándares de Código Odoo 20 / Python (odoo-standards.md)

## Objetivo
Definir las normas de desarrollo para asegurar la consistencia y estabilidad del sistema.

## Documentación y Referencias
* Ante dudas sobre infraestructura y código de Odoo 20, consultar siempre: https://www.odoo.com/documentation/20.0/

## Estructura de Módulos
Cada módulo en custom-addons debe seguir la estructura estándar de Odoo:
* __manifest__.py: Declaración del módulo.
* models/: Definición de clases heredadas o nuevas (models.Model).
* views/: Vistas XML y templates.
* security/: ir.model.access.csv y reglas de registro.

## Estándares de Codificación
* **Estilo de Código:** Seguir estrictamente [PEP 8](https://peps.python.org/pep-0008/).
* **Convenciones de Nombres:**
    * **snake_case:** Obligatorio para funciones, variables, métodos y nombres de módulos (ej. mi_variable, calcular_total)
    * **snake_case:** Obligatorio para funciones, variamente para nombres de clases (ej. ClassMiClase).
* **Idioma:**
    * **Código:** Nombres de variables, funciones y clases deben estar en inglés.
    * **Comentarios y Docstrings:** Deben redactarse siempre en español.
* **Docstrings:**
    * Obligatorios en cada nueva función, método o clase.
    * Seguir el estándar [PEP 257](https://peps.python.org/pep-0257/).
    * Incluir descripción del propósito, parámetros (Args) y retorno (Returns).

## Seguridad
* **Prioridad:** Usar siempre el ORM de Odoo para operaciones CRUD.
* **Prohibido:** Ejecutar SQL directo (cr.execute) excepto cuando sea estrictamente necesario y justificado.
* **sudo():** Usar con precaución extrema, limitando el alcance al bloque necesario.
* **Acceso:** Todo nuevo modelo debe incluir su respectivo archivo ir.model.access.csv con permisos definidos.
