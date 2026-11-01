# Gestión de Base de Datos (database.md)

## Objetivo
Configuración y reglas de seguridad para la interacción con la base de datos vía MCP.

## Credenciales
* db_user: postgres18
* db_name: odoo_dev

## Reglas de Interacción
* **Integridad:** Respetar la integridad referencial de Odoo (tablas ir_model_data, restricciones res_company).
* **Seguridad:** No ejecutar cambios masivos (UPDATE, DELETE) sin antes haber realizado una consulta de validación (SELECT sobre los registros afectados).
* **MCP:** Se utiliza el MCP postgresql-18-shared para ejecutar consultas SQL necesarias para auditoría o debugging.
