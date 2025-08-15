# Whisper

Este proyecto utiliza [Whisper](https://github.com/openai/whisper) para transcribir audios automáticamente.

## Requisitos

- **Python 3.8+**
- **ffmpeg** instalado en tu sistema ([descargar ffmpeg](https://ffmpeg.org/download.html))
- Entorno virtual recomendado

## Instalación

1. **Instala ffmpeg**

   - Windows: Descarga el ejecutable desde [ffmpeg.org](https://ffmpeg.org/download.html) y agrega la carpeta `bin` al PATH.
   - Linux/Mac:  
     ```sh
     sudo apt install ffmpeg
     # o
     brew install ffmpeg
     ```

2. **Crea y activa un entorno virtual**

   ```sh
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```
