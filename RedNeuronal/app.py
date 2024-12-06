import os
import speech_recognition as sr
import librosa
import numpy as np
import tensorflow as tf
import librosa.display
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Ruta al modelo guardado
model_path = './modelo/cnn_baby_cry_classifier.h5'  
model = load_model(model_path)
print("Modelo cargado correctamente.")  

# Clases definidas manualmente, en el mismo orden que las carpetas
class_names = ['belly_pain', 'discomfort', 'hungry', 'tired']

# Directorio para almacenar los audios grabados
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Función para cargar y convertir audio a espectrograma
def audio_to_spectrogram(audio_path):
    print(f"Cargando audio desde {audio_path}...")  
    # Cargar el archivo de audio
    y, sr = librosa.load(audio_path, sr=None)  

    # Crear el espectrograma de Mel
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)

    # Convertir el espectrograma a decibelios (log-amplitude)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)

    # Convertir a una imagen RGB duplicando el canal
    spectrogram_rgb = np.stack([spectrogram_db] * 3, axis=-1)  

    # Mostrar el espectrograma (opcional)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(spectrogram_db, x_axis='time', y_axis='mel', sr=sr)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Espectrograma de Mel')
    plt.show()

    print("Espectrograma generado correctamente.")  
    return spectrogram_rgb

# Función para preprocesar el espectrograma y realizar la predicción
def classify_audio(audio_path):
    print(f"Procesando audio: {audio_path}...")  
    spectrogram = audio_to_spectrogram(audio_path)

    # Redimensionar el espectrograma para que coincida con las dimensiones de entrada del modelo
    spectrogram_resized = tf.image.resize(spectrogram, (128, 128))  
    spectrogram_resized = np.expand_dims(spectrogram_resized, axis=0)  

    # Realizar la predicción
    prediction = model.predict(spectrogram_resized)

    print(f"Predicciones del modelo: {prediction}")  

    # Obtener el índice de la clase con la mayor probabilidad
    predicted_class_index = np.argmax(prediction, axis=-1)
    print(f"Índice de la clase predicha: {predicted_class_index}")  

    # Obtener el nombre de la clase a partir del índice
    predicted_class_name = class_names[predicted_class_index[0]]

    print(f'Predicción: {predicted_class_name}') 
    return predicted_class_name

# Función para grabar el audio desde el micrófono
def record_audio():
    print("Iniciando grabación...")  
    recognizer = sr.Recognizer()

    # Usar el micrófono para grabar
    with sr.Microphone() as source:
        print("Por favor, hable ahora...")

        recognizer.adjust_for_ambient_noise(source)  

        # Si quieres grabar hasta que haya un silencio largo, puedes eliminar timeout y phrase_time_limit
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=10)  

    # Guardar el audio como un archivo WAV en el directorio de uploads
    audio_file_path = os.path.join(UPLOAD_FOLDER, "audio_grabado.wav")
    with open(audio_file_path, "wb") as f:
        f.write(audio.get_wav_data()) 

    print(f"Audio grabado y guardado en {audio_file_path}")  
    return audio_file_path


# Función principal para grabar y procesar el audio
def main():
    print("Iniciando proceso...")  
    audio_file_path = record_audio()

    # Realizar la clasificación del audio grabado
    predicted_class = classify_audio(audio_file_path)

    print(f'Clase predicha: {predicted_class}') 

if __name__ == "__main__":
    main()
