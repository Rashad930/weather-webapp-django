from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '8e127bd81fa5486614eec3c28872d736'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        weather_data = response.json()
        
        weather = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
        return render(request, 'weather/index.html', {'weather': weather})
    else:
        return render(request, 'weather/index.html')
