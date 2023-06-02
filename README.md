# Automatización de carga de datos desde Excel a Microsoft Forms

Este proyecto tiene como objetivo automatizar la carga de datos desde un archivo Excel a un formulario en Microsoft Forms utilizando Python y Selenium.

## Descripción

El objetivo de este proyecto es desarrollar una solución automatizada para la carga de datos desde un archivo Excel a un formulario en Microsoft Forms. Se utilizará Python en combinación con la biblioteca Selenium para controlar el navegador web y realizar las acciones necesarias.

El flujo de trabajo de la automatización es el siguiente:

1. El usuario proporciona un archivo Excel que contiene los datos a cargar en el formulario de Microsoft Forms.

2. El script de automatización lee el archivo Excel utilizando la biblioteca openpyxl y almacena los datos en una estructura adecuada.

3. Utilizando Selenium, el script abre el navegador web (Chrome) y accede a la página de Microsoft Forms.

4. Usando los métodos proporcionados por Selenium, el script localiza los campos del formulario en la página y los completa con los datos del archivo Excel.

5. Después de completar todos los campos del formulario, el script hace clic en el botón de envío para enviar los datos.

6. Opcionalmente, se pueden capturar los resultados o registros y guardarlos en un archivo de texto para su posterior análisis.

## Estructura del proyecto

El proyecto sigue la siguiente estructura de directorios y archivos:


- `chromedriver/`: Carpeta que almacena el controlador de Chrome (ChromeDriver).

- `archivos/`: Carpeta para almacenar los archivos relacionados al proyecto, como el archivo Excel con los datos y el archivo para guardar resultados o registros.

- `scripts/`: Carpeta para almacenar los scripts de Python, con el script principal de automatización llamado `automatizar_formulario.py`.

- `README.md`: Este archivo que estás leyendo, proporciona información detallada sobre el proyecto, instrucciones de instalación y configuración.

## Instrucciones de uso

1. Clona o descarga este repositorio en tu máquina local.

2. Asegúrate de tener Python instalado en tu sistema.

3. Instala las dependencias ejecutando el siguiente comando en tu terminal o línea de comandos:

pip install selenium openpyxl


4. Descarga el controlador de Chrome (ChromeDriver) compatible con tu versión de Chrome y guárdalo en la carpeta `chromedriver/`.

5. Coloca el archivo Excel con los datos a cargar en la carpeta `archivos/`.

6. Abre el archivo `automatizar_formulario.py` en un editor de texto y modifica cualquier configuración necesaria (URL del formulario, selectores de elementos, etc.).

7. Ejecuta el script `automatizar_formulario.py` para iniciar la automatización.

## Notas adicionales

- Asegúrate de cumplir con los términos de servicio de Microsoft Forms y seguir las buenas prácticas de automatización.

- Puedes personalizar y extender la automatización según tus necesidades específicas.

- Si encuentras algún problema o tienes alguna pregunta,
