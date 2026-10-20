# Reconocimiento facial con OpenCV

Conjunto de tres scripts en Python que capturan rostros desde la cámara web, entrenan un modelo LBPH y reconocen personas en tiempo real.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-contrib-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Estado](https://img.shields.io/badge/estado-ejercicio%20académico-lightgrey?style=flat)
![Licencia](https://img.shields.io/badge/licencia-MIT-blue?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/Face-Recognition-Script?style=flat)

<!-- Demo: agrega una captura o GIF en docs/demo.gif y descomenta la línea siguiente -->
<!-- <p align="center"><img src="docs/demo.gif" alt="Demostración del reconocimiento facial" width="800"></p> -->

## Tabla de contenidos

- [Descripción](#descripción)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Autor](#autor)

## Descripción

Proyecto de aprendizaje que separa el flujo de reconocimiento facial en tres procesos independientes (captura, entrenamiento y reconocimiento) para entender cómo se relaciona cada etapa. Está en estado de desarrollo temprano (pre-alpha).

## Estado del proyecto

**Ejercicio académico.** Proyecto de aprendizaje en estado pre-alpha, sin planes de ampliación.

## Características

- Captura hasta 1000 imágenes del rostro por persona (150x150 px) con detección Haar Cascade.
- Entrena un reconocedor `LBPHFaceRecognizer` y guarda el modelo en `FacesModel.xml`.
- Reconoce rostros en tiempo real y muestra el nombre o "Desconocido" sobre el video.
- Se cierra con la tecla `q`.

## Tecnologías

- Python 3.11
- OpenCV (`opencv-contrib-python`)
- Imutils

## Requisitos

- Python 3 y una cámara web.
- Dependencias de `requirements.txt`.

## Instalación

```bash
git clone https://github.com/ViceAguilera/Face-Recognition-Script.git
cd Face-Recognition-Script
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

> **Importante:** los tres scripts tienen la variable `dataPath` con una ruta absoluta del equipo original (`/home/sirius/PycharmProjects/FaceRecognition/Data`). Edítala para que apunte a la carpeta `Data/` de tu copia del proyecto antes de ejecutar.

## Uso

1. Capturar rostros (pide el nombre de la persona y crea `Data/<nombre>/`):
   ```bash
   python ImageCapture.py
   ```
2. Entrenar el modelo (genera `FacesModel.xml`):
   ```bash
   python TrainModel.py
   ```
3. Reconocer en tiempo real:
   ```bash
   python FaceRecognition.py
   ```

## Estructura del proyecto

```
ImageCapture.py                      # Captura de rostros desde la cámara
TrainModel.py                        # Entrenamiento del modelo LBPH
FaceRecognition.py                   # Reconocimiento en tiempo real
haarcascade_frontalface_default.xml  # Clasificador Haar Cascade
Data/                                # Imágenes de rostros por persona
requirements.txt
```

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).

## Autor

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)
