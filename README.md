# Duran Sales Commission (Odoo 20)

Módulo personalizado desarrollado para **Odoo 20** que implementa un sistema completo y modular de gestión de comisiones de ventas y reglas de excepción por producto.

---

## 📋 Características Principales

1. **Configuración de Comisión General por Defecto:**
   - Permite definir un porcentaje de comisión general aplicable a todas las ventas de la compañía (por defecto configurado al **5%**).
   - Totalmente administrable desde la interfaz visual (*Ventas > Configuración > Ajustes*).

2. **Excepciones de Comisión por Producto (CRUD):**
   - Tabla relacional dedicada (`duran.commission.rule`) accesible desde *Ventas > Configuración > Reglas de Comisión por Producto*.
   - Permite al administrador asignar porcentajes de comisión personalizados y superiores para incentivar la venta de productos específicos o de gama alta.
   - Validación integrada mediante restricciones de base de datos (`UNIQUE` por producto y compañía) y validaciones de rango en Python (`0%` a `100%`).

3. **Cálculo Automático en Órdenes de Venta:**
   - Extensión inteligente de `sale.order` y `sale.order.line`.
   - Evalúa de forma reactiva si el producto vendido cuenta con una regla de excepción activa; de lo contrario, aplica la regla general de la compañía.
   - **Regla de Negocio:** El monto de comisión efectivo se calcula y computa automáticamente solo cuando la orden de venta se confirma o factura (`state in ['sale', 'done']`). En estados de cotización/borrador, el monto permanece en `0.00`.
   - Cálculo de la tasa de comisión ponderada y monto total acumulado de comisión por orden.

4. **Integración en la Interfaz Gráfica (XML Views):**
   - **Líneas de Pedido:** Columnas opcionales para visualizar el porcentaje y monto de comisión por cada producto.
   - **Resumen de Comisiones:** Sección dedicada en el formulario de ventas (*Resumen de Comisiones de Venta*) que muestra el vendedor asignado, la comisión ponderada y el total de la comisión.

---

## 📦 Dependencias

Este módulo requiere que los siguientes módulos estándar de Odoo 20 estén instalados:
* `base` (Sistema base de Odoo y gestión de compañías)
* `sale_management` (Gestión completa de ventas, cotizaciones y órdenes de venta)

---

## 🛠️ Estructura del Módulo

```
custom-addons/duran_sales_commission/
├── __init__.py                         # Inicializador principal del paquete Python
├── __manifest__.py                     # Manifiesto y metadatos del módulo
├── security/
│   └── ir.model.access.xml             # Control de acceso y permisos (ir.access) para roles de venta
├── models/
│   ├── __init__.py                     # Inicializador de modelos
│   ├── commission_rule.py              # Modelo CRUD de reglas excepcionales por producto
│   ├── res_company.py                  # Extensión de compañía (porcentaje general por defecto)
│   ├── res_config_settings.py          # Extensión de ajustes de ventas
│   └── sale_order.py                   # Lógica computada para líneas y órdenes de venta
└── views/
    ├── commission_rule_views.xml       # Vistas Form, List, Search y menú de reglas de comisión
    ├── res_config_settings_views.xml   # Inyección del ajuste general en la pantalla de Ventas
    └── sale_order_views.xml            # Herencia y campos de comisión en el formulario de ventas
---

## 🚀 Instalación y Despliegue en Entorno Docker

Este módulo está diseñado para ejecutarse en entornos contenedorizados con **Docker**. Asume la siguiente arquitectura:
* **Odoo** corre dentro de un contenedor dedicado (ej. `odoo_dev_web`) con el directorio de addons personalizado montado como volumen (`/mnt/extra-addons`).
* **PostgreSQL** corre en su propio contenedor (ej. `shared_postgres_18`).
* Ambos servicios se comunican a través de una red Docker dedicada (en este entorno denominada `red-postgres-18`).

### Pasos de Instalación:

1. **Ubicación:**
   Coloque la carpeta del módulo `duran_sales_commission` dentro del directorio de addons personalizados de su proyecto (montado en los contenedores).

2. **Instalación / Actualización:**
   Ejecute el siguiente comando en el contenedor Docker de Odoo para compilar e instalar el módulo en su base de datos (ej. `odoo_dev`), ajustando el nombre del host, usuario y contraseña de su servicio PostgreSQL:
   ```bash
   docker exec -it odoo_dev_web odoo -i duran_sales_commission -d odoo_dev --stop-after-init --db_host=shared_postgres_18 --db_user=postgres18 --db_password=contraseña --db_port=5432
   ```

3. **Acceso:**
   - Inicie sesión en Odoo (http://localhost:8069/).
   - Active el **Modo Desarrollador** (opcional pero recomendado).
   - Diríjase al módulo **Ventas**.


---

## 📖 Manual de Uso

### 1. Configurar la Comisión General
1. Vaya a **Ventas > Configuración > Ajustes**.
2. En la sección **Product Catalog**, busque el campo **Porcentaje de Comisión General (%)**.
3. Ingrese el porcentaje deseado (ej. `5%`) y guarde los cambios.

### 2. Configurar Reglas de Excepción por Producto
1. Vaya a **Ventas > Configuración > Reglas de Comisión por Producto**.
2. Haga clic en **Nuevo**.
3. Seleccione el **Producto**, asigne el **Porcentaje de Comisión** personalizado (ej. `10%`), seleccione la compañía y guarde.

### 3. Visualizar Comisiones en Órdenes de Venta
1. Vaya a **Ventas > Órdenes > Órdenes**.
2. Abra o cree una cotización y añada productos.
3. En las líneas de la orden, podrá visualizar el porcentaje de comisión aplicado y el monto calculado.
4. Al confirmar la cotización (botón **Confirmar Venta**), el sistema calculará automáticamente el monto efectivo de la comisión y mostrará el **Resumen de Comisiones de Venta** en la parte inferior del formulario (vendedor, comisión ponderada y total de comisión).

---

## 🔒 Seguridad y Permisos

El módulo define controles de acceso estrictos basados en los roles estándar de ventas de Odoo:
* **Vendedores (`sales_team.group_sale_salesman`):** Permisos de lectura (`r`) sobre las reglas de comisión y visualización en órdenes de venta.
* **Gerentes de Ventas (`sales_team.group_sale_manager`):** Permisos completos CRUD (`crud`) para gestionar la configuración y las reglas excepcionales.

---

## ✒️ Autor
* **Duran / Odoo Expert**
* **Versión:** 20.0.1.0.0
* **Licencia:** LGPL-3
