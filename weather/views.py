import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
def index(request):
	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7d01ebda491ec1bba8dafe94688cf580'
	
	
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()
	
	form = CityForm()

	cities = City.objects.all()

	weather_data=[]

	for city in cities:

		r=requests.get(url.format(city)).json()

		city_weather ={
		'city':city.name,
		'temperature':r['main']['temp'],
		'description':r['weather'][0]['description'],
		'icon':r['weather'][0]['icon'],

		}
		#print(city_weather)
		weather_data.append(city_weather)
	print(weather_data)
	context = {'weather_data':weather_data, 'form':form}
	return render(request,'weather/weather.html',context)
