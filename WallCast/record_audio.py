import wave
import pyaudio
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog


class RecordAudio(QWidget):
    def __init__(self):
        super().__init__()

        # Константы для аудио
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.RECORD_SECONDS = 600

        # Инициализация PyAudio
        self.p = pyaudio.PyAudio()

        # Создание элементов интерфейса
        self.label = QLabel(self)
        self.label.setText("Нажмите кнопку, чтобы начать запись")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 300, 50)

        self.button = QPushButton('Запись', self)
        self.button.setGeometry(100, 150, 200, 50)
        self.button.clicked.connect(self.start_recording)

        self.show()

    def start_recording(self):
        # Открытие потока записи
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

        # Запуск записи при нажатии на кнопку
        self.label.setText("Идет запись...")
        self.button.setText("Остановить")
        self.button.clicked.disconnect(self.start_recording)
        self.button.clicked.connect(self.stop_recording)

        # Запись аудио
        self.frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)
            QApplication.processEvents()  # Обновление интерфейса
            if not self.button.isEnabled():
                break

        # Остановка записи
        self.stop_recording()

    def stop_recording(self):
        # Остановка потока записи
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        # Сохранение записи
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить запись", "", "Wave files (*.wav)")
        if filename:
            wf = wave.open(filename, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            self.label.setText(f"Запись сохранена в {filename}")
        else:
            self.label.setText("Запись отменена")

        # Обновление интерфейса
        self.button.setText("Запись")
        self.button.clicked.disconnect(self.stop_recording)
        self.button.clicked.connect(self.start_recording)
