# Flujos de Trabajo (workflows.md)

## Objetivo
Instrucciones operativas para la gestión del entorno y despliegue de cambios.

## Arranque del Entorno
Ejecutar en orden:
1. colima start --cpu 4 memory 4
2. cd /Users/duran/Projects/www/shared/postgres-18 && docker-compose up -d
3. cd /Users/duran/Projects/www/odoo-dev && docker-compose up -d

## Actualización de Módulos
Tras cualquier modificación en custom-addons, actualizar mediante:
* CLI del contenedor (recomendado para desarrollo): docker exec -it <nombre_contenedor_odoo> odoo -u <nombre_modulo> -d <nombre_base_datos> --stop-after-init --db_host=<nombre_host_o_ip_postgres> --db_user=<usuario_postgres> --db_password=<contraseña_postgres> --db_port=<puerto_postgres>
* O vía interfaz web: http://localhost:8069/ (Activando Modo Desarrollador).

## Regla Operativa de Ejecución Autónoma
* **Autonomía en Comandos Docker:** El agente tiene autorización explícita y permanente para ejecutar comandos de contenedores (`docker exec`, `docker restart`, etc.) de forma autónoma e independiente, **sin requerir confirmación ni permiso previo** del usuario cada vez que sea necesario desplegar actualizaciones de módulos, reiniciar servicios o verificar el estado del entorno.

