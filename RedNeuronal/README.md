# Cuna Inteligente - Modelo de Red Neuronal

Este repositorio contiene el código en Python para el entrenamiento y la implementación de una red neuronal convolucional (CNN) que clasifica el llanto del bebé en diferentes categorías, como hambre, sueño o incomodidad. El modelo es parte esencial del proyecto **Cuna Inteligente**, permitiendo a los cuidadores tomar decisiones rápidas y adecuadas basadas en el motivo del llanto.

## Problemática

El llanto es el principal medio de comunicación de un bebé, pero identificar correctamente sus causas puede ser un desafío para los cuidadores. Un modelo de red neuronal puede analizar patrones en el llanto y proporcionar una clasificación precisa, ayudando a mejorar el cuidado del bebé y reducir el estrés de los padres.

## Objetivos del Modelo

- Entrenar una red neuronal convolucional para clasificar el llanto del bebé.
- Utilizar espectrogramas de audio como entrada para el modelo.
- Proporcionar predicciones en tiempo real a partir de grabaciones enviadas por el sistema IoT.
- Mejorar la precisión del modelo mediante técnicas de aumentación de datos y optimización del entrenamiento.

## Requisitos del Sistema

- Python 3.8+
- TensorFlow 2.x
- NumPy, Matplotlib, librosa

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```sh
   git clone https://github.com/usuario/cuna-inteligente-rnn.git
   cd cuna-inteligente-rnn
