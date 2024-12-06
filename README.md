# Cuna Inteligente - Proyecto Integrado

Bienvenido al repositorio **Cuna-Inteligente-Integrado**, una solución integral basada en IoT para el cuidado de bebés. Este proyecto combina tecnologías avanzadas de sensores, procesamiento de datos, redes neuronales y una interfaz web para proporcionar monitoreo en tiempo real, alertas automáticas y herramientas interactivas que facilitan el cuidado de los más pequeños.

---

## Descripción General del Proyecto

El proyecto **Cuna Inteligente** se diseñó para abordar las dificultades que enfrentan los cuidadores al monitorear continuamente a un bebé. Utiliza sensores para medir condiciones ambientales y patrones de actividad, junto con un modelo de inteligencia artificial que analiza el llanto del bebé para identificar posibles causas como hambre, incomodidad o sueño.

### Estructura del Proyecto

Este repositorio integra los siguientes componentes, cada uno alojado en repositorios independientes:

1. **Frontend**  
   Aplicación web desarrollada en Vue.js que permite visualizar datos en tiempo real, recibir alertas y controlar dispositivos conectados.  
   [Ver Repositorio Frontend](https://github.com/jhessika-zarate/Cuna-Inteligente-Frontend)

2. **Backend**  
   API RESTful desarrollada en Spring Boot, responsable de gestionar los datos de los sensores, almacenar registros en la base de datos y comunicarse con el frontend y los dispositivos IoT.  
   [Ver Repositorio Backend](https://github.com/jhessika-zarate/backend-cuna-inteligente)

3. **Código IoT**  
   Scripts en MicroPython para el control de sensores y actuadores en un microcontrolador ESP32, incluyendo la comunicación con el backend.  
   [Ver Repositorio IoT](https://github.com/usuario/cuna-inteligente-iot)

4. **Modelo de Red Neuronal**  
   Código en Python para el entrenamiento y la predicción de un modelo CNN que clasifica el llanto del bebé.  
   [Ver Repositorio Red Neuronal](https://github.com/LuwuVelasco/CunaInteligente)

---

## Problemática y Solución Propuesta

### Problemática

El monitoreo constante de un bebé puede ser desafiante y agotador. Los cuidadores necesitan herramientas que les permitan automatizar tareas como el control de temperatura, humedad y detección de movimientos, así como identificar patrones en el llanto del bebé.

### Solución

La **Cuna Inteligente** integra sensores IoT, procesamiento de datos y una interfaz gráfica para ofrecer una solución completa que:

- **Monitorea** las condiciones ambientales y el comportamiento del bebé.
- **Genera alertas** en tiempo real ante cambios significativos.
- **Clasifica el llanto** del bebé mediante un modelo de inteligencia artificial.
- **Proporciona control remoto** de dispositivos como un servomotor y un reproductor de audio.

---

## Tecnologías Utilizadas

- **Frontend**: Vue.js, Vite, Tailwind CSS.
- **Backend**: Spring Boot, PostgreSQL, API RESTful.
- **IoT**: ESP32, MicroPython, sensores (DHT22, PIR).
- **Modelo AI**: Python, TensorFlow, librosa, redes neuronales convolucionales (CNN).
