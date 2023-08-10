# WeatherNow: Secure Weather Application

WeatherNow is a secure and reliable weather application that provides real-time weather data to users. Developed using the FastAPI framework and integrated with the OpenWeather API, WeatherNow ensures accurate and up-to-date weather information. The application goes the extra mile to protect user data through advanced security measures, including JWT token-based authentication and robust password hashing.

## Features

- **Real-time Weather Data**: WeatherNow uses the OpenWeather API to fetch real-time weather information, ensuring accurate forecasts for users.
- **JWT Token-Based Authentication**: Security is a priority. WeatherNow employs JWT token-based authentication to ensure safe and authenticated user access.
- **Robust Password Hashing**: User passwords are hashed securely, enhancing data privacy and reducing vulnerabilities.
- **Docker for Deployment**: Docker is used for streamlined deployment, making it easy to run WeatherNow on various environments.
- **Efficient Data Storage**: SQLAlchemy is employed for efficient data storage and retrieval, enhancing performance and data management.

## How It Works

WeatherNow communicates with the OpenWeather API to fetch weather data. The FastAPI framework handles incoming requests, and advanced security measures, such as JWT-based authentication and password hashing, protect user data.

## Getting Started

1. Clone this repository.
2. Install the necessary dependencies. You can set up a virtual environment for this project.
   ```shell
   pip install -r requirements.txt
   ```
3. Build the Docker image for WeatherNow.
   ```shell
   docker build -t weatherapp .
   ```
4. Run the application in a Docker container.
   ```shell
   docker run -p 8000:8000 weatherapp
   ```
5. Open your browser and visit [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) to access WeatherNow running in the Docker container.