from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Client, SuperuserProfile

from .utils import *

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderNotFound


# Create your views here.


@login_required(login_url='logowanie')
def dashboard(request):
    username = request.session.get('username')

    try:
        User = get_user_model()
        user = User.objects.get(username=username)
        user_profile = SuperuserProfile.objects.get(user=user)

    except ObjectDoesNotExist:
        return redirect('logowanie')

    if request.method == 'POST' and 'add-client' in request.POST:
        if user_profile.permission == 0:
            messages.error(request, 'Nie masz uprawnień do dodawania klientów!')
        else:
            full_name = request.POST.get('full-name')
            installation = request.POST.get('installation')
            installation_type = request.POST.get('installation-type')
            installation_date = request.POST.get('installation-date')
            street_address = request.POST.get('street-address')
            phone_number = request.POST.get('phone-number')

            try:
                geolocator = Nominatim(user_agent="agent0")
                get_loc = geolocator.geocode(street_address, timeout=5)


                if get_loc is not None:
                    client = Client(
                        full_name=full_name, 
                        installation=installation, 
                        installation_type=installation_type,
                        installation_date=installation_date,
                        address=street_address,
                        phone_number=phone_number,
                        location_latitude=get_loc.latitude,
                        location_longitude=get_loc.longitude)
                    client.save()
                else:
                    messages.error(request, 'Nie udało się zlokalizować adresu. Spróbuj ponownie.')


            except GeocoderTimedOut:
                messages.error(request, 'Przekroczono limit czasu podczas próby geokodowania. Spróbuj ponownie.')

            except GeocoderNotFound:
                messages.error(request, 'Nie udało się zlokalizować adresu. Spróbuj ponownie.')

    map = create_admin_map(Client, user_profile.permission)

    context = {
        'map': map,
        'messages': messages.get_messages(request),
        'user_profile': user_profile,
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='logowanie')
def clients(request):
    if request.method == 'GET':
        all_clients = Client.objects.all()
        print(all_clients)

        context = {
            'all_clients': all_clients,
        }


    return render(request, 'clients.html', context)

@login_required(login_url='logowanie')
def delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    
    return HttpResponse('<script>window.parent.location="/administrator"</script>')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('administrator')

    return render(request, 'login.html')

@login_required(login_url='logowanie')
def logout_user(request):
    logout(request)

def handler404(request, exception):
    return render(request, 'errors/404.html')

def handler500(request):
    return render(request, 'errors/500.html')

def viewers_map(request):
    map = create_viewers_map(Client=Client)
    
    context = {
        'map': map,
    }

    return render(request, 'map.html', context)
    
