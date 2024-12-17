# Aplicación de Gestión de Tareas

## Descripción

Esta es una aplicación de gestión de tareas desarrollada en Python utilizando Streamlit para la interfaz de usuario y SQLAlchemy para la persistencia de datos. Permite a los usuarios gestionar sus tareas diarias de manera eficiente y sencilla.

## Características

- Agregar nuevas tareas con título y descripción
- Listar todas las tareas con su estado (pendiente o completada)
- Marcar tareas como completadas
- Eliminar tareas completadas
- Exportar e importar tareas en formato JSON
- Interfaz gráfica intuitiva con Streamlit

## Requisitos

- Python 3.7+
- Streamlit
- SQLAlchemy

## Instalación y Configuración

1. Asegúrate de tener Python 3.7 o superior instalado. Puedes verificar tu versión de Python con:
   ```bash
   python --version
   ```

2. Clona este repositorio:
   ```bash
   git clone https://github.com/sepulveda272/Proyecto_IA.git
   ```

3. (Opcional pero recomendado) Crea un entorno virtual:
   ```bash
   python -m venv env
   ```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\\env\\Scripts\\activate
     ```
    
5. Instala las dependencias:
   ```bash
   pip install streamlit sqlalchemy
   ````

## Ejecución de la Aplicación

1. Asegúrate de estar en el directorio del proyecto y que tu entorno virtual esté activado (si lo estás usando).

2. Ejecuta la aplicación con Streamlit dentro de la carpeta Frontend:
   ```bash
   streamlit run app.py
   ```

3. Streamlit abrirá automáticamente una nueva pestaña en tu navegador predeterminado. Si no se abre automáticamente, puedes acceder a la aplicación navegando a la URL que aparece en la terminal (generalmente `http://localhost:8501`).

4. Utiliza el menú lateral para navegar por las diferentes funcionalidades de la aplicación:
   - Inicio: Página de bienvenida
   - Ver Tareas: Lista todas las tareas existentes
   - Agregar Tarea: Permite crear una nueva tarea
   - Completar Tarea: Marca una tarea como completada
   - Eliminar Tarea: Elimina una tarea completada
   - Importar/Exportar: Permite guardar las tareas en un archivo JSON o cargarlas desde uno

5. Para detener la aplicación, presiona `Ctrl+C` en la terminal donde la ejecutaste.

## Video del trabajo

1. Link: https://youtu.be/YOrLfZKTiME