# prueba de IA CHATBOT con datos personalizados

## 0. Requerimientos
- python 3.x
- pip
- virtualenv
- un api key de openai
  - https://beta.openai.com/account/api-keys 

## 1. Instalacion
- crea una carpeta para el proyecto
- instala un entorno virtual (virtualenv venv)
- activa el entorno virtual (.\venv\Scripts\activate para windows, source venv/bin/activate para linux)
- instala las dependencias (pip install -r requirements.txt)

## 2. Configuracion
- crea un archivo .env en la raiz del proyecto
- en el archivo .env OPENAI_API_KEY= "tu api key de openai"

## 3. Ejecucion
- para cargar tus datos copia la informacion en formato plano (txt,csv,etc) en la carpeta data
- llama a la funcion training_with_data() (descomenta la linea 54)
- ejecuta el script (esto creara un archivo index.json en la carpeta index)
- llama a la funcion ask_ai() (descomenta la linea 55 y comenta la linea 54)
- puedes hacer preguntas sobre los datos cargados

## 4. Referencias
- https://youtu.be/vDZAZuaXf48
- https://beebom.com/how-train-ai-chatbot-custom-knowledge-base-chatgpt-api/

## 5. Notas
- el ejemplo tiene los datos cargados del cuento el fantasma de canterville
- por ahora no funciona con archivos muy extensos (mas de 1500 lineas)