# Weather Web Application
This Django web application allows users to check the current weather conditions of cities around the world. It integrates with the OpenWeatherMap API to fetch real-time weather data.
## deployed here : https://shaan786.pythonanywhere.com/
## Features
Weather Information: Displays current temperature, description, and weather icon for the searched city.
Responsive Design: Built using Tailwind CSS for a modern and responsive UI.
Security: Implements CSRF protection to prevent cross-site request forgery.
## Prerequisites
Before running this project locally, ensure you have the following installed:

Python (version 3.x)
Django (version 3.x)
Git (optional, if you want to clone the repository)
## Installation
Clone the repository:

```bash
git clone git@github.com:Rashad930/weather-webapp-django.git
```

Navigate into the project directory:

```bash
cd weather-webapp-django
```
## Create a virtual environment:

```bash
python -m venv env
```

## Activate the virtual environment:

On Windows:

```bash
.\env\Scripts\activate
```
On macOS/Linux:

```bash
source env/bin/activate
```
## Install dependencies:

```bash
pip install -r requirements.txt
```
## Apply migrations:

```bash
python manage.py migrate
```
## Run the development server:

```bash
python manage.py runserver
```
## The application will be accessible at http://localhost:8000.

## Usage
Access the application through a web browser.
Enter the name of the city you want to check the weather for in the input field.
Click on the "Get Weather" button to see the current weather information for the specified city.
Technologies Used
Django
Python
HTML/CSS (Tailwind CSS)
OpenWeatherMap API

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests to propose improvements or additional features.
