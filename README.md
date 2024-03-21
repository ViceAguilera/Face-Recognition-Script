# Reconocimiento facial con OpenCV

###### ***🚧 V1.0  Pre-Alpha development.🚧🔨***

_Sistema de reconocimiento facial en tiempo real, con procesos separados para la comprensión de sistemas similares_

## Construido con 🛠️

- [Python v3.11](https://www.python.org/) - Lenguaje de programación
- [OpenCV](https://opencv.org/) - Librería de visión artificial
- [Imutils](https://www.jaided.ai/easyocr/) - Librería simplificada de imagenes

## Comenzando 🚀

### Instalacion  🔧

<details>
   <summary>Linux</summary>

1. Se clona el repositorio de GitHub
    ```bash
    git clone https://github.com/ViceAguilera/face-recognition-script.git
    ```
  
2. Se ingresa a la carpeta del proyecto
    ```bash
    cd face-recognition-script
    ```
  
3. Se crea un entorno virtual
    ```bash
    python3 -m venv venv
    ```
    
4. Se activa el entorno virtual
    ```bash
    source venv/bin/activate
    ```

5. Se instala los requerimientos del proyecto
    ```bash
    pip3 install -r requirements.txt
    ```

6. Descarga el algoritmo de deteccion de rostros [Haar Cascade Face Default](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) y se agrega a la carpeta.

7. Se ejecuta el script para "escanear" la cara
    ```bash
    python3 ImageCapture.py
    ```
    
8. Se ejecuta el script para "entrenar" el modelo
    ```bash
    python3 TrainModel.py
    ```
    
9. Se ejecuta el script para "reconocer" la cara y disfruta
    ```bash
    python3 FaceRecognition.py
    ```
</details>

<details>
  <summary>Windows</summary>

1. Se clona el repositorio de GitHub
    ```bash
    git clone https://github.com/ViceAguilera/face-recognition-script.git
    ```
  
2. Se ingresa a la carpeta del proyecto
    ```bash
    cd face-recognition-script
    ```
  
3. Se crea un entorno virtual
    ```bash
    python -m venv venv
    ```
    
4. Se activa el entorno virtual
    ```bash
    source venv/bin/activate
    ```

5. Se instala los requerimientos del proyecto
    ```bash
    pip install -r requirements.txt
    ```

6. Descarga el algoritmo de deteccion de rostros [Haar Cascade Face Default](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) y se agrega a la carpeta.

7. Se ejecuta el script para "escanear" la cara
    ```bash
    python ImageCapture.py
    ```
    
8. Se ejecuta el script para "entrenar" el modelo
    ```bash
    python TrainModel.py
    ```
    
9. Se ejecuta el script para "reconocer" la cara y disfruta
    ```bash
    python FaceRecognition.py
    ```
</details>
   
## Licencia 📄

Este proyecto está bajo el _MIT LICENSE_ - mira el archivo [LICENSE](LICENSE) para detalles

## Autores ✒️

[**Vicente Aguilera Arias**](https://github.com/ViceAguilera)