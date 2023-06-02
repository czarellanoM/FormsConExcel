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

