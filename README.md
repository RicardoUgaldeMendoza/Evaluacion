# Proyecto Paquexpress - Sistema de Gestión de Entregas

Este proyecto implementa un sistema modular de gestión de entregas compuesto por una API de backend desarrollada con **FastAPI** y una aplicación móvil frontend desarrollada con **Flutter**.

La aplicación permite a los agentes de entrega autenticarse de forma segura, visualizar sus paquetes asignados y registrar la entrega final con evidencia fotográfica y coordenadas GPS.

## Estructura del Proyecto

El repositorio está organizado en dos directorios principales:
* **`paquexpress_api/`**: Contiene la API REST del backend (FastAPI, SQLAlchemy, MySQL).
* **`evaluacion_u3/`**: Contiene la aplicación móvil (Frontend Flutter).

## 1. Configuración del Backend (FastAPI + MySQL)

El backend utiliza un patrón de diseño modular para los *routers* y se conecta a una base de datos MySQL.

# 1.1. Dependencias de Python

Se requiere Python 3.10 o superior.

# Activar entorno virtual
.\venv\Scripts\activate

# Instalar librerías
pip install fastapi uvicorn[standard] sqlalchemy pymysql python-multipart

# 1.2. Configuración de Base de Datos
Crear una base de datos MySQL llamada paquexpress.
Verificar y actualizar las credenciales de conexión en paquexpress_api/bd.py.
El sistema crea las tablas (agentes y paquetes) automáticamente.
Insertar el agente de prueba (ricardo01) en la tabla agentes. La contraseña debe ser el hash MD5 de '1234' (81dc9bdb52d04dc20036dbd8313ed055).

# 1.3. Ejecución del Servidor
Navegar al directorio de la API y ejecutar:
uvicorn main:app --reload

## 2. Configuración del Frontend (Flutter)
La aplicación debe configurarse para apuntar al servidor local de FastAPI.

# 2.1. Dependencias de Flutter
Navegar al directorio raíz de Flutter e instalar dependencias:
flutter pub get

# 2.3. Ejecución de la Aplicación
Asegurarse de que el servidor FastAPI esté activo y ejecutar la aplicación:
flutter run

# 2.4. Credenciales de Prueba
Utilizar las siguientes credenciales para probar la integración:
Usuario: ricardo01
Contraseña: 1234