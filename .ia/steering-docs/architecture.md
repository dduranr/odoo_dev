# Arquitectura del Entorno (architecture.md)

## Objetivo
Este documento define la topología física del entorno para evitar que el agente intente acceder a rutas inexistentes o protegidas dentro de los contenedores.

## runtime
* **Entorno:** macOS Tahoe
* **Runtime de contenedores:** Colima

## Distribución de Servicios
1. **PostgreSQL 18:** /Users/duran/Projects/www/shared/postgres-18
2. **Odoo:** /Users/duran/Projects/www/odoo-dev

## Visibilidad del Sistema de Archivos
* La IA solo tiene acceso directo al sistema de archivos del host en la ruta: /Users/duran/Projects/www/odoo-dev/.
* **Nota crítica:** No se debe intentar acceder a rutas internas del contenedor de Odoo (como /var/lib/odoo o /usr/lib/python3/...). Toda interacción con archivos debe realizarse exclusivamente a través de los volúmenes montados en /Users/duran/Projects/www/odoo-dev/custom-addons.
