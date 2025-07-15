import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QIcon, QPixmap
import pygame
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name: ", self)
        self.city_name = QLineEdit(self)
        self.get_weather_button = QPushButton("Get result", self)
        self.temperature_label = QLabel(self)
        self.weather_emoji = QLabel(self)
        self.weather_description = QLabel(self)

        self.UI()
    def UI(self): 

        self.setWindowTitle("WEATHER APP")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(100, 100, 1400, 500)
        #create layout manager

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_name)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.weather_emoji)
        vbox.addWidget(self.weather_description)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_name.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.weather_emoji.setAlignment(Qt.AlignCenter)
        self.weather_description.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_name.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_emoji.setObjectName("emoji_label")
        self.weather_description.setObjectName("description_label")
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                color: #e8e8e8;
                font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
            
            QLabel#city_label {
                font-size: 28px;
                font-style: italic;
                font-weight: 500;
                color: #ffffff;
                margin: 20px 0px 10px 0px;
                letter-spacing: 0.5px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 16px 24px;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
            }
            
            QLineEdit#city_input {
                font-size: 30px;
                font-weight: bold;
                padding: 16px 20px;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
                background: rgba(255, 255, 255, 0.08);
                color: #ffffff;
                margin: 8px 40px;
                selection-background-color: #4a90e2;
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }
            
            QLineEdit#city_input:focus {
                background: rgba(255, 255, 255, 0.12);
                border: 1px solid rgba(74, 144, 226, 0.5);
                outline: none;
                box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
            }
            
            QPushButton#get_weather_button {
                font-size: 16px;
                font-weight: 600;
                padding: 14px 32px;
                margin: 20px 40px;
                border: 1px solid rgba(74, 144, 226, 0.3);
                border-radius: 10px;
                background: rgba(74, 144, 226, 0.15);
                color: #ffffff;
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }
            
            QPushButton#get_weather_button:hover {
                background: rgba(74, 144, 226, 0.25);
                border: 1px solid rgba(74, 144, 226, 0.4);
                transform: translateY(-1px);
                box-shadow: 0 6px 25px rgba(0, 0, 0, 0.4);
            }
            
            QPushButton#get_weather_button:pressed {
                background: rgba(74, 144, 226, 0.2);
                transform: translateY(0px);
                box-shadow: 0 2px 15px rgba(0, 0, 0, 0.3);
            }
            
            QLabel#temperature_label {
                font-size: 30px;
                font-weight: 300;
                color: #ffffff;
                margin: 30px 0px 20px 0px;
                letter-spacing: -1px;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
                padding: 20px 30px;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }
            
            QLabel#emoji_label {
                font-size: 50px;
                font-family: segoe UI emoji;
                margin: 15px 0px;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 24px;
                padding: 20px;
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }
            
            QLabel#description_label {
                font-size: 60px;
                font-weight: 400;
                color: #b8b8b8;
                margin: 10px 0px 20px 0px;
                letter-spacing: 0.3px;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 14px;
                padding: 12px 20px;
                backdrop-filter: blur(15px);
                -webkit-backdrop-filter: blur(15px);
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            }
        """)
        self.setFixedSize(1000, 700)
        #set music
        pygame.mixer.init()                    #loadd it
        pygame.mixer.music.load("sound.mp3")   #play it
        pygame.mixer.music.play(-1)            # make it infinite lol
        self.get_weather_button.clicked.connect(self.get_weather)               # Make the app do something when I clik on the button
    def get_weather(self):
        api_key = "146cec9aef63800a289fd87133e3d487"
        city = self.city_name.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            self.display_weather(data)
        else:
            self.display_error("ERROR! Check syntax")
    def display_error(self, message):
        self.city_label.setStyleSheet("""
                font-size: 28px;
                font-style: italic;
                font-weight: bold;
                color: #FF0000;
                margin: 20px 0px 10px 0px;
                letter-spacing: 0.5px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 16px 24px;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                """)

        self.city_label.setText(message)
    def display_weather(self, data):
        self.city_label.setStyleSheet("""
                font-size: 28px;
                font-style: italic;
                font-weight: bold;
                color: ##5CE65C;
                margin: 20px 0px 10px 0px;
                letter-spacing: 0.5px;
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 16px 24px;
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                """)
        self.city_label.setText("Success!")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        Fuck_microsoft = data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_c:.2f}℃/{temperature_f:.2f}℉")
        
        self.weather_description.setText(Fuck_microsoft)

        if 200 <= weather_id <= 232:
            self.weather_emoji.setText("⛈️")
        elif 300 <= weather_id <= 321:
            self.weather_emoji.setText("🌦️")
        elif 500 <= weather_id <= 531:
            self.weather_emoji.setText("🌧️")
        elif 600 <= weather_id <= 622:
            self.weather_emoji.setText("❄️")
        elif 701 <= weather_id <= 741:
            self.weather_emoji.setText("🌫️")
        elif weather_id == 762:
            self.weather_emoji.setText("🌋")
        elif weather_id == 771:
            self.weather_emoji.setText("🌬️")
        elif weather_id == 781:
            self.weather_emoji.setText("🌪️")
        elif weather_id == 800:
            self.weather_emoji.setText("☀️")
        elif 801 <= weather_id <= 804:
            self.weather_emoji.setText("⛅")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

