
# 🌤️ Weather GUI App

A simple Python desktop application built using **Tkinter** that allows users to check the real-time weather conditions of any city using the **OpenWeatherMap API**.

## 🖼️ Features

- User-friendly GUI using Tkinter
- Fetches current weather information including:
  - Temperature
  - Feels like temperature
  - Weather condition
  - Humidity
  - Wind speed
  - Min/Max temperature
  - Weather icon
- Error handling for:
  - Invalid city names
  - Internet connection issues

## 🛠️ Requirements

Make sure to install the following Python libraries:

```bash
pip install requests pillow
```

> 🔌 **Note:** Internet connection is required to fetch data from the OpenWeatherMap API.

## 🚀 How to Run

1. Clone this repository or download the `Weather GUI.py` file.
2. Open your terminal or command prompt.
3. Navigate to the project folder.
4. Run the application using:

```bash
python "Weather GUI.py"
```

## 🔑 API Key

This app uses the OpenWeatherMap API. You can replace the sample API key in the code with your own key by registering at:

👉 [https://openweathermap.org/api](https://openweathermap.org/api)

Replace this line in the code:
```python
api_key = "your_api_key_here"
```

## 📸 GUI Preview

![weather-gui-sample](https://user-images.githubusercontent.com/your-github-id/weather-gui-preview.png)
> *(Add a screenshot here if available)*

## 📦 Project Structure

```
📁 Weather GUI Project/
└── Weather GUI.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ using Python and Tkinter
