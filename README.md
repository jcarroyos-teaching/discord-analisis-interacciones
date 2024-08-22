# discord-analisis-interacciones

Este repositorio contiene un conjunto de scripts en Python diseñados para extraer mensajes de un canal de Discord y realizar un análisis de sentimientos sobre dichos mensajes. A continuación, se describen los archivos y su funcionalidad:

## Estructura del Repositorio

- `.env`: Archivo que contiene las variables de entorno necesarias para la ejecución de los scripts, como el token del bot de Discord y el ID del canal.
- `.gitignore`: Archivo que especifica qué archivos y directorios deben ser ignorados por Git.
- `analisis_sentimientos.py`: Script que carga los mensajes extraídos de Discord desde un archivo CSV, realiza un análisis de sentimientos utilizando la librería `TextBlob`, y genera un gráfico de barras con los resultados.
- `discord_extractor.py`: Script que se conecta a un canal de Discord utilizando un bot, extrae los mensajes y reacciones, y guarda esta información en un archivo CSV.
- `discord_messages.csv`: Archivo CSV que contiene los mensajes extraídos del canal de Discord.
- `discord_messages_analizados.csv`: Archivo CSV que contiene los mensajes con el análisis de sentimientos realizado.

## Uso

### Extracción de Mensajes

1. Configura las variables de entorno en el archivo `.env`:

   ```env
   TOKEN=tu_token_de_discord
   CHANNEL_ID=tu_id_de_canal
   ```

2. Ejecuta el script `discord_extractor.py` para extraer los mensajes del canal de Discord y guardarlos en `discord_messages.csv`:

   ```sh
   python discord_extractor.py
   ```

3. Asegurate de incluir el bot en el canal de Discord y darle permisos de lectura de mensajes.

### Análisis de Sentimientos

1. Ejecuta el script `analisis_sentimientos.py` para realizar el análisis de sentimientos sobre los mensajes extraídos y generar un gráfico de barras:
   ```sh
   python analisis_sentimientos.py
   ```

## Dependencias

- `discord.py`: Librería para interactuar con la API de Discord.
- `pandas`: Librería para manipulación y análisis de datos.
- `textblob`: Librería para procesamiento de texto y análisis de sentimientos.
- `plotly`: Librería para la creación de gráficos interactivos.

## Instalación de Dependencias

Puedes instalar las dependencias necesarias utilizando `pip`:

```sh
pip install discord.py pandas textblob plotly
```
